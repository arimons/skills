---
name: html-document-design
description: 박창현의 개인 HTML 문서 디자인 가이드. HTML 문서·보고서·기획서·가이드·아티팩트를 만들거나 수정할 때 항상 적용. 라이트 모드 기본 + 기기 추종 그레이 다크모드 + 테마 전환 버튼, 헤딩 IBM Plex Sans KR, AMORE/PACIFIC Blue 토큰, 한글 mono fallback(Nanum Gothic Coding) 규칙 포함. Use when creating or editing any HTML document, report, or artifact.
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
5. **헤딩은 IBM Plex Sans KR** — h1·h2는 weight 700 + letter-spacing -0.02em, h3는 600 + -0.01em, 색은 --head. 위계는 3단계 이하. (이 서체는 700이 최대 굵기다. 더 굵은 헤딩이 필요한 문서에 한해 Noto Sans KR 800을 쓴다.)
6. **이미지는 항상 문서 안에 넣는다.** 이미지·아이콘은 `data:` URI(base64)로 인라인하고, 다이어그램은 이미지 대신 인라인 SVG를 우선한다. **폰트는 공유 경로에 따라 갈린다** — OneDrive 링크·Teams로 파일을 공유할 때만 base64 `@font-face`로 임베드하고, 그 외에는 CDN 링크를 그대로 둔다(아래 "산출물 분기" 절).
7. **monospace 영역의 한글 fallback**: 영문 mono 폰트(IBM Plex Mono 등)는 한글 글리프가 없어 굴림으로 떨어진다. 반드시 `"IBM Plex Mono", "Nanum Gothic Coding", "D2Coding", monospace` 겹침 스택을 사용해 한글이 나눔 코딩 계열로 렌더되게 한다. Google Fonts 환경에서는 Nanum Gothic Coding을 함께 로드한다.

## 글은 어떻게 쓰나

이 스킬은 **어떻게 보이는가**만 다룬다. 문장을 어떤 목소리로 쓸지는 `manual-voice` 스킬에 있다.

설명하는 성격의 문서 — 매뉴얼·가이드·튜토리얼·교재 — 를 HTML로 만들 때는 **`manual-voice`가 설치되어 있으면 두 스킬을 함께 적용한다. 설치되지 않았다면 이 스킬을 적용하고 사용자가 요청한 문체를 따른다. `manual-voice`는 이 묶음에 포함되지 않은 선택 의존성이다.** 잘 만든 판에 딱딱한 글이 얹히면 읽히지 않는다. 대시보드나 표 위주의 산출물처럼 읽을 문장이 거의 없는 경우에는 이 스킬만으로 충분하다.

## 색 토큰

라이트: --bg #FFFFFF / --surface #FFFFFF / --surface-2 #F7F9FC / --ink #333333 / --ink-soft #5A6472 / --head #001C58(PACIFIC Blue) / --line #E6EAF0 / --accent #1F5795(AMORE Blue) / --accent-soft #F7FBFF / --amber #B07C00 / --amber-soft #FFF4D6 / --th-bg #001C58 / --th-ink #FFFFFF

다크(그레이): --bg #161618 / --surface #1E1E21 / --surface-2 #252529 / --ink #E8E8EA / --ink-soft #A6A6AD / --head #F0F0F2 / --line #34343A / --accent #82AEDE(밝힌 AMORE Blue) / --accent-soft #212831 / --amber #D9B15C / --amber-soft #2E2817 / --th-bg #26262B / --th-ink #E8E8EA

용법: AMORE Blue = 강조(레일·라벨·링크·핵심 콜아웃), PACIFIC Blue = 구조(헤드라인·표 헤더). 다크에서 브랜드 블루는 배경이 아니라 강조색으로만.

## 타이포그래피

- 문서형 HTML의 서체는 어디서 열리든 같다: Heading·Body 모두 "IBM Plex Sans KR"(wght 400;500;600;700), Mono "IBM Plex Mono"+"Nanum Gothic Coding". 공유 경로에 따라 갈리는 건 로드 방식뿐이다. (Pretendard는 슬라이드 HTML 전용이며 `amorepacific-presentation` 스킬이 맡는다.)
- CDN 로드는 Google Fonts `@import`다. 아티팩트는 `<head>`에 손댈 수 없으므로 `<style>` 첫 줄 `@import`로 로드한다.
- H1 clamp(28~40px)/700, H2 24px/700, H3 16.5px/600, 본문 15~16px/line-height 1.75.
- 본문 텍스트 폭 68ch 이내, 컨테이너 max-width 760~800px.
- **헤딩과 한글 표 셀에 `word-break: keep-all`** (+ `overflow-wrap: break-word`). 없으면 한글 제목이 단어 중간에서 잘린다 — 임베드 폰트로 바꾼 뒤 특히 눈에 띈다. 숫자 정렬 열은 `font-variant-numeric: tabular-nums`.
- 라벨·eyebrow는 mono 스택 + uppercase + letter-spacing(+0.08~0.14em), 문서당 1~2종만.

## 컴포넌트

- 카드: white surface + 1px --line 보더 + radius 6px. **섀도우 금지** (얇은 선 + 여백이 정체성).
- 표: `.tbl-wrap`(overflow-x:auto) 래퍼 필수 — 페이지 가로 스크롤 금지. 헤더는 --th-bg 배경 + --th-ink + mono 스택.
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

## 산출물 분기 — OneDrive·Teams로 공유하는가

