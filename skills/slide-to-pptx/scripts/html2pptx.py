#!/usr/bin/env python3
"""1920x1080 고정 좌표 HTML 슬라이드를 편집 가능한 PPTX로 옮긴다.

    python3 html2pptx.py deck.html deck.pptx [--font "Arita Dotum KR Medium" [--font-bold "Arita Dotum KR Bold"]]

브라우저에서 각 요소의 최종 좌표와 스타일을 읽어, 같은 자리에 PPT 도형과
텍스트 상자를 놓는다. 1920px = 13.333in 이므로 1px = 1/144in.

줄바꿈은 브라우저가 실제로 끊은 위치를 그대로 옮기고 PPT의 자동 줄바꿈은
꺼버린다. 받는 사람 PC에 폰트가 없어도 줄 모양이 무너지지 않는다.
"""
import base64
import io
import json
import pathlib
import sys

from playwright.sync_api import sync_playwright
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.util import Emu, Pt

PX = 914400 / 144.0  # 1px -> EMU
# 아리따 돋움은 굵기마다 파일·서체 이름이 따로이고 Regular가 없다(예: "Arita Dotum KR Bold").
# 그래서 굵은 글씨는 bold 속성 대신 Bold 서체 이름을 쓴다(속성을 켜면 한 번 더 굵어진다).
FONT = "Arita Dotum KR Medium"
FONT_BOLD = "Arita Dotum KR Bold"

EXTRACT = r"""
() => {
  const page = document.querySelector('.page, .slide');
  const pr = page.getBoundingClientRect();
  const scale = pr.width / page.offsetWidth;
  const px = v => v / scale;
  const rectOf = el => {
    const r = el.getBoundingClientRect();
    return {x: px(r.left - pr.left), y: px(r.top - pr.top), w: px(r.width), h: px(r.height)};
  };
  const rgb = s => {
    const m = (s || '').match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(',').map(Number);
    if (p.length > 3 && p[3] === 0) return null;
    return [p[0], p[1], p[2]];
  };
  const INLINE = new Set(['B','STRONG','SPAN','I','EM','SMALL','CODE','A','BR']);
  const out = [];

  const walk = el => {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') return;
    const r = rectOf(el);
    if (r.w < 0.5 || r.h < 0.5) return;

    if (el.tagName === 'IMG') {
      out.push({kind: 'image', rect: r, src: el.getAttribute('src'), cls: el.className});
      return;
    }

    const bg = rgb(cs.backgroundColor);
    const sides = ['Top', 'Right', 'Bottom', 'Left'].map(s => ({
      side: s.toLowerCase(),
      w: parseFloat(cs['border' + s + 'Width']),
      c: rgb(cs['border' + s + 'Color']),
    })).filter(b => b.w > 0.4 && b.c);
    const radius = parseFloat(cs.borderTopLeftRadius) || 0;
    if (bg || sides.length) {
      out.push({kind: 'box', rect: r, bg, sides, radius,
                pad: [cs.paddingTop, cs.paddingRight, cs.paddingBottom, cs.paddingLeft].map(parseFloat)});
    }

    const kids = [...el.childNodes];
    const isInline = n => INLINE.has(n.tagName) && getComputedStyle(n).display === 'inline';
    const hasOwnText = kids.some(n => n.nodeType === 3 && n.textContent.trim());
    const blockKids = kids.filter(n => n.nodeType === 1 && !isInline(n));
    const isContainer = /flex|grid/.test(cs.display);

    if (!isContainer && (hasOwnText || (kids.length && blockKids.length === 0)) && el.textContent.trim()) {
      const styleOf = e => {
        const s = getComputedStyle(e);
        return {size: parseFloat(s.fontSize), bold: parseInt(s.fontWeight) >= 600,
                color: rgb(s.color) || [0, 0, 0]};
      };
      // 브라우저가 실제로 끊은 줄을 그대로 뜯어낸다 → PPT에서 재줄바꿈이 일어나지 않음
      const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      const range = document.createRange();
      const lines = [];
      let node;
      while ((node = walker.nextNode())) {
        const st = styleOf(node.parentElement);
        const text = node.textContent;
        const toks = text.match(/\S+\s*/g) || [];
        let i = 0;
        for (const tok of toks) {
          const a = text.indexOf(tok, i), b = a + tok.length;
          i = b;
          range.setStart(node, a); range.setEnd(node, b);
          const rc = range.getClientRects();
          if (!rc.length) continue;
          const top = Math.round(rc[0].top);
          let line = lines[lines.length - 1];
          if (!line || Math.abs(line.top - top) > 2) { line = {top, runs: []}; lines.push(line); }
          const last = line.runs[line.runs.length - 1];
          if (last && last.size === st.size && last.bold === st.bold &&
              String(last.color) === String(st.color)) last.t += tok;
          else line.runs.push({t: tok, ...st});
        }
      }
      lines.forEach(l => {
        const last = l.runs[l.runs.length - 1];
        if (last) last.t = last.t.replace(/\s+$/, '');
      });
      const base = styleOf(el);
      const p = [cs.paddingTop, cs.paddingRight, cs.paddingBottom, cs.paddingLeft].map(parseFloat);
      const bw = ['Top', 'Right', 'Bottom', 'Left'].map(s => parseFloat(cs['border' + s + 'Width']));
      out.push({kind: 'text', lines,
                rect: {x: r.x + p[3] + bw[3], y: r.y + p[0] + bw[0],
                       w: r.w - p[1] - p[3] - bw[1] - bw[3], h: r.h - p[0] - p[2] - bw[0] - bw[2]},
                align: cs.textAlign, size: base.size,
                lh: parseFloat(cs.lineHeight) || base.size * 1.3, color: base.color});
      return;
    }
    kids.filter(n => n.nodeType === 1).forEach(walk);
  };

  [...page.children].forEach(walk);
  return out;
}
"""


