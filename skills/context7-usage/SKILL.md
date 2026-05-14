---
name: context7-usage
description: Use when the user mentions LLM, AI API, Gemini, OpenAI, Claude API, 모델 연동, AI 연동, API 연동, or external library integration. Do not use for model availability, latest model lists, preview model validation, or llm-model-reference work.
---
# Context7 사용 규칙
## 반드시 조회 (Context7 필수)
### LLM / AI API 관련
- Gemini, OpenAI, Claude, Anthropic 등 LLM API 코드 작성 시
- LLM 클라이언트 초기화 시 (예: `genai.Client`, `openai.OpenAI`)
- 임베딩, 멀티모달, 파일 업로드 등 API 기능 사용 시
- 외부 라이브러리의 클래스명·메서드명·엔드포인트를 공식 문서 URL 없이 추측해야 할 때
- → **클래스명·메서드명·엔드포인트는 학습 데이터 기준으로 틀릴 수 있음. 반드시 최신 문서 확인**

### ❗ 모델명 예외

다음 작업에는 Context7을 사용하지 않는다.

- `llm-model-reference` 스킬이 적용되는 모델명 검증/최신 모델 확인 작업
- preview, beta, newly released 모델의 존재 여부를 확인하는 작업
- OpenAI/Gemini/Claude 모델 목록 자체를 갱신하는 작업
- API 문서에는 있지만 Context7 인덱스에 아직 반영되지 않았을 수 있는 모델 확인

Context7은 GA 문서나 안정 버전 문서 중심으로 결과를 반환할 수 있어,
Gemini preview 이미지 모델이나 OpenAI 신규 이미지 모델처럼 공식 문서에는 있지만
Context7 인덱스에 늦게 반영되는 모델을 누락할 수 있다.

따라서 모델명/모델 목록/preview 지원 여부를 다룰 때는 `llm-model-reference`
스킬을 우선하고, 그 스킬에 적힌 공식 문서 링크를 직접 확인한다.
이 경우 Context7 조회 결과로 공식 문서의 모델명을 부정하지 않는다.

### ❗ 검색(Query) 작성 원칙
1. **선입견 배제**: Context7에 `query`를 던질 때, 과거 학습 데이터의 특정 버전이나 모델명을 검색어에 미리 포함하지 않는다.
2. **최신 정보 탐색**: "What is the latest API usage and how to use it?"처럼 중립적이고 범용적인 질문을 던진다.

### 외부 라이브러리 일반
- 이 프로젝트에서 해당 라이브러리를 처음 사용할 때
- 라이브러리 버전이 바뀐 후 첫 작업 시
- 에러가 "deprecated" 또는 버전 관련일 때
- 공식 문서 URL이 없는 상태에서 API 스펙을 추측해야 할 때

## 조회 불필요 (Context7 생략)
- 모델명 최신성/preview 모델 여부 검증
- 이미 이 세션에서 검증된 패턴 반복 시
- 기본 Python / JS 문법 (조건문, 반복문, 함수 등)
- 이미 작동 중인 코드 패턴 재사용 시
- 표준 라이브러리 (os, json, datetime 등)

## 절차
1. Context7에서 해당 라이브러리 최신 문서 조회
2. 현재 설치 버전 확인 (`pip show 패키지명` 또는 `npm list 패키지명`)
3. 문서 기준 최신 클래스명·메서드명·엔드포인트로 코드 작성
4. 사용한 버전 및 API 방식을 주석으로 명시

## 판단 기준
코드에 외부 서비스의 **클래스명, 메서드명, 엔드포인트, SDK 초기화 방식**이 들어간다면
→ Context7 조회 후 작성한다.

코드에 **모델명**이 들어간다면
→ `llm-model-reference`와 공식 문서를 우선한다.