폰트를 받아오는 주체는 파일이 놓인 곳이 아니라 **문서를 여는 사람의 브라우저**다. Teams·OneDrive 뷰어는 외부 CDN을 막기 때문에, 그 경로로 나가는 파일만 폰트를 문서 안에 실어야 한다. 이미지는 어느 경우든 항상 `data:` URI다.

| | Claude 아티팩트 | 파일 — 그 외 (내 PC 등) | 파일 — **OneDrive 링크·Teams 공유** |
|---|---|---|---|
| 폰트 | Google Fonts `@import` | CDN `@import` 그대로 | **base64 `@font-face` 임베드** |
| 이유 | 아티팩트 CSP가 Google Fonts만 허용 | 열 때 온라인이면 CDN에서 받아진다 | 뷰어가 외부 요청을 막아 맑은 고딕으로 떨어진다 |
| 누가 | 그대로 게시 | 그대로 전달 | **에이전트가 `embed_fonts.py`를 돌려서 낸다** |

### 파일로 낼 때 먼저 묻는다

파일(.html)로 전달하기로 정해지면, 공유 경로가 대화에서 아직 드러나지 않았을 때 **한 번만** 묻는다: *"OneDrive나 Teams로 공유하실 건가요?"* 사용자가 이미 경로를 말했으면 묻지 않고 바로 분기한다. 답이 없거나 사용자가 자리에 없으면 **임베드로 간다** — 임베드는 어디서 열어도 안전하고, CDN 판은 공유 경로에서 깨질 수 있기 때문이다.

### 임베드로 갈 때

**이건 사용자가 하는 일이 아니다.** 전달 직전에 에이전트가 스크립트를 돌리고 **임베드본 하나만** 낸다. CDN 판과 임베드판을 둘 다 주지 않는다. 사용자에게 "공유하실 땐 이 명령을 돌리세요"라고 안내하는 것은 이 규칙을 지킨 것이 아니다.

OneDrive·SharePoint 링크로 공유할 때는 뷰어가 샌드박스 도메인에서 열며 외부 리소스를 막고, 사용자 스크립트도 기본 차단이라 테마 토글이 안 돌 수 있다. 이 경우 임베드본이어도 토글은 동작하지 않을 수 있다고 한 줄로 알린다.

## 폰트 임베드 (`embed_fonts.py`)

**OneDrive·Teams로 공유할 때만** 돌린다. 동봉된 스크립트가 외부 `@import`/`<link>`를 지우고 그 자리에 base64 `@font-face`를 넣는다. 결과물은 네트워크 없이도 의도한 서체로 렌더된다.

```bash
python3 embed_fonts.py doc.html -o doc_embed.html      # 기본 = fixed
python3 embed_fonts.py doc.html --mode doc             # 메일 첨부 등 용량이 걸릴 때만
python3 embed_fonts.py deck.html --family pretendard   # 슬라이드 HTML (amorepacific-presentation 에서 호출)
```

전달 직전, 본문이 확정된 뒤에 돌린다. 문서를 다시 고쳤으면 다시 돌린 판으로 교체한다.

| 모드 | 담기는 글자 | 문서 증가분 | 언제 |
|---|---|---|---|
| `fixed` *(기본)* | KS X 1001 한글 2350자 + 라틴 + 구두점 | 약 +1.0MB | **거의 항상.** 나중에 손으로 문장을 고쳐도 안 깨진다 |
| `doc` | 문서에 실제로 등장한 글자만 | 약 +0.25MB | 메일 첨부처럼 용량이 걸릴 때만 |

`doc` 모드의 함정: 이후 새 한글을 손으로 넣으면 **그 글자만** 대체 서체로 떨어진다. 문서를 다시 고쳤으면 스크립트를 다시 돌린다.

담기는 서체는 `--family`로 고른다. 기본 `plex`는 IBM Plex Sans KR 400·500·600·700, IBM Plex Mono 400·500, Nanum Gothic Coding 400·700(문서 +약 1.0MB). `pretendard`는 Pretendard 400·500·600·700·800(문서 +약 0.9MB)이다. 폰트 원본은 최초 1회 npm(`@fontsource/*`, `pretendard`)에서 받아 작업 공간의 `~/.cache/ap-doc-fonts`에 캐시한다. 필요: `fonttools`, `brotli`, node.

> 스킬 파일을 읽을 때 base64 덩어리를 컨텍스트에 올리지 않는다. 임베드는 **스크립트를 실행해서** 하고, 결과 파일을 열어 확인하지 않는다.

## 산출·검수

- 단일 self-contained HTML로 전달. 폰트는 공유 경로로 분기한다(위 절): OneDrive·Teams 공유면 임베드본, 그 외는 CDN. CDN 로드는 @import보다 `<link>` 우선.
- 파일명: `<주제>_<문서성격>.html`, 소문자+언더스코어.
- 게시 전 체크: ① 라이트/다크 양쪽에서 모든 색이 토큰으로 해석되는가 ② 다크에 네이비·유채색 배경이 없는가 ③ mono 영역 한글이 굴림으로 떨어지지 않는가 ④ 표가 페이지 가로 스크롤을 만들지 않는가 ⑤ 헤딩이 IBM Plex Sans KR + --head 적용됐는가 ⑥ 테마 전환 버튼이 3단 순환하고 새로고침 후에도 선택이 유지되는가 ⑦ 한글 헤딩이 단어 중간에서 잘리지 않는가 ⑧ OneDrive·Teams 공유본이면 외부 요청이 0건인가 — 폰트·이미지가 모두 인라인인지 확인. 그 외 파일은 이미지만 인라인이면 된다.
