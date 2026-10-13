# AMOREPACIFIC Presentation Skill

```yaml
Version: 2.2
Owner: 박창현 / 스킨케어2 Lab
Base Template: BY27 템플릿(PPT).pptx
Scope: PPT, HTML Slideshow, Marp, Reveal.js, PDF Export
Default Deliverable: Self-contained single HTML (Base64 embedded assets)
Last Updated: 2026-08-31
```

> **이 문서의 역할**
> AI(Copilot / Claude / GPT)에게 "이 presentation_skill.md 기준으로 발표자료 만들어줘"라고 지시했을 때,
> 별도 설명 없이 AMOREPACIFIC 사내 발표자료를 생성하도록 하는 단일 Skill 명세서입니다.

---

## 0. Quick Reference (AI 생성 시 최소 준수 사항)

```yaml
Canvas: 1920 x 1080 px (16:9)
Background: "#FFFFFF"
Font: Pretendard
Title Color: "#001C58"
Accent Color: "#1F5795"
Body Color: "#333333"
Assets: cover header + content header + footer left + footer right (Base64 embed)
Output: 단일 .html 파일 1개
Rule: 한 슬라이드 = 하나의 메시지
```

---

## 1. Output Policy (최우선 규칙)

### 1.1 Default Delivery

```yaml
Default Format: Self-contained HTML
Asset Handling: Embed as Base64 data URI
Delivery: single .html file
External Asset Folder: NOT required for delivery
ZIP Packaging: avoid unless explicitly requested
```

### 1.2 왜 Base64 내장인가

```yaml
Reason:
  - 수신자가 압축 해제 없이 더블클릭으로 실행
  - Teams / SharePoint / OneDrive / 메일 첨부 시 경로 깨짐 없음
  - assets 폴더 누락으로 로고·푸터가 사라지는 사고 방지
  - AI 생성 결과물 보관 및 버전 관리 단순화
Trade-off:
  - 파일 크기 증가 (현 자산 기준 약 +50KB, 무시 가능 수준)
```

### 1.3 Source vs Deliverable 분리

```yaml
Source Package (영구 보관, 참조용):
  design.md
  assets/          # 원본 PNG 유지
  templates/       # 원본 PPTX 유지
  samples/         # 렌더링 참고 이미지

Deliverable (배포용):
  <topic>.html     # Base64 내장 단일 파일
```

### 1.4 Exception — 외부 asset 폴더를 쓰는 경우

```yaml
Use external assets only if:
  - 단일 이미지가 1MB 초과
  - 동영상 / 오디오 포함
  - 고해상도 사진이 5장 이상
  - 이미지가 배포 후에도 개별 교체되어야 함
```

### 1.5 Base64 Embed 구현 규칙

```yaml
Method:
  1. assets/ 폴더의 PNG를 읽는다
  2. data:image/png;base64,... 형태로 변환한다
  3. <img src="data:image/png;base64,..."> 로 직접 삽입한다
  4. 외부 파일 참조(src="assets/...")를 남기지 않는다

Verification:
  - HTML 파일 단독으로 브라우저 실행 시 로고/푸터가 보여야 함
  - 파일 내 "assets/" 문자열이 남아있으면 실패
```

---

## 2. Brand Assets

### 2.1 Asset Manifest

| Asset | 파일명 | 용도 | 배치 |
|---|---|---|---|
| Cover Header | `cover_header_amorepacific.png` | 표지 로고 (AMOREPACIFIC 워드마크, 대형) | 표지 좌상단 |
| Content Header | `content_header_amorepacific.png` | 본문 로고 (AMOREPACIFIC 워드마크, 소형 · BY27 신규) | 본문 슬라이드 우상단 |
| Footer Left | `footer_left_create_new_beauty.png` | Create New Beauty | 좌하단 |
| Footer Right | `footer_right_beauty_in_motion.png` | Beauty in Motion (BY27 슬로건 · 구 footer_right_by26_statement.png 대체) | 우하단 |

### 2.2 Placement (1920 × 1080 px 기준)

