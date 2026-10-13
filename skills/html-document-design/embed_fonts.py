#!/usr/bin/env python3
"""
embed_fonts.py — HTML 문서에 한글 웹폰트를 base64로 박아 넣는다.

외부 CDN(@import / <link>)을 지우고 그 자리에 @font-face + data: URI 를 넣는다.
결과 파일은 네트워크가 전혀 없어도 의도한 서체로 렌더된다.
사내망·OneDrive 공유·오프라인 열람용 산출물에 쓴다.

사용:
    python3 embed_fonts.py doc.html                 # 기본 = fixed (KS X 1001 2350자)
    python3 embed_fonts.py doc.html --mode doc      # 이 문서에 실제로 쓰인 글자만
    python3 embed_fonts.py doc.html -o out.html
    python3 embed_fonts.py deck.html --family pretendard   # 슬라이드 HTML 등 Pretendard 문서

서체 묶음 (--family)
    plex        IBM Plex Sans KR / IBM Plex Mono / Nanum Gothic Coding  (기본, HTML 문서)
    pretendard  Pretendard 400·500·600·700·800                          (슬라이드 HTML)

사내 공유용일 때만 돌린다. 내 PC 저장용은 임베드하지 않는다.

모드
    fixed  한글 2350자 고정 세트. 문서당 약 +1.3MB.
           나중에 손으로 문장을 고쳐도 글자가 깨지지 않는다. 이쪽이 기본.
    doc    문서에 실제로 등장한 글자만. 약 +0.3MB.
           가볍지만, 이후 새 한글을 손으로 넣으면 그 글자만 대체 서체로 떨어진다.

필요: python3 -m pip install fonttools brotli   /   node + npm (폰트 내려받기용, 최초 1회)
"""

import argparse
import base64
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile

CACHE = os.path.expanduser("~/.cache/ap-doc-fonts")

# 서체 묶음: (CSS family, npm 패키지, 패키지 안 폴더, 파일명 패턴, 굵기들)
# 파일명 패턴의 {w} 는 굵기 숫자, {n} 은 굵기 이름(Pretendard 용)
FAMILIES = {
    "plex": [
        ("IBM Plex Sans KR", "@fontsource/ibm-plex-sans-kr", "files",
         "ibm-plex-sans-kr-korean-{w}-normal.woff2", [400, 500, 600, 700]),
        ("IBM Plex Mono", "@fontsource/ibm-plex-mono", "files",
         "ibm-plex-mono-latin-{w}-normal.woff2", [400, 500]),
        ("Nanum Gothic Coding", "@fontsource/nanum-gothic-coding", "files",
         "nanum-gothic-coding-korean-{w}-normal.woff2", [400, 700]),
    ],
    "pretendard": [
        ("Pretendard", "pretendard", "dist/web/static/woff2",
         "Pretendard-{n}.woff2", [400, 500, 600, 700, 800]),
    ],
}

WEIGHT_NAMES = {400: "Regular", 500: "Medium", 600: "SemiBold", 700: "Bold", 800: "ExtraBold"}

PUNCT = (
    "←→↑↓·—–…“”‘’•※°±×÷≤≥≠∞⇒✓✗√"
    "①②③④⑤⑥⑦⑧⑨⑩⑪⑫"
    "　、。「」『』〈〉《》【】〔〕"
    "₩€£¥©®™§¶†‡"
)


def ks_x_1001_hangul():
    """KS X 1001 완성형 한글 2350자."""
    out = []
    for cp in range(0xAC00, 0xD7A4):
        ch = chr(cp)
        try:
            b = ch.encode("euc-kr")
        except UnicodeEncodeError:
            continue
        if len(b) == 2 and b[0] >= 0xA1 and b[1] >= 0xA1:
            out.append(ch)
    return "".join(out)


def base_charset():
    ascii_ = "".join(chr(c) for c in range(0x20, 0x7F))
    latin1 = "".join(chr(c) for c in range(0xA0, 0x100))
    jamo = "".join(chr(c) for c in range(0x3131, 0x3164))
    return ascii_ + latin1 + jamo + PUNCT


def doc_chars(source):
    """HTML 본문에서 실제로 화면에 나오는 글자만 추린다."""
    body = source
    body = re.sub(r"<style\b.*?</style>", " ", body, flags=re.S | re.I)
    body = re.sub(r"<script\b.*?</script>", " ", body, flags=re.S | re.I)
    body = re.sub(r"<[^>]+>", " ", body)
    body = html.unescape(body)
    return "".join(sorted({c for c in body if c.strip()}))


