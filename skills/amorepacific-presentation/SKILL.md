---
name: amorepacific-presentation
description: 'HTML 슬라이드로 아모레퍼시픽 사내 보고·발표자료를 만들거나, 기존 슬라이드 HTML의 레이아웃·여백·컬러·문구를 고칠 때 항상 적용. BY27 템플릿 규격과 로고·푸터 자산을 적용해 단독 실행되는 단일 HTML 파일 하나를 산출한다. Use when creating or editing an AMOREPACIFIC internal presentation slide in HTML.'
---

# AMOREPACIFIC Presentation

사내 보고용 발표자료를 HTML 슬라이드 덱으로 만드는 스킬입니다. 산출물은 항상 **Base64 자산이 내장된 단일 .html 파일 1개**이며, 받는 사람이 더블클릭만 하면 로고와 푸터까지 그대로 보여야 합니다. 로고·푸터 이미지는 항상 내장하고, **폰트는 파일에 담지 않습니다.** 서체는 전사 PC에 자동 설치되는 아리따 돋움(Arita Dotum KR)이고, 템플릿이 이름으로 불러 씁니다.

## 작업 순서

1. **내용을 먼저 정한다.** 슬라이드 제목만 순서대로 읽어도 논지가 완성되는지 확인합니다. 제목은 "현황 및 문제점" 같은 라벨이 아니라 결론 문장으로 씁니다.
2. **레이아웃을 고른다.** `reference.md`의 Layout Patterns(5.4)과 Slide Type Library(8)에서 슬라이드마다 하나씩 선택합니다.
3. **HTML을 만든다.** `templates/base_slide.html`을 뼈대로 삼고, CSS 변수와 규격은 `reference.md`를 따릅니다.
4. **자산을 내장한다.** `python3 scripts/embed_assets.py <파일.html>` 을 실행하면 플레이스홀더가 Base64 data URI로 치환됩니다.
5. **검수한다.** `reference.md`의 Final Quality Checklist(14)를 확인합니다. 특히 콘텐츠가 footer line을 침범하지 않는지 실제로 렌더링해서 봅니다.

## 반드시 지킬 것

- Canvas 1920×1080, 배경 흰색, `transform: scale()`로 뷰포트 대응
- AMORE Blue는 **강조**, PACIFIC Blue는 **구조**(제목·표 헤더·백본)
- 얇은 선(1px, opacity 0.35~0.4) + 넓은 여백. 굵은 박스나 진한 그림자 금지
- 로고와 슬로건은 절대 텍스트로 재현하지 않고 `assets/`의 PNG를 사용
- 모든 콘텐츠 슬라이드에 footer 두 개 고정, 페이지 번호는 하단 중앙 2자리(01, 02…)
- 모든 본문(콘텐츠) 슬라이드 우상단에 Content Header 고정. 표지에는 쓰지 않음
- 한 슬라이드 = 하나의 메시지, 텍스트 계층 3단계 이하
- 출력 파일명은 소문자 + 언더스코어: `<주제>_<문서성격>.html`

## 자산 좌표 (1920×1080 기준)

| 자산 | 파일 | 위치 |
|---|---|---|
| Cover Header | `assets/cover_header_amorepacific.png` | left 160 / top 108 / width 331 |
| Content Header | `assets/content_header_amorepacific.png` | right 39 / top 74 / width 231 |
| Footer Left | `assets/footer_left_create_new_beauty.png` | left 32 / bottom 4 / width 283 |
| Footer Right | `assets/footer_right_beauty_in_motion.png` | right 12 / bottom 4 / width 283 |

Cover Header는 표지에만, Content Header는 본문 슬라이드에만 씁니다. 서로 대신 쓰지 않습니다. Footer Right는 우측 여백이 12px로 매우 좁으므로 콘텐츠와 겹치지 않는지 렌더링해서 육안으로 확인하십시오.

## 플레이스홀더

HTML 작성 중에는 `src` 자리에 아래 토큰을 그대로 두고, 마지막에 `embed_assets.py`로 치환합니다.

```html
<img class="cover-header"   src="{{ASSET:cover_header}}"   alt="AMOREPACIFIC">
<img class="content-header" src="{{ASSET:content_header}}" alt="AMOREPACIFIC">
<img class="footer-left"    src="{{ASSET:footer_left}}"    alt="Create New Beauty">
<img class="footer-right"   src="{{ASSET:footer_right}}"   alt="Beauty in Motion">
```

치환 후 파일 안에 `assets/` 나 `{{ASSET:` 문자열이 남아 있으면 실패입니다. 스크립트가 이 검사를 대신 해 줍니다.

## 폰트 (아리따 돋움)

슬라이드 서체는 아리따 돋움(Arita Dotum KR)입니다. 전사 PC에 자동 설치되므로 파일에 담지 않고, 질문도 하지 않습니다. 템플릿의 `@font-face`가 `local()`로 설치된 폰트를 이름으로 연결합니다.