```yaml
Cover Header:
  left: 160 px
  top: 108 px
  width: 331 px
  height: 32 px

Content Header:              # BY27 신규 — 본문 슬라이드 전용
  right: 39 px
  top: 74 px
  width: 231 px
  height: 22 px

Footer Left:
  left: 32 px
  bottom: 4 px                # BY27: 로고 세로폭 확대(53px→80px)로 하단 여백 축소, 실사용 시 육안 확인 권장
  width: 283 px
  height: 52 px

Footer Right:
  right: 12 px                 # BY27: 우측 여백이 158px → 12px로 크게 축소됨(템플릿 실측값), 콘텐츠와 겹치지 않는지 확인
  bottom: 4 px
  width: 283 px
  height: 52 px
```

### 2.3 Placement (PPT / inch 기준)

```yaml
Slide: 13.333 in x 7.5 in
Cover Header:   x 1.114  / y 0.748 / w 2.299 / h 0.221
Content Header: x 11.462 / y 0.512 / w 1.603 / h 0.154   # BY27 신규
Footer Left:    x 0.219  / y 7.109 / w 1.965 / h 0.362
Footer Right:   x 11.285 / y 7.109 / w 1.965 / h 0.362
Conversion: 1 in = 144 px
```

### 2.4 Asset Rules

```yaml
Do:
  - 원본 비율 유지
  - 고정 좌표 배치
  - 모든 콘텐츠 슬라이드에 footer 적용

Never:
  - AMOREPACIFIC 로고를 텍스트로 재현
  - 푸터 문구를 직접 타이핑으로 대체
  - 로고/푸터 색상 변경 또는 비율 왜곡
  - 표지 헤더(Cover Header)를 본문 슬라이드에 반복 사용
  - Content Header를 Cover Header 대신 사용(또는 그 반대) — 두 자산은 크기·용도가 다름
```

---

## 3. Color System

### 3.1 Corporate CI Colors

```yaml
AMORE Blue:
  HEX: "#1F5795"
  RGB: "31, 87, 149"
  CMYK: "C90 M69 Y22 K0"
  Role: 1강조색 / Primary Accent
  Use:
    - 핵심 강조, 활성 요소
    - 프로세스 화살표
    - Agent Layer 등 "변화가 일어나는 지점"
    - 강조 카드 좌측 바

PACIFIC Blue:
  HEX: "#001C58"
  RGB: "0, 28, 88"
  CMYK: "C100 M100 Y58 K18"
  Role: 2강조색 / Structural Navy
  Use:
    - 슬라이드 헤드라인
    - 표 헤더
    - 아키텍처 백본
    - Executive Summary 블록

Black:
  HEX: "#000000"
  CMYK: "C0 M0 Y0 K100"
  Use: 슬라이드 타이틀, 강한 레이블

Gray:
  HEX: "#7D7D7D"
  RGB: "125, 125, 125"
  CMYK: "C59 M50 Y47 K0"
  Use: 보조 텍스트, 캡션, 페이지 번호, 비활성 요소

White:
  HEX: "#FFFFFF"
  CMYK: "C0 M0 Y0 K0"
  Use: 배경, 카드 표면
```

### 3.2 Extended Neutrals

```yaml
Off White:   "#F7F9FC"   # 섹션 배경, 강조 박스 배경
Light Gray:  "#E6EAF0"   # 카드 보더, 구분선, 표 라인
Mid Gray:    "#B8C0CC"   # 비활성 아이콘
Dark Gray:   "#333333"   # 본문 기본 텍스트
Tint Blue:   "#F7FBFF"   # Action/강조 영역 배경
Pale Blue:   "#B8CDE6"   # 보조 차트 계열
```

### 3.3 Semantic Colors (보조 강조색)

```yaml
Alert Red:      "#D9291C"   # 리스크, 병목, 문제 제기
Soft Red:       "#FDECEA"   # 문제 카드 배경
Success Green:  "#1C8C5A"   # 완료, 승인, 개선
Soft Green:     "#EAF6F0"   # 성과 카드 배경
Amber:          "#F2A900"   # 대기, 의사결정 필요
Soft Amber:     "#FFF4D6"   # 주의 카드 배경
```

