# arimons/skills

개인용 + Vibe Coding 강의 배포용 AI 에이전트 스킬 모음.

[Agent Skills](https://github.com/vercel-labs/skills) 오픈 스탠다드를 따릅니다.

## 설치

```bash
npx skills add arimons/skills -g
```

## 스킬 목록

| 스킬 | 설명 |
|------|------|
| `llm-model-reference` | Gemini/OpenAI/Claude 현행 모델 레퍼런스 (deprecated 방지, thinking budget 가이드 포함) |
| `grill-me` | 프로젝트 설계 전 인터뷰로 막연한 아이디어를 구체적 설계로 변환 |

## 업데이트

```bash
npx skills update -g
```

## HTML 문서·발표자료 스킬

2026-10-13 제공 `ap-skills_20261013_r6.zip`에서 검토하여 반영한 r6 스킬입니다. 사내 공유 HTML과 PPTX의 기본 서체는 아리따 돋움이며, 슬라이드 템플릿은 Finder 미리보기도 지원합니다.

| 스킬 | 설명 |
|------|------|
| `html-document-design` | HTML 보고서·가이드 디자인, 테마 전환, 사내 공유용 아리따 돋움 |
| `amorepacific-presentation` | BY27 사내 HTML 발표자료 템플릿·로고·푸터 |
| `slide-to-pptx` | 1920×1080 고정 배치 HTML을 편집 가능한 PPTX로 변환 |

### Codex / Claude Code 공통 설치

저장소의 `skills/<스킬명>`을 공통 원본으로 두고, Codex 개인 경로 `~/.agents/skills/<스킬명>`과 Claude Code 개인 경로 `~/.claude/skills/<스킬명>`에 심볼릭 링크로 연결합니다. 기존 항목이 있다면 먼저 백업하세요. 기존 Codex 설치의 `~/.codex/skills` 링크를 유지하는 경우에도 같은 원본을 가리키게 합니다.

### 실행 의존성

- 자산 내장: Python 3 표준 라이브러리.
- 선택적 폰트 내장(명시적으로 요청한 경우만): Python `fonttools`, `brotli` 및 Node.js/npm. 최초 실행 시 npm에서 폰트를 받아 `~/.cache/ap-doc-fonts`에 캐시합니다.
- PPTX 변환: Python `playwright`, `python-pptx`, Playwright Chromium.
- `manual-voice`는 선택 사항이며 이 저장소의 제공 ZIP에는 포함되지 않습니다.

설치 위치를 기준으로 스크립트 경로를 해석하고, 변환할 파일에는 작업 디렉터리에 맞는 경로를 지정하세요.
