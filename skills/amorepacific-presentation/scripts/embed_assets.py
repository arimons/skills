#!/usr/bin/env python3
"""HTML 안의 {{ASSET:...}} 플레이스홀더를 Base64 data URI로 치환한다.

사용법:
    python3 scripts/embed_assets.py deck.html            # 제자리 치환
    python3 scripts/embed_assets.py deck.html out.html   # 다른 파일로 저장

토큰: {{ASSET:cover_header}} {{ASSET:content_header}} {{ASSET:footer_left}} {{ASSET:footer_right}}
"""
import base64
import pathlib
import re
import sys

ASSET_DIR = pathlib.Path(__file__).resolve().parent.parent / "assets"

ASSETS = {
    "cover_header": "cover_header_amorepacific.png",
    "content_header": "content_header_amorepacific.png",
    "footer_left": "footer_left_create_new_beauty.png",
    "footer_right": "footer_right_beauty_in_motion.png",
}


def data_uri(name: str) -> str:
    path = ASSET_DIR / ASSETS[name]
    if not path.exists():
        sys.exit(f"[에러] 자산을 찾을 수 없습니다: {path}")
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{b64}"


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)

    src = pathlib.Path(sys.argv[1])
    dst = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else src
    html = src.read_text(encoding="utf-8")

    used = 0
    for name in ASSETS:
        token = "{{ASSET:%s}}" % name
        if token in html:
            html = html.replace(token, data_uri(name))
            used += 1

    # assets/ 직접 참조도 함께 흡수한다
    for name, filename in ASSETS.items():
        html = re.sub(
            r'src\s*=\s*["\'][^"\']*%s["\']' % re.escape(filename),
            'src="%s"' % data_uri(name),
            html,
        )

    dst.write_text(html, encoding="utf-8")

    leftovers = []
    if "{{ASSET:" in html:
        leftovers.append("치환되지 않은 {{ASSET:...}} 토큰")
    if "assets/" in html:
        leftovers.append('남아있는 "assets/" 외부 참조')

    print(f"자산 {used}종 내장 완료 → {dst} ({dst.stat().st_size / 1024:.0f} KB)")
    if leftovers:
        print("[경고] " + " / ".join(leftovers))
        sys.exit(1)
    print("검증 통과: 단독 실행 가능한 HTML입니다.")


if __name__ == "__main__":
    main()