### 3.4 Usage Ratio & Rules

```yaml
Ratio:
  White / Neutral: 75-85%
  Text (Black/Gray): 10-15%
  AMORE Blue: 3-8%
  PACIFIC Blue: 3-8%
  Semantic: below 3%

Rules:
  - AMORE Blue는 "강조", PACIFIC Blue는 "구조"에 사용
  - Red는 진짜 리스크·문제일 때만 사용
  - 무지개 팔레트 금지
  - 그라디언트는 Blue 계열 내에서만 허용
  - 차트는 Blue 단색 계열을 기본으로 함
```

### 3.5 Contrast / Accessibility

```yaml
Minimum Contrast:
  Body text on white: 4.5:1 이상 (Dark Gray #333333 이상 어둡게)
  Large title: 3:1 이상
Forbidden:
  - Gray #7D7D7D 를 본문 장문에 사용
  - AMORE Blue 배경 위 PACIFIC Blue 텍스트
  - Light Gray 위 White 텍스트
On Dark Block:
  Background: PACIFIC Blue
  Text: White only
```

---

## 4. Typography

### 4.1 Font Policy

```yaml
Primary: Pretendard
Template Reference: Arita Dotum KR (사내 공식 폰트)
Fallback KR: Malgun Gothic
Fallback EN: Aptos, Segoe UI, Arial

Decision:
  - AI 생성물(PPT/HTML)은 Pretendard 사용
  - 브랜드 로고/슬로건은 폰트 재현 금지, 이미지 asset 사용
```

### 4.2 PPT Type Scale

| Level | Size | Weight | Color | 용도 |
|---|---|---|---|---|
| Cover Title | 34–40 pt | 800 | Black | 표지 제목 |
| Slide Title | 16–20 pt | 700 | Black | 본문 슬라이드 상단 제목 |
| Section Title | 26–32 pt | 700 | PACIFIC Blue | 섹션 구분 |
| Headline | 22–28 pt | 800 | PACIFIC Blue | 슬라이드 핵심 주장 |
| Card Title | 15–18 pt | 700 | PACIFIC Blue | 카드 제목 |
| Body | 12–15 pt | 400–500 | Dark Gray | 본문 |
| Label | 10–12 pt | 600 | AMORE Blue | 태그, 다이어그램 라벨 |
| Caption | 9–10 pt | 400 | Gray | 출처, 각주 |

### 4.3 HTML Type Scale (1920 × 1080)

```css
:root {
  --font-main: "Pretendard", "Malgun Gothic", "Segoe UI", system-ui, sans-serif;

  --cover-title: 78px;   /* weight 800, letter-spacing -0.055em */
  --slide-title: 27px;   /* weight 700 */
  --headline:    44px;   /* weight 800, PACIFIC Blue */
  --section:     38px;
  --card-title:  29px;
  --body:        24px;
  --small:       20px;
  --caption:     16px;
}
```

### 4.4 Typography Rules

```yaml
Visible Levels Per Slide: maximum 3
  1. Slide Title
  2. Block / Card Title
  3. Body

Korean Typesetting:
  letter-spacing: -0.02em ~ -0.055em (제목일수록 크게 음수)
  line-height: 1.25 ~ 1.45

Forbidden:
  - 한 슬라이드에 H1~H6 전부 사용
  - 3줄 이상 연속 문단
  - 두 가지 이상 서체 혼용
  - 본문 전체 Bold
```

---

## 5. Layout System

### 5.1 Canvas & Grid

```yaml
PPT Canvas: 13.333 in x 7.5 in (16:9)
HTML Canvas: 1920 x 1080 px
Grid: 12 columns
Base Unit: 8 px
Scaling: viewport 비율에 맞춰 transform: scale() 적용
```

### 5.2 Margins & Spacing

