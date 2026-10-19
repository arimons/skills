---
name: html-document-design
description: 박창현의 개인 HTML 문서 디자인 가이드. HTML 문서·보고서·기획서·가이드·아티팩트를 만들거나 수정할 때 항상 적용. 라이트 모드 기본 + 기기 추종 그레이 다크모드 + 테마 전환 버튼, 기본 서체 IBM Plex Sans KR(사내 공유용은 아리따 돋움), AMORE/PACIFIC Blue 토큰, 한·영 고정폭 Nanum Gothic Coding 통일 및 수치 표 정렬 규칙 포함. Use when creating or editing any HTML document, report, or artifact.
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
5. **서체는 IBM Plex Sans KR이 기본**, 사내 공유(OneDrive·Teams)용은 아리따 돋움이다("산출물 분기" 절). 헤딩은 h1·h2가 weight 700 + letter-spacing -0.02em, h3는 600 + -0.01em, 색은 --head. 위계는 3단계 이하. (Plex는 700이 최대 굵기다. 아리따일 때는 자간을 `data-font="arita"`가 함께 조인다.)
6. **이미지는 항상 문서 안에 넣는다.** 이미지·아이콘은 `data:` URI(base64)로 인라인하고, 다이어그램은 이미지 대신 인라인 SVG를 우선한다. **폰트는 파일에 담지 않는다.** 기본은 Google Fonts(Plex), 사내 공유용은 전사 PC에 설치된 아리따 돋움을 이름으로 부른다(아래 "산출물 분기" 절).
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
- **사내 공유용**: `<html data-font="arita">` 한 줄로 아리따 돋움 + 좁힌 자간(본문 -0.04em, 헤딩 -0.06em)으로 바뀐다. Mono 라벨은 그대로다.
- 슬라이드 HTML은 문서형과 별개로 아리따 돋움을 기본으로 쓰며 `amorepacific-presentation` 스킬이 맡는다.
- CDN 로드는 Google Fonts `@import`다. 아티팩트는 `<head>`에 손댈 수 없으므로 `<style>` 첫 줄 `@import`로 로드한다.
- H1 clamp(28~40px)/700, H2 24px/700, H3 16.5px/600, 본문 15~16px/line-height 1.75.
- 본문 텍스트 폭 68ch 이내, 컨테이너 max-width 760~800px.
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

## 산출물 분기 — 사내 공유(OneDrive·Teams)인가

폰트를 받아오는 주체는 파일이 놓인 곳이 아니라 **문서를 여는 사람의 브라우저**다. Teams·OneDrive 뷰어는 외부 CDN(Google Fonts·jsDelivr)을 막는다(2026-10-13 테스트). 반면 아리따 돋움은 전사 PC에 자동 설치돼 있어 네트워크가 필요 없다. 그래서 사내 공유용만 아리따로 간다. 이미지는 어느 경우든 항상 `data:` URI다.

| | Claude 아티팩트 | 파일 — **기본** (내 PC 등) | 파일 — **사내 공유** (OneDrive 링크·Teams) |
|---|---|---|---|
| 서체 | IBM Plex Sans KR | IBM Plex Sans KR | **아리따 돋움** (`data-font="arita"`) |
| 로드 | Google Fonts `@import` | Google Fonts `@import` | 설치된 폰트 이름으로 호출 (파일에 담지 않음) |
| 자간 | 기본 | 기본 | 본문 -0.04em, 헤딩 -0.06em |
| 이유 | 아티팩트 CSP가 Google Fonts만 허용 | 열 때 온라인이면 받아진다 | CDN이 막혀도 전사 PC에는 이미 설치돼 있다 |

### 파일로 낼 때 먼저 묻는다

파일(.html)로 전달하기로 정해지면, 공유 경로가 대화에서 아직 드러나지 않았을 때 **한 번만** 묻는다: *"사내 OneDrive나 Teams로 공유하실 건가요?"* 사용자가 이미 경로를 말했으면 묻지 않고 바로 분기한다. 답이 없거나 사용자가 자리에 없으면 **기본(Plex)으로 간다.** 아티팩트로 게시할 때는 묻지 않고 Plex다.

사내 공유로 정해지면 `<html lang="ko" data-font="arita">`로 바꾸는 것이 전부다. 폰트 파일을 만들거나 임베드하지 않는다.

주의할 점:
- 아리따는 사내 PC에만 있다. 사외로 나가는 파일(협력사 전달 등)에는 쓰지 않고 Plex로 둔다. 설치되지 않은 PC에서는 Pretendard → 맑은 고딕 순으로 대체돼 모양이 달라진다.
- OneDrive·SharePoint 링크 뷰어는 사용자 스크립트를 기본 차단하므로 테마 토글이 안 돌 수 있다. 이때는 한 줄로 알린다.
- Mac Finder 미리보기(Quick Look)는 스크립트와 일부 CSS가 제한될 수 있다. 문서형은 단일 열이라 대체로 문제없다.

### 사내 공유에서도 Plex를 꼭 유지해야 할 때 (예외)

아리따 대신 Plex를 그대로 보여 줘야 하는 경우에 한해 `embed_fonts.py`로 base64 임베드한다. 기본 흐름이 아니므로 사용자가 요청할 때만 쓴다.

```bash
python3 embed_fonts.py doc.html -o doc_embed.html      # 기본 = fixed (+약 1.0MB)
python3 embed_fonts.py doc.html --mode doc             # 용량이 걸릴 때만 (+약 0.25MB)
```

전달 직전, 본문이 확정된 뒤에 에이전트가 직접 돌리고 임베드본 하나만 낸다. `--family pretendard`는 Pretendard 문서용이다. 스킬 파일을 읽을 때 base64 덩어리를 컨텍스트에 올리지 않는다.

## 산출·검수

- 단일 self-contained HTML로 전달. 서체는 공유 경로로 분기한다(위 절): 사내 공유면 `data-font="arita"`, 그 외는 Plex(Google Fonts). CDN 로드는 @import보다 `<link>` 우선.
- 파일명: `<주제>_<문서성격>.html`, 소문자+언더스코어.
- 게시 전 체크: ① 라이트/다크 양쪽에서 모든 색이 토큰으로 해석되는가 ② 다크에 네이비·유채색 배경이 없는가 ③ mono 영역의 한·영이 Nanum Gothic Coding으로 표시되는가 ④ 표가 페이지 가로 스크롤을 만들지 않고 수치 열의 헤더·값 정렬 및 표 밀도가 적절한가 ⑤ 헤딩이 의도한 서체(기본 Plex, 사내 공유 아리따) + --head 적용됐는가 ⑥ 테마 전환 버튼이 3단 순환하고 새로고침 후에도 선택이 유지되는가 ⑦ 한글 헤딩이 단어 중간에서 잘리지 않는가 ⑧ 사내 공유본이면 외부 요청이 0건인가 — Google Fonts `@import`가 남아 있어도 서체는 아리따로 잡히지만, 막힌 요청이 생기지 않도록 이미지가 모두 인라인인지 확인.

<!-- sync-test 2026-10-19: claude.ai 마켓플레이스 반영 시점 확인용, 확인 후 제거 -->
