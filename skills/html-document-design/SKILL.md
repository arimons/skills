---
name: html-document-design
description: 박창현의 개인 HTML 문서 디자인 가이드. HTML 문서·보고서·기획서·가이드·아티팩트를 만들거나 수정할 때 항상 적용. 라이트 모드 기본 + 기기 추종 그레이 다크모드 + 테마 전환 버튼, HTML 문서 서체 IBM Plex Sans KR(슬라이드는 별도 스킬의 아리따 돋움), AMORE/PACIFIC Blue 토큰, 한·영 고정폭 Nanum Gothic Coding 통일 및 수치 표 정렬 규칙 포함. Use when creating or editing any HTML document, report, or artifact.
---

# HTML Document Design — 박창현 개인 가이드

스크롤형 HTML 문서(보고서·기획서·가이드·아티팩트)에 항상 적용한다.
슬라이드 발표자료는 이 스킬이 아니라 별도의 presentation skill을 따른다.
동봉된 `base.css`가 이 가이드의 구현체다 — 새 문서를 만들 때 이 토큰과 컴포넌트를 그대로 인라인하여 사용한다.

## 핵심 원칙 (반드시 준수)

1. **라이트 모드 기본.** 흰 배경(#FFFFFF), 본문 #333333.
2. **다크 모드는 기기 설정 자동 추종**하되 **무채색 그레이 톤** — 배경 #161618(검정에서 살짝 올라간 그레이), 표면 #1E1E21. **네이비·유채색 배경 금지.** 순수 #000도 금지(대비 과다). 헤드라인은 다크에서 near-white(#F0F0F2).
3. **모든 색은 CSS 변수(토큰)로만.** 컴포넌트 규칙에 hex 직접 기입 금지. 다크 블록 안에서만 정의되는 색 금지(라이트 미정의 → 렌더 깨짐 1순위 원인). body 배경 반드시 명시.
4. **테마는 3단 패턴**: 바닥 `:root`에 라이트 전체 팔레트 → `@media (prefers-color-scheme: dark)` 안에서 `:root:not([data-theme="light"])`로 다크 토큰 재정의 → `:root[data-theme="dark"]`로 수동 지정 대응.
4b. **테마 전환 버튼을 반드시 넣는다.** 기기 설정 추종만으로는 부족하다. 문서 우측 상단에 `시스템 → 라이트 → 다크` 3단 순환 버튼을 두고, 선택은 `localStorage`에 try/catch로 보관한다. `시스템`일 때는 `data-theme` 속성을 지운다. 인쇄 시 숨긴다.
5. **서체는 파일 형식으로 정한다.** HTML 문서는 IBM Plex Sans KR, 슬라이드는 아리따 돋움(`amorepacific-presentation` 스킬)이다. 공유 경로(사내 여부)로 나누지 않는다("서체" 절). 헤딩은 h1·h2가 weight 700 + letter-spacing -0.02em, h3는 600 + -0.01em, 색은 --head. 위계는 3단계 이하. (Plex는 700이 최대 굵기다. 문서에 아리따를 쓰라고 요청받은 경우에만 `data-font="arita"`가 자간을 조인다.)
6. **이미지는 기본적으로 문서 안에 넣는다.** 이미지·아이콘은 `data:` URI(base64)로 인라인하고, 다이어그램은 이미지 대신 인라인 SVG를 우선한다. 예외: 이미지가 수십 장인 인터랙티브 보고서는 상대 링크를 쓴다("이미지가 많은 인터랙티브 보고서" 절). **폰트는 파일에 담지 않는다.** Google Fonts(Plex)를 이름으로 불러온다.
7. **한·영 고정폭 서체는 Nanum Gothic Coding으로 통일한다.** 코드·로그·실행 ID·경로·수치·mono 라벨에는 `"Nanum Gothic Coding", "D2Coding", monospace`를 사용한다. IBM Plex Mono를 앞에 두지 않는다. Google Fonts 환경에서는 Nanum Gothic Coding(400;700)을 로드한다. 서체 비교에서 Plex Mono와 Nanum Gothic Coding을 비교한다면 Plex Mono의 한글도 Nanum으로 대체되어 같게 보인다는 점을 표시한다.

## 글은 어떻게 쓰나

이 스킬은 **어떻게 보이는가**만 다룬다. 문장을 어떤 목소리로 쓸지는 `manual-voice` 스킬에 있다.

설명하는 성격의 문서 — 매뉴얼·가이드·튜토리얼·교재 — 를 HTML로 만들 때는 **`manual-voice`가 설치되어 있으면 두 스킬을 함께 적용한다. 설치되지 않았다면 사용자가 요청한 문체를 따른다. `manual-voice`는 이 묶음에 포함되지 않은 선택 의존성이다.** 잘 만든 판에 딱딱한 글이 얹히면 읽히지 않는다. 대시보드나 표 위주의 산출물처럼 읽을 문장이 거의 없는 경우에는 이 스킬만으로 충분하다.

## 색 토큰

라이트: --bg #FFFFFF / --surface #FFFFFF / --surface-2 #F7F9FC / --ink #333333 / --ink-soft #5A6472 / --head #001C58(PACIFIC Blue) / --line #E6EAF0 / --accent #1F5795(AMORE Blue) / --accent-soft #F7FBFF / --amber #B07C00 / --amber-soft #FFF4D6 / --th-bg #001C58 / --th-ink #FFFFFF

다크(그레이): --bg #161618 / --surface #1E1E21 / --surface-2 #252529 / --ink #E8E8EA / --ink-soft #A6A6AD / --head #F0F0F2 / --line #34343A / --accent #82AEDE(밝힌 AMORE Blue) / --accent-soft #212831 / --amber #D9B15C / --amber-soft #2E2817 / --th-bg #26262B / --th-ink #E8E8EA

용법: AMORE Blue = 강조(레일·라벨·링크·핵심 콜아웃), PACIFIC Blue = 구조(헤드라인·표 헤더). 다크에서 브랜드 블루는 배경이 아니라 강조색으로만.

## 타이포그래피

- **기본**: Heading·Body 모두 "IBM Plex Sans KR"(wght 400;500;600;700), Mono는 한·영 모두 "Nanum Gothic Coding"(400;700).
- **아리따 요청 시에만**: `<html data-font="arita">` 한 줄로 아리따 돋움 + 좁힌 자간(본문 -0.04em, 헤딩 -0.06em)으로 바뀐다. Mono 라벨은 그대로다.
- 슬라이드 HTML은 문서형과 별개로 아리따 돋움을 기본으로 쓰며 `amorepacific-presentation` 스킬이 맡는다.
- CDN 로드는 Google Fonts `@import`다. 아티팩트는 `<head>`에 손댈 수 없으므로 `<style>` 첫 줄 `@import`로 로드한다.
- H1 clamp(28~40px)/700, H2 24px/700, H3 16.5px/600, 본문 17px(모바일 700px 이하 15px)/line-height 1.75. 큰 모니터에서 16px은 작아 보인다.
- 본문 줄 폭은 `ch`가 아니라 **`em`으로 40em**(17px에서 680px, 한글 약 40자). `ch`는 숫자 글리프 폭 기준이라 한글 줄이 34자 안팎으로 짧아진다. 컨테이너는 max-width 780px.
- **헤딩과 한글 표 셀에 `word-break: keep-all`** (+ `overflow-wrap: break-word`). 없으면 한글 제목이 단어 중간에서 잘린다 — 서체를 바꾼 뒤 특히 눈에 띈다. 숫자 정렬 열은 `font-variant-numeric: tabular-nums`.
- 라벨·eyebrow는 mono 스택 + uppercase + letter-spacing(+0.08~0.14em), 문서당 1~2종만.

## 컴포넌트

- 카드: white surface + 1px --line 보더 + radius 6px. **섀도우 금지** (얇은 선 + 여백이 정체성).
- 표: `.tbl-wrap`(overflow-x:auto) 래퍼 필수 — 페이지 가로 스크롤 금지. 헤더는 --th-bg 배경 + --th-ink + mono 스택.
- **수치 표는 내용에 맞게 조밀하게 구성한다.** 짧은 ID·수치 위주 표는 `.tbl-wrap.table-compact`로 폭을 내용에 맞추고 불필요한 전체 폭 확장과 큰 열 간격을 피한다. 셀 패딩은 8px 14px을 기본으로 한다. 긴 설명·요약이 있는 표는 가용 폭을 활용한다.
- **열마다 헤더와 본문의 정렬 기준을 맞춘다.** 텍스트 열은 좌측, 숫자 열은 헤더·값 모두 우측 정렬한다. 수치 열의 `th`와 `td`에 `.numeric`을 붙이고 `tabular-nums`를 사용한다. 숫자의 소수 자릿수는 같은 지표끼리 통일한다. 수치 표에는 얇은 `--line` 세로 구분선을 기본으로 두어 열 경계를 드러낸다. 코드·수치의 자간은 `normal`로 유지한다.
- 콜아웃: `.note`(amber 좌측 3px 바, 주의·전제) / `.key`(accent 좌측 3px 바, 핵심 메시지).
- 순차 레일(좌측 3px accent 보더): 연차·단계 등 실제 순서가 있는 내용에만.
- 테마 토글: eyebrow와 같은 줄(`.topbar` flex, space-between)에 놓는 pill 버튼. mono 스택 + 1px --line 보더 + radius 999px, accent 도트 하나. hover에서 보더·글자를 --accent로.
- 섹션 간격 56~64px, margin-top으로 통일. 형제 요소는 flex/grid + gap.

## 테마 토글 스크립트 (그대로 인라인)

```html
<script>
(function () {
  var KEY = 'ap-doc-theme';
  var ORDER = ['system', 'light', 'dark'];
  var LABEL = { system: '시스템', light: '라이트', dark: '다크' };
  var root = document.documentElement;
  var btn = document.getElementById('theme-toggle');
  var label = document.getElementById('theme-label');

  function read() {
    try { var v = localStorage.getItem(KEY); return ORDER.indexOf(v) > -1 ? v : 'system'; }
    catch (e) { return 'system'; }
  }
  function apply(mode) {
    if (mode === 'system') root.removeAttribute('data-theme');
    else root.setAttribute('data-theme', mode);
    label.textContent = LABEL[mode];
    btn.setAttribute('aria-label', '테마 — 현재 ' + LABEL[mode] + '. 눌러서 전환');
  }

  var current = read();
  apply(current);

  btn.addEventListener('click', function () {
    current = ORDER[(ORDER.indexOf(current) + 1) % ORDER.length];
    apply(current);
    try { localStorage.setItem(KEY, current); } catch (e) {}
  });
})();
</script>
```

`시스템`에서 `data-theme`를 지우는 것이 핵심이다. 속성이 없어야 `prefers-color-scheme`가 다시 살아난다.

## 직접 수정 모드 (그대로 인라인)

문서를 열어 놓고 글자를 바로 고칠 수 있게 한다. 동봉된 `edit_mode.js`의 내용을 `<script>`로 테마 토글 스크립트 바로 아래에 그대로 인라인하면 된다(`base.css`의 `#editbar` 스타일 포함). 문서 우하단에 `✎ 편집` 버튼이 생기고, 켜면 글자 있는 요소를 클릭해서 고칠 수 있다. `수정본 저장`(또는 Ctrl/Cmd+S)을 누르면 `<파일명>_edited.html`이 내려받아진다. 원본은 건드리지 않는다.

- 글자 고치기 전용이다. 문단·항목·표 행을 늘리거나 줄이는 일은 Claude에게 맡긴다고 사용자에게 한 줄로 알린다.
- 붙여넣기는 서식 없이 글자만 들어간다. Enter는 줄바꿈(`<br>`)이다.
- 브라우저로 직접 열었을 때만 동작한다. OneDrive·Teams 뷰어와 일부 아티팩트 화면은 스크립트나 다운로드를 막는다.
- 저장본에는 편집 버튼과 편집용 속성이 남지 않는다. 테마 선택(`data-theme`)도 굳히지 않는다.

## 서체 — 파일 형식으로 나눈다

HTML 문서는 어디로 공유하든 IBM Plex Sans KR(Google Fonts `@import`)이다. 슬라이드는 아리따 돋움이고 `amorepacific-presentation` 스킬이 맡는다. 사내 공유 여부를 묻지 않는다.

주의할 점:
- OneDrive·Teams 웹 뷰어는 외부 CDN을 막는다. 그 뷰어로 열면 Plex 대신 대체 서체가 보인다. 로컬 파일로 열면 문제없다.
- 같은 뷰어는 사용자 스크립트도 기본 차단하므로 테마 토글이 안 돌 수 있다. 이때는 한 줄로 알린다.
- Mac Finder 미리보기(Quick Look)는 스크립트와 일부 CSS가 제한될 수 있다. 문서형은 단일 열이라 대체로 문제없다.
- 문서에 아리따를 써 달라는 요청이 있을 때만 `<html lang="ko" data-font="arita">`로 바꾼다. 폰트 파일은 만들거나 임베드하지 않는다. 아리따는 사내 PC에만 있어 사외 전달 파일에는 쓰지 않는다.
- 대체 서체 없이 Plex를 그대로 보여 줘야 할 때만 `embed_fonts.py`로 base64 임베드한다(사용자가 요청할 때만).

```bash
python3 embed_fonts.py doc.html -o doc_embed.html      # 기본 = fixed (+약 1.0MB)
python3 embed_fonts.py doc.html --mode doc             # 용량이 걸릴 때만 (+약 0.25MB)
```

## 이미지가 많은 인터랙티브 보고서 (2026-11 EP 보고서에서 발견한 결점)

표 칸이나 점을 누르면 그림이 열리는 보고서를 만들며 확인한 규칙이다.

1. **폭은 두 단으로 둔다.** 본문 컬럼 780px(줄 폭 40em), 표·figure 같은 넓은 블록은 `width: min(1000px, 100vw - 48px)`를 가운데 정렬한다. 1120px 이상으로 펼치면 본문과 어긋나 보이고, 뷰포트에 따라 들쭉날쭉해진다. 이미지가 담기는 카드도 같은 상한을 쓰고, 뷰포트가 더 넓어도 넘기지 않는다.
2. **줄 폭은 `em`으로 정한다.** `max-width: 68ch`는 한글에서 줄이 34자로 짧다. 40em을 쓴다.
3. **보는 기기를 확인한다.** 4K 모니터(2560×1440 렌더링, 창 2/3 = 뷰포트 약 1700px), Windows FHD(1536〜1920px), iPhone Pro Max 세로(약 440px) 세 가지에서 열어 본다. 본문은 17px, 모바일은 15px.
4. **모바일.** 좌우 gutter 16px, 표는 `.tbl-wrap` 안에서만 가로 스크롤(페이지 가로 스크롤 금지), SVG 산점도는 `viewBox`로 줄이되 클릭 영역(투명 `.hit` 원)은 화면 기준 지름 40px 이상이 되게 키운다, 옆 패널은 전체 폭 시트로 열고 닫기 버튼을 크게 한다.
5. **이미지는 상대 링크.** 문서 구조를 그대로 복사해 공유하는 환경이면 `data:` 인라인 대신 `assets/<주제>/`를 상대 경로로 건다. 링크 대상은 반드시 문서 폴더 안에 둔다(밖에 있으면 사본에서 깨진다). 같은 그림은 파일 하나를 여러 곳에서 참조한다.
6. **인터랙션 데이터는 `<script>` 상수.** 더블클릭으로 `file://`을 열면 `fetch`가 막힌다.
7. **용어.** 과학 용어는 원어(pore, replica, snapshot, threshold)를 쓰고 "무공", "시트", "한계 전기장" 같은 번역어는 피한다. 판정과 무관한 실행 호스트 같은 열은 표에 넣지 않는다.
8. **제목 아래 lede에는 핵심만.** 보정 이력처럼 중요도가 낮은 단서는 끝 절로 보낸다.

## 산출·검수

- 단일 self-contained HTML로 전달. 서체는 HTML 문서이면 Plex(Google Fonts)이고, 아리따는 요청이 있을 때만 `data-font="arita"`로 쓴다("서체" 절). CDN 로드는 @import보다 `<link>` 우선.
- 파일명: `<주제>_<문서성격>.html`, 소문자+언더스코어.
- 게시 전 체크: ① 라이트/다크 양쪽에서 모든 색이 토큰으로 해석되는가 ② 다크에 네이비·유채색 배경이 없는가 ③ mono 영역의 한·영이 Nanum Gothic Coding으로 표시되는가 ④ 표가 페이지 가로 스크롤을 만들지 않고 수치 열의 헤더·값 정렬 및 표 밀도가 적절한가 ⑤ 헤딩이 의도한 서체(기본 Plex) + --head 적용됐는가 ⑥ 테마 전환 버튼이 3단 순환하고 새로고침 후에도 선택이 유지되는가 ⑦ 한글 헤딩이 단어 중간에서 잘리지 않는가 ⑧ 직접 수정 모드: `✎ 편집` → 글자 수정 → `수정본 저장`이 되고, 저장본에 `contenteditable`·`#editbar`가 남지 않는가 ⑨ 1000px 상한 폭, 모바일(약 440px) 가로 스크롤 없음, 본문 줄이 한글 40자 안팎인가.

<!-- sync-test 2026-10-19: claude.ai 마켓플레이스 반영 시점 확인용, 확인 후 제거 -->