```yaml
Cover Left Margin: 158-160 px
Content Left/Right Margin: 115 px (본문 영역)
Slide Title: left 39 px / top 46 px
Top Rule: left 32 px / right 32 px / top 107 px
Footer Rule: left 32 px / right 32 px / bottom 70 px
Content Area: top 170 px / bottom 118 px
Card Gap: 24-28 px
Card Padding: 28-34 px
```

### 5.3 Thin Rule Style (템플릿 핵심 특징)

```yaml
Top Rule:
  color: "#111111"
  height: 1 px
  opacity: 0.4

Footer Rule:
  color: "#111111"
  height: 1 px
  opacity: 0.35

Cover Rule:
  color: "#222222"
  height: 1 px
  opacity: 0.75

Note: BY26 템플릿의 정체성은 "얇은 선 + 넓은 여백"입니다. 굵은 박스/헤비 섀도우 금지.
```

### 5.4 Layout Patterns

```yaml
Full Bleed Message:
  - 헤드라인 1개 + 근거 카드 2~3개

Two Column:
  - 45% : 55%
  - Before/After, Current/Future, 업무/기술

Three Card Row:
  - 1fr 1fr 1fr, gap 28px
  - 카드 최소 높이 270px

2x2 Matrix:
  - 업무 유형 분류, 우선순위 매핑

Horizontal Flow:
  - 3~5 단계, 좌→우, 화살표는 AMORE Blue

Layer Stack:
  - User / Agent / Tool·API / System / Data
  - 4~5 레이어 초과 금지
```

---

## 6. Component Library

### 6.1 Card

```yaml
Background: "#FFFFFF"
Border: 1px solid "#E6EAF0"
Radius: 12-18 px
Padding: 28-34 px
Shadow: none 또는 매우 약하게
```

### 6.2 Emphasis Card (핵심 메시지)

```yaml
Background: "#F7F9FC"
Border Left: 8px solid AMORE Blue
Radius: 8 px
Font: 26px / weight 600
Use: 슬라이드 하단 Key Takeaway
```

### 6.3 Active / Highlight Card

```yaml
Background: "#F7FBFF"
Border: 3px solid AMORE Blue
Use: Before/After의 After, Flow의 핵심 단계, Action 영역
```

### 6.4 Semantic Cards

```yaml
Problem Card:
  Background: Soft Red
  Border Left: 4px solid Alert Red
  Title Color: Alert Red

Success Card:
  Background: Soft Green
  Border Left: 4px solid Success Green
  Title Color: Success Green

Caution Card:
  Background: Soft Amber
  Border Left: 4px solid Amber
```

### 6.5 Badge / Chip

```yaml
Background: Off White
Text Color: AMORE Blue
Radius: 999 px
Padding: 8px 18px
Font Size: 18px / weight 700
Use: 카드 우상단 분류 라벨
```

### 6.6 Table

```yaml
Header Background: PACIFIC Blue
Header Text: White
Row Border: 1px solid Light Gray
First Column: left align, bold
Other Columns: center align
Radius: 14 px (overflow hidden)
Symbol Convention: ● 높음 / △ 부분 / - 해당없음
```

### 6.7 Circle Emphasis (역할·중심 개념)

```yaml
Size: 300 px
Background: PACIFIC Blue
Text: White, 38px, weight 800
Shadow: 0 18px 60px rgba(0,28,88,0.22)
Use: Domain Owner, Core Concept 등 중심 노드
```

---

## 7. Diagram & Chart Rules

### 7.1 Flow Diagram

```yaml
Direction: 좌 → 우
Arrow: AMORE Blue, 2-3 px, 화살표 문자는 →
Node: White background, Light Gray border
Active Node: AMORE Blue 3px border + Tint Blue background
Max Steps: 5
```

### 7.2 Layer Architecture

```yaml
Order:
  User Layer
  Agent Layer
  Tool / API Layer
  Business System Layer
  Data Layer

Color:
  Agent Layer: AMORE Blue (변화의 핵심)
  System Layer: PACIFIC Blue
  Data Layer: Gray 계열
```

### 7.3 Before / After

