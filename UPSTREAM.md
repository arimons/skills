# 외부 스킬 출처

- 저장소: [mattpocock/skills](https://github.com/mattpocock/skills)
- 확인일: 2026-10-21
- 커밋: `5beb35b040e3de97e54fa9e386d7e42d15c295c2`
- 가져온 경로: `skills/productivity/grill-me`, `skills/productivity/grilling`
- 라이선스: MIT. 각 스킬 폴더에 원문 LICENSE를 보존한다.

`grilling`의 인터뷰 지침은 원문 그대로 유지한다. 최신판은 의존성이 정리된 질문들을 한 라운드에 묶어 묻는다.
`grill-me`는 원본의 사용자 호출 전용 정책을 유지하고, 특정 에이전트의 Skill 도구 대신 상대 경로로 `grilling/SKILL.md`를 읽도록 연결한다. Codex 호출 정책은 `agents/openai.yaml`에도 명시한다.

업스트림 README는 범용·비코딩 인터뷰에 `grill-me`, 용어집과 ADR을 함께 관리하는 코드 설계에는 `grill-with-docs`를 권장한다. 후자는 `domain-modeling`에도 의존하므로 현재 개인 묶음에는 설치하지 않는다.

업데이트할 때는 필요한 스킬과 의존성만 확인하고 이 기록을 갱신한다. 전체 업스트림 플러그인을 동시에 설치하면 수동 설치와 중복될 수 있다.