def ensure_fonts(faces):
    """폰트 패키지를 캐시에 준비한다. 이미 있으면 건너뛴다."""
    pkgs = sorted({f[1] for f in faces})
    need = [p for p in pkgs
            if not os.path.isdir(os.path.join(CACHE, "node_modules", *p.split("/")))]
    if not need:
        return
    if not shutil.which("npm"):
        sys.exit("npm 이 필요합니다 (폰트 내려받기 최초 1회). node 를 설치한 뒤 다시 실행하세요.")
    os.makedirs(CACHE, exist_ok=True)
    if not os.path.exists(os.path.join(CACHE, "package.json")):
        subprocess.run(["npm", "init", "-y"], cwd=CACHE,
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"폰트 내려받는 중 … ({', '.join(need)})", file=sys.stderr)
    subprocess.run(["npm", "install", *need], cwd=CACHE,
                   check=True, stdout=subprocess.DEVNULL)


def subset(src, chars, out):
    from fontTools import subset as ftsubset
    args = [
        src,
        f"--text={chars}",
        "--flavor=woff2",
        "--layout-features=*",
        "--no-hinting",
        "--desubroutinize",
        f"--output-file={out}",
    ]
    ftsubset.main(args)


def build_css(chars, weights_note, faces):
    blocks = [f"/* 폰트 임베드 — {weights_note}. 외부 네트워크 불필요 */"]
    total = 0
    with tempfile.TemporaryDirectory() as tmp:
        for family, pkg, sub, pattern, weights in faces:
            for w in weights:
                src = os.path.join(CACHE, "node_modules", *pkg.split("/"),
                                   *sub.split("/"),
                                   pattern.format(w=w, n=WEIGHT_NAMES.get(w, "")))
                if not os.path.exists(src):
                    print(f"  건너뜀 (파일 없음): {os.path.basename(src)}", file=sys.stderr)
                    continue
                dst = os.path.join(tmp, f"{family}-{w}.woff2".replace(" ", "-"))
                subset(src, chars, dst)
                data = open(dst, "rb").read()
                total += len(data)
                b64 = base64.b64encode(data).decode("ascii")
                blocks.append(
                    "@font-face{font-family:'%s';font-style:normal;font-weight:%d;"
                    "font-display:swap;src:url(data:font/woff2;base64,%s) format('woff2')}"
                    % (family, w, b64)
                )
                print(f"  {family} {w} — {len(data)//1024} KB", file=sys.stderr)
    return "\n".join(blocks), total


IMPORT_RE = re.compile(
    r"@import\s+url\(\s*['\"]?https://(?:fonts\.googleapis\.com|cdn\.jsdelivr\.net/gh/orioncactus/pretendard)/[^)]*\)\s*;", re.I)
LINK_RE = re.compile(
    r"<link[^>]+(?:fonts\.(?:googleapis|gstatic)\.com|orioncactus/pretendard)[^>]*>\s*", re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-o", "--output")
    ap.add_argument("--mode", choices=["fixed", "doc"], default="fixed")
    ap.add_argument("--family", choices=list(FAMILIES), default="plex")
    args = ap.parse_args()
    faces = FAMILIES[args.family]

    src = open(args.input, encoding="utf-8").read()

    if args.mode == "fixed":
        chars = ks_x_1001_hangul() + base_charset()
        note = "KS X 1001 한글 2350자 고정 세트"
    else:
        chars = doc_chars(src) + base_charset()
        note = "이 문서에 쓰인 글자만"
    chars = "".join(sorted(set(chars)))
    print(f"모드 {args.mode} — 글자 {len(chars)}자", file=sys.stderr)

    ensure_fonts(faces)
    css, total = build_css(chars, note, faces)

    out = LINK_RE.sub("", src)
    if IMPORT_RE.search(out):
        out = IMPORT_RE.sub(css, out, count=1)
    elif "<style>" in out:
        out = out.replace("<style>", "<style>\n" + css, 1)
    else:
        out = f"<style>\n{css}\n</style>\n" + out

    dst = args.output or re.sub(r"\.html?$", "", args.input) + "_embed.html"
    open(dst, "w", encoding="utf-8").write(out)

    before = len(src.encode("utf-8")) / 1024
    after = len(out.encode("utf-8")) / 1024
    print(f"\n{dst}", file=sys.stderr)
    print(f"폰트 {total//1024} KB → 문서 {before:.0f} KB → {after:.0f} KB", file=sys.stderr)


if __name__ == "__main__":
    main()