```yaml
Before:
  Background: "#FAFAFA"
  Title Color: "#555555"
  Tone: 중립·회색

After:
  Background: "#F7FBFF"
  Border: 3px solid AMORE Blue
  Title Color: PACIFIC Blue

Center Arrow: → , 78px, AMORE Blue, weight 800
```

### 7.4 Charts

```yaml
General:
  - 3D 차트 금지
  - 무지개 색상 금지
  - 그리드 최소화, 직접 라벨 우선

Bar:
  Primary: AMORE Blue
  Secondary: "#B8CDE6"
  Highlight: Alert Red 또는 Success Green (의미 있을 때만)
  Grid: "#E6EAF0"

Line:
  Primary: AMORE Blue
  Secondary: PACIFIC Blue
  Risk: Alert Red
  Stroke: 2.5-3 px

Donut / Pie:
  Palette: PACIFIC Blue → AMORE Blue → "#5F8FC5" → "#B8CDE6" → "#E6EAF0"
  Use: 부분-전체 관계일 때만
```

---

## 8. Slide Type Library

```yaml
01_Cover:
  Purpose: 제목, 부제, 날짜/소속, 목차
  Required: cover header + footer assets

# 02~15 모든 본문 슬라이드 공통: content header + footer assets 필수

02_Context:
  Purpose: 왜 이 주제를 지금 논의하는가

03_Current_State:
  Purpose: 현재 상태의 가치를 먼저 인정
  Note: 기존 프로젝트를 부정하지 않는 것이 설득의 핵심

04_Limitation:
  Purpose: 현재 접근의 구조적 한계
  Style: Problem Card 또는 Before/After

05_Insight:
  Purpose: 관점 전환 한 문장
  Style: 대형 텍스트 1개

06_Vision:
  Purpose: 목표 상태 (예: Knowledge → Action)

07_Architecture:
  Purpose: User → Agent → Tool/API → System → Data
  Rule: 기술 디테일은 Appendix로

08_Process_Map:
  Purpose: 실제 업무 흐름 자동화 시나리오

09_Matrix:
  Purpose: 업무를 조회/판단/실행/추적으로 분류

10_Role_Definition:
  Purpose: 제안자의 역할 정의
  Note: 리더 설득에서 가장 중요한 슬라이드

11_Pilot_Proposal:
  Purpose: 첫 실행 후보 3개 이내

12_Roadmap:
  Purpose: 3~5 Phase, 각 Phase에 목표/산출물/주체

13_Expected_Impact:
  Purpose: 시간 절감, 표준화, 온보딩, 품질

14_Decision_Request:
  Purpose: 리더에게 요청하는 의사결정 1개

15_Appendix:
  Purpose: API/MCP, 시나리오 목록, 검증 기준
```

---

## 9. AI / AX Presentation Components

### 9.1 Knowledge vs Action Frame

```yaml
Left (Knowledge Agent):
  - 검색한다
  - 요약한다
  - 근거를 제시한다
  - 판단을 보조한다
  Style: 중립 회색 톤

Right (Action Agent):
  - 등록한다
  - 생성한다
  - 갱신한다
  - 추적한다
  Style: AMORE Blue 강조

Message Rule:
  기존 플랫폼을 부정하지 말고 "다음 단계"로 위치시킬 것
```

### 9.2 Agent Card

```yaml
Fields:
  - Agent Name
  - User Input (자연어 예시)
  - Required Context (필수 정보)
  - Tool / API Call
  - Output
  - Exception Handling

Example:
  Name: 시험의뢰 Agent
  Input: "탠저린 비타C 세럼 광안정성 시험 의뢰해줘"
  Context: 제품코드, LOT, 시험 종류, 의뢰 부서
  Tool: getProduct, getLot, createTestRequest
  Output: 의뢰번호 / 일정 / 담당자
  Exception: LOT 다수 존재 시 재질문
```

### 9.3 Tool Card

```yaml
Fields:
  - Tool / API Name
  - Trigger
  - Required Parameters
  - Target System
  - Return Value
Style: Light Gray border, 아이콘은 라인 스타일
```