- 이 서체는 굵기마다 파일이 따로이고 **Regular가 없습니다.** 파일은 Thin·Light·Medium·SemiBold·Bold 5종이며, 파일 안의 서체 이름은 "Arita Dotum KR Bold"처럼 굵기가 붙어 있습니다(2026-10-13 맥 설치본에서 확인).
- 그래서 템플릿은 본문(400·500)을 Medium, 600을 SemiBold, 700·800을 Bold로 연결합니다. 800은 별도 파일이 없어 Bold입니다. 이 `@font-face` 블록을 지우지 마십시오.
- 설치되지 않은 PC(외부 공유 등)는 Pretendard → 맑은 고딕 순으로 대체됩니다. 가변 폰트판 Pretendard는 "Pretendard Variable"이라는 다른 이름으로 등록되므로(2026-10-13 맥 설치본에서 확인) 서체 목록에 두 이름을 모두 둡니다. 이 경우 줄바꿈과 박스 안 여백이 틀어질 수 있습니다.
- 제목의 자간(`letter-spacing`)은 원래 Pretendard 기준으로 잡은 값입니다. 아리따는 자간이 넓은 서체라 같은 값에서도 느낌이 다를 수 있으니, 렌더링해서 확인하십시오.

## 수치는 CSS 변수로 뺀다

여백·카드 높이·행 간격처럼 나중에 손으로 다시 맞출 값은 반드시 `:root`의 CSS 변수로 선언하고, 규칙에서는 `var(--pad-t)` 형태로만 참조합니다. 값이 규칙 안에 흩어져 있으면 사용자가 직접 조정할 수 없습니다.

```css
:root{ --card-h:530px; --row-gap:14px; --pad-t:18px; --pad-x:28px; --pad-b:14px; }
.panel{ padding:var(--pad-t) var(--pad-x) var(--pad-b) }
```

그 위에 `templates/layout_tuner.html`을 `</body>` 앞에 붙여넣으면, 브라우저에서 T 키로 슬라이더 패널을 열어 값을 눈으로 맞추고 "값 복사하기"로 확정할 수 있습니다. 패널은 박스마다 남은 여백과 footer line까지의 거리를 실시간으로 표시하며, 음수가 되면 빨갛게 경고합니다. 슬라이드를 만들 때 이 패널을 기본으로 넣어 두십시오.

## 직접 수정 모드

템플릿에는 브라우저에서 글자를 바로 고치는 모드가 들어 있습니다. HTML을 열고 **E 키**를 누르면 글자가 있는 요소를 클릭해 고칠 수 있고, 아래에 뜨는 막대의 **수정본 저장**(또는 Ctrl/Cmd+S)을 누르면 `<파일명>_edited.html`이 내려받아집니다. Esc 또는 **편집 끝**으로 나옵니다. 막대의 ◀ ▶로 슬라이드를 넘깁니다.

- 글자 고치기 전용입니다. 카드·행·슬라이드를 늘리거나 줄이는 일은 Claude에게 맡깁니다.
- 붙여넣기는 서식 없이 글자만 들어가고, Enter는 줄바꿈입니다.
- 저장본에는 편집용 속성과 막대가 남지 않습니다. `layout_tuner`로 맞춘 여백 값은 저장본에 그대로 남습니다.
- 템플릿의 이 스크립트(`setEdit`, `snapshot`)와 `layout_tuner.html`의 키 가드를 지우지 마십시오. 슬라이드를 새로 만들 때 `base_slide.html`을 뼈대로 쓰면 자동으로 들어갑니다.
- 브라우저에서 직접 연 경우에만 동작합니다. 미리보기(맥 Finder)나 스크립트가 막힌 뷰어에서는 안 됩니다.

## PPTX가 필요할 때

최종 발표용으로 PowerPoint에서 레이아웃을 직접 다듬어야 하면 `slide-to-pptx` 스킬로 변환합니다. 이 스킬에서는 HTML까지만 책임집니다.

## 자주 나는 실수

- **슬라이드가 좁은 창에서 찌그러진다.** 스케일 컨테이너를 flex로 잡으면 고정 폭 1920px 슬라이드가 flex-shrink 기본값 1 때문에 컨테이너 폭에 맞춰 줄어들고, 그 상태에서 텍스트가 재배치된 뒤 scale이 걸립니다. 슬라이드에 `flex:0 0 auto`를 반드시 넣으십시오.
- **미리보기 패널에서만 크기가 안 맞는다.** `resize` 이벤트는 브라우저 창 크기에만 반응합니다. iframe이나 패널 안에서 쓰려면 `ResizeObserver`로도 `fit()`을 호출해야 합니다.
- **맥 Finder 미리보기(스페이스바)에서 슬라이드가 잘려 보인다.** 미리보기는 스크립트를 돌리지 않아서 `fit()`이 실행되지 않습니다. 템플릿의 `<noscript><style>`이 이 경우에만 모든 슬라이드를 세로로 쌓고 창 폭에 맞춰 줄입니다. 템플릿에서 이 블록을 지우지 마십시오. 브라우저(스크립트 켜짐)에서는 적용되지 않습니다.
- **하단 강조 박스가 footer line을 침범한다.** 고정 높이 그리드 행의 합이 콘텐츠 영역보다 크면 아래로 넘칩니다. 렌더링해서 실제 좌표를 확인하십시오.

## 세부 규격

색상 팔레트, 타이포 스케일, 컴포넌트 라이브러리, 다이어그램·차트 규칙, 슬라이드 타입 15종, 문장 톤 가이드는 모두 `reference.md`에 있습니다. 슬라이드를 실제로 그리기 전에 해당 절을 읽으십시오.
