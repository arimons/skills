# arimons/skills

개인용 설계 인터뷰와 사내 AI 연동·보고서·발표자료 스킬 모음입니다. 원본은 `~/Developer/skills` 한 곳에서 관리합니다.

## 스킬 목록

| 스킬 | 설명 |
|------|------|
| [grill-me](skills/grill-me/SKILL.md) | 직접 요청했을 때 계획·설계를 검증하는 인터뷰 시작 |
| [grilling](skills/grilling/SKILL.md) | grill-me가 사용하는 인터뷰 본체. 별도 사용 준비는 필요 없음 |
| [internal-ai-endpoint](skills/internal-ai-endpoint/SKILL.md) | 사내 AI Studio REST 연동 규격과 키 없는 환경 파일 템플릿 |
| [html-document-design](skills/html-document-design/SKILL.md) | 개인·사내 HTML 보고서와 가이드 디자인 |
| [amorepacific-presentation](skills/amorepacific-presentation/SKILL.md) | BY27 사내 HTML 발표자료 템플릿·로고·푸터 |
| [slide-to-pptx](skills/slide-to-pptx/SKILL.md) | 고정 배치 HTML 슬라이드를 편집 가능한 PPTX로 변환 |

`grill-me`와 `grilling`은 Matt Pocock 최신 확인 커밋에서 가져왔습니다. [출처·로컬 변경](UPSTREAM.md)을 참고하세요. 범용 인터뷰에는 `grill-me`, 용어집·ADR을 만드는 코드 설계에는 업스트림 `grill-with-docs`가 맞습니다. 후자는 현재 설치하지 않습니다.

## 개인 설치와 업데이트

- Codex: `~/.agents/skills/<스킬명>`에서 이 저장소의 `skills/<스킬명>`으로 심볼릭 링크를 연결합니다.
- Claude Code: `~/.claude/skills/<스킬명>`에서도 같은 원본으로 연결합니다.
- Codex의 `~/.codex/skills`에 동일한 링크를 추가하지 않습니다. 내장 `.system`은 유지합니다.
- 원본 저장소를 업데이트하면 연결된 스킬에도 반영됩니다. `npx skills update -g`로 별도 복사본을 다시 설치하지 않습니다.

## 플러그인 배포

`.claude-plugin/marketplace.json`에 다음 묶음을 등록합니다.

- `ap-report-skills`: HTML 문서 디자인, 사내 발표자료, HTML→PPTX 변환.
- `personal-tools`: grill-me와 grilling, 사내 AI 엔드포인트.

개인 로컬 설치는 위 심볼릭 링크 방식만 사용합니다. 같은 에이전트에서 동일 스킬의 플러그인 설치와 수동 연결을 함께 사용하지 않습니다.

## 사내 AI 설정

실제 사내 주소·에이전트 식별자·API 키는 로컬 `.env`에서 관리하고 Git에 올리지 않습니다. 공개 템플릿에는 실제 주소와 키를 넣지 않습니다. 모델·파라미터는 대상 환경에서 지원하는 값을 확인해 설정합니다.

## 실행 의존성

- 자산 내장: Python 3 표준 라이브러리.
- 선택적 폰트 내장: `fonttools`, `brotli`, Node.js/npm. 요청한 경우에만 사용합니다.
- PPTX 변환: `playwright`, `python-pptx`, Playwright Chromium.
- 사내 AI 예제: `requests`, `python-dotenv`.

`manual-voice`는 이 묶음에 포함되지 않은 선택 의존성입니다. 디자인·발표자료의 서체·색·로고 규격은 각 스킬을 따릅니다.