### 9.4 Domain Owner Role Card

```yaml
Fields:
  - 업무 프로세스 정의
  - Task Map 작성
  - 자연어 표현 수집
  - 필수값 / 예외상황 정의
  - Acceptance Test 설계
  - 사용성 검증
Position: 중심 원(PACIFIC Blue) + 주변 카드 배치
```

---

## 10. Writing & Storytelling Rules

### 10.1 Slide Title = 결론

```yaml
Rule: 제목만 순서대로 읽어도 전체 논지가 완성되어야 한다
```

Good:

```text
정보 접근성은 개선되었지만 업무 수행은 여전히 사람 중심이다
연구원의 시간은 조회보다 등록·확인·추적에서 더 많이 소모된다
```

Weak:

```text
현황 및 문제점
개선 방안
```

### 10.2 Text Budget

```yaml
Executive Slide: bullet 3-5개
Technical Slide: bullet 5-7개
Diagram Slide: 다이어그램을 반복 설명하지 말 것
Key Takeaway: 슬라이드당 1개, 하단 Emphasis Card
```

### 10.3 Tone

```yaml
Prefer:
  - 반복 입력 감소
  - 등록·추적 자동화
  - 업무 표준화
  - 신입 온보딩 보조
  - 검증 가능한 Pilot

Avoid:
  - 만능 AI / 혁신적 패러다임 전환 (단독 사용)
  - 근거 없는 정량 효과 수치
  - 과도한 기술 아키텍처 노출 (본문에서)
```

---

## 11. HTML Generation Standard

### 11.1 Required Behavior

```yaml
Stage: fixed 1920 x 1080, transform scale로 뷰포트 대응
Navigation:
  Keyboard:
    - ArrowLeft: previous slide
    - ArrowRight: next slide
    - Space: next slide
    - PageUp: previous slide
    - PageDown: next slide
    - Home: first slide
    - End: last slide
  Mouse:
    - WheelDown: next slide
    - WheelUp: previous slide
    - Debounce: 500-700ms
Fullscreen: F key
Print: P key (@media print 로 페이지 분할)
Page Number: 하단 중앙, Gray, 2자리 (01, 02 ...)
Footer: 모든 콘텐츠 슬라이드에 고정
```

### 11.2 CSS Variables (필수 선언)

```css
:root {
  --amore-blue:    #1F5795;
  --pacific-blue:  #001C58;
  --black:         #000000;
  --gray:          #7D7D7D;
  --white:         #FFFFFF;
  --off-white:     #F7F9FC;
  --light-gray:    #E6EAF0;
  --tint-blue:     #F7FBFF;
  --alert-red:     #D9291C;
  --soft-red:      #FDECEA;
  --success-green: #1C8C5A;
  --soft-green:    #EAF6F0;
  --amber:         #F2A900;
  --soft-amber:    #FFF4D6;
  --font-main: "Pretendard", "Malgun Gothic", "Segoe UI", system-ui, sans-serif;
}
```

### 11.3 Print / PDF Export

```yaml
@media print:
  body background: white
  .slide: display block, transform none, page-break-after always
  .controls: display none
Export Path: 브라우저 인쇄 → PDF 저장 (가로 방향, 여백 없음)
```

### 11.4 Output Naming

```text
ax_action_agent_proposal.html
pif_agent_pilot.html
regulatory_agent_concept.html

규칙: <주제>_<문서성격>.html / 소문자 + 언더스코어
```

---

## 12. Source Folder Structure

```text
AI_Design/
├─ design.md                              ← 이 파일만 지속 갱신
├─ assets/
│  ├─ cover_header_amorepacific.png
│  ├─ content_header_amorepacific.png
│  ├─ footer_left_create_new_beauty.png
│  └─ footer_right_beauty_in_motion.png
├─ templates/
│  └─ BY27_template.pptx
├─ samples/
│  ├─ cover_sample.png
│  └─ content_sample.png
└─ output/
   └─ *.html                              ← Base64 내장 단일 파일
```