def color(c):
    return RGBColor(int(c[0]), int(c[1]), int(c[2]))


def build(html_path: str, out_path: str, font: str = FONT, font_bold: str | None = None) -> None:
    if font_bold is None and font == FONT:
        font_bold = FONT_BOLD
    url = pathlib.Path(html_path).resolve().as_uri()
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 2100, "height": 1300})
        pg.goto(url)
        pg.wait_for_timeout(600)
        items = pg.evaluate(EXTRACT)
        b.close()

    prs = Presentation()
    prs.slide_width, prs.slide_height = Emu(int(1920 * PX)), Emu(int(1080 * PX))
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    def E(v):
        return Emu(int(round(v * PX)))

    for it in items:
        r = it["rect"]
        if it["kind"] == "image":
            src = it["src"]
            if not src.startswith("data:"):
                continue
            raw = base64.b64decode(src.split(",", 1)[1])
            slide.shapes.add_picture(io.BytesIO(raw), E(r["x"]), E(r["y"]), E(r["w"]), E(r["h"]))

        elif it["kind"] == "box":
            radius = it["radius"]
            shp_type = MSO_SHAPE.ROUNDED_RECTANGLE if radius > 1 else MSO_SHAPE.RECTANGLE
            shp = slide.shapes.add_shape(shp_type, E(r["x"]), E(r["y"]), E(r["w"]), E(r["h"]))
            if radius > 1:
                try:
                    shp.adjustments[0] = min(0.5, radius / min(r["w"], r["h"]))
                except Exception:
                    pass
            if it["bg"]:
                shp.fill.solid()
                shp.fill.fore_color.rgb = color(it["bg"])
            else:
                shp.fill.background()
            shp.shadow.inherit = False
            sides = it["sides"]
            full = len(sides) == 4 and len({round(s["w"], 1) for s in sides}) == 1
            if full:
                shp.line.color.rgb = color(sides[0]["c"])
                shp.line.width = Pt(sides[0]["w"] / 2)
            else:
                shp.line.fill.background()
                for s in sides:                     # 한쪽 변만 있는 선은 얇은 사각형으로
                    w, h, x, y = r["w"], r["h"], r["x"], r["y"]
                    if s["side"] == "left":
                        w = s["w"]
                    elif s["side"] == "right":
                        x, w = x + r["w"] - s["w"], s["w"]
                    elif s["side"] == "top":
                        h = s["w"]
                    else:
                        y, h = y + r["h"] - s["w"], s["w"]
                    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, E(x), E(y), E(w), E(h))
                    bar.fill.solid()
                    bar.fill.fore_color.rgb = color(s["c"])
                    bar.line.fill.background()
                    bar.shadow.inherit = False

        else:  # text
            tw, tx = r["w"], r["x"]
            if tw < 70:                              # 좁은 상자는 재줄바꿈 방지용 폭 확보
                tx, tw = tx - (70 - tw) / 2, 70
            tb = slide.shapes.add_textbox(E(tx), E(r["y"]), E(tw), E(max(r["h"], 8)))
            tf = tb.text_frame
            tf.word_wrap = False                     # 줄은 이미 확정되어 있다
            tf.auto_size = MSO_AUTO_SIZE.NONE        # 상자 크기 자동 변경 금지
            tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
            tf.vertical_anchor = MSO_ANCHOR.TOP
            align = {"right": PP_ALIGN.RIGHT, "center": PP_ALIGN.CENTER}.get(
                it["align"], PP_ALIGN.LEFT)
            for n, line in enumerate(it["lines"]):
                para = tf.paragraphs[0] if n == 0 else tf.add_paragraph()
                para.alignment = align
                para.line_spacing = Pt(it["lh"] / 2)
                for run in line["runs"]:
                    rn = para.add_run()
                    rn.text = run["t"]
                    rn.font.size = Pt(run["size"] / 2)
                    if run["bold"] and font_bold:
                        rn.font.name, rn.font.bold = font_bold, False
                    else:
                        rn.font.name, rn.font.bold = font, run["bold"]
                    rn.font.color.rgb = color(run["color"])

    # 눈으로 보지 않아도 걸러지는 것들만 자동 점검한다
    warn = []
    if len(items) < 5:
        warn.append(f"추출된 요소가 {len(items)}개뿐입니다. 캔버스 최상위 요소의 class가 "
                    ".page 또는 .slide인지 확인하십시오.")
    out_of_canvas = sum(
        1 for sh in slide.shapes
        if sh.left < -Emu(int(2 * PX)) or sh.top < -Emu(int(2 * PX))
        or sh.left + sh.width > prs.slide_width + Emu(int(2 * PX))
        or sh.top + sh.height > prs.slide_height + Emu(int(2 * PX)))
    if out_of_canvas:
        warn.append(f"{out_of_canvas}개 개체가 슬라이드 밖으로 나갔습니다. "
                    "원본 HTML이 1920x1080을 넘었을 수 있습니다.")

    prs.save(out_path)
    print(f"{len(items)}개 요소 → {out_path}")
    for w in warn:
        print("  [확인 필요]", w)
    if not warn:
        print("  자동 점검 통과 — 그대로 쓰셔도 됩니다.")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    font, font_bold = FONT, None
    if "--font-bold" in args:
        i = args.index("--font-bold")
        font_bold = args[i + 1]
        del args[i:i + 2]
    if "--font" in args:
        i = args.index("--font")
        font = args[i + 1]
        del args[i:i + 2]
    if len(args) < 2:
        sys.exit(__doc__)
    build(args[0], args[1], font, font_bold)