```yaml
Update Policy:
  presentation_skill.md: 수시 갱신
  assets/: CI 또는 연도 슬로건 변경 시에만 교체
  templates/: 회사 공식 템플릿 개정 시에만 교체
  samples/: 렌더링 기준 참고용, 선택
```

---

## 13. AI 요청 템플릿 (복사해서 사용)

```text
첨부한 presentation_skill.md 기준으로 발표자료를 만들어줘.

주제: <주제>
대상: <리더 / 유관부서 / 전사>
목적: <설득 / 공유 / 의사결정 요청>
슬라이드 수: <n>장

산출물:
- Base64 이미지 내장 단일 HTML 파일 1개
- assets 폴더 없이 단독 실행 가능해야 함
- 슬라이드 제목만 읽어도 논지가 완성되도록 구성
```

---

## 14. Final Quality Checklist

```yaml
Delivery:
  - [ ] 단일 HTML 파일로 전달되는가
  - [ ] 로고/푸터가 Base64로 내장되었는가
  - [ ] 파일 내 "assets/" 외부 참조가 남아있지 않은가
  - [ ] 단독 실행 시 이미지가 모두 표시되는가

Brand:
  - [ ] AMORE Blue = 강조, PACIFIC Blue = 구조로 사용되었는가
  - [ ] 로고/슬로건이 텍스트로 재현되지 않았는가
  - [ ] 이미지 비율이 왜곡되지 않았는가
  - [ ] Pretendard가 일관 적용되었는가

Layout:
  - [ ] 얇은 선 + 넓은 여백 스타일이 유지되었는가
  - [ ] 콘텐츠가 푸터와 겹치지 않는가 (Footer Right 우측 여백 12px 특히 확인)
  - [ ] 본문 슬라이드 우상단에 Content Header가 적용되었는가 (표지에는 미적용)
  - [ ] 슬라이드당 텍스트 계층이 3단계 이하인가

Content:
  - [ ] 한 슬라이드 = 하나의 메시지인가
  - [ ] 제목만 읽어도 스토리가 연결되는가
  - [ ] 기술 상세가 Appendix로 분리되었는가
  - [ ] 마지막에 요청하는 의사결정이 명확한가
```

---

## Changelog

```yaml
v2.2 (2026-08-31):
  - BY27 템플릿으로 브랜드 자산 전면 교체
  - Content Header(본문 슬라이드 우상단, AMOREPACIFIC 워드마크 소형) 신규 추가
  - Footer Right 자산을 footer_right_by26_statement.png → footer_right_beauty_in_motion.png(BY27 슬로건)로 교체
  - Footer Left/Right 좌표 갱신: 로고 세로폭 확대(53px→80px)로 하단 여백 축소, Footer Right 우측 여백 158px→12px로 축소
  - Asset Rules에 "Content Header/Cover Header 상호 대체 금지" 규칙 추가
  - Final Quality Checklist에 Content Header 적용 여부, Footer Right 여백 확인 항목 추가

v2.1 (2026-08-03):
- 문서명을 AMOREPACIFIC Presentation Skill로 변경
- HTML 슬라이드 Navigation에 Mouse Wheel, Home, End 동작 규칙 추가

v2.0 (2026-07-31):
  - Output Policy를 최상단으로 승격, Base64 내장을 기본 산출 방식으로 확정
  - Source Package와 Deliverable 분리 원칙 명문화
  - Asset Manifest 표 및 px/inch 좌표 동시 제공
  - Contrast / Accessibility 규칙 추가
  - Thin Rule Style을 템플릿 정체성으로 명시
  - Print / PDF Export 규칙 추가
  - Output Naming 규칙 추가
  - AI 요청 템플릿 추가
  - Slide Type Library 15종으로 확장
  - Agent Card에 Exception Handling 필드 추가

v1.0 (2026-07-31):
  - BY26 템플릿 분석 기반 초기 디자인 시스템 작성
  - CI 컬러(AMORE Blue / PACIFIC Blue) 반영
  - Pretendard 기준 타이포그래피 정의
```
