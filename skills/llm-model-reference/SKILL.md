# LLM Model Reference — 2026.05 기준

> 이 SKILL의 목적: 코드에서 LLM 모델명을 사용할 때 outdated/deprecated 모델이
> 들어가지 않도록 현행 모델 기준을 강제한다.
>
> ⚠️ 중요 원칙: 훈련 데이터 기반으로 모델명을 추론하지 말 것.
> 아래 테이블에 없는 모델명은 절대 코드에 사용하거나 추천하지 말 것.
>
> ⚠️ 문서 원칙: OpenAI는 `platform.openai.com/docs`보다
> `https://developers.openai.com/api/docs` 쪽을 우선 확인한다. 이미지 생성,
> 최신 모델, Responses API 문서가 developers 문서에 먼저 반영되는 경우가 있다.
> Gemini는 `https://ai.google.dev/gemini-api/docs`의 모델/이미지 생성 문서를
> 우선 확인한다.
>
> ⚠️ Context7 예외: 이 스킬을 적용하는 모델명 검증/최신 모델 확인 작업에서는
> Context7을 기준으로 삼지 않는다. Context7은 GA/안정 문서 중심으로 인덱싱되어
> preview 또는 갓 출시된 모델을 누락할 수 있으므로, 아래 공식 문서를 직접 확인한다.

---

## 공식 문서 확인 순서

### OpenAI

1. 모델 목록: https://developers.openai.com/api/docs/models
2. 이미지 생성: https://developers.openai.com/api/docs/guides/image-generation
3. 변경사항: https://developers.openai.com/api/docs/changelog
4. API 레퍼런스 세부 파라미터: https://developers.openai.com/api/docs/api-reference

### Google Gemini

1. 모델 목록: https://ai.google.dev/gemini-api/docs/models
2. 이미지 생성: https://ai.google.dev/gemini-api/docs/image-generation
3. 모델 버전/지원 상태: https://ai.google.dev/gemini-api/docs/models/gemini
4. 사용 중단: https://ai.google.dev/gemini-api/docs/deprecations

---

## Google Gemini

### ✅ 현행 사용 가능 모델 (2026.05)

| 용도 | 모델 문자열 | 비고 |
|------|------------|------|
| 최고 성능 / 복잡한 추론 | `gemini-3.1-pro-preview` | preview, GA 예정 |
| 고성능 균형 (agentic) | `gemini-3-flash-preview` | preview, GA 예정 |
| 경량 / 고볼륨 / 저비용 | `gemini-3.1-flash-lite-preview` | preview |
| custom tool 우선 agentic | `gemini-3.1-pro-preview-customtools` | 3.1-pro 변형 |
| 이미지 생성/편집 최고 품질 | `gemini-3-pro-image-preview` | Nano Banana Pro |
| 이미지 생성/편집 고효율 | `gemini-3.1-flash-image-preview` | Nano Banana 2 |

### ❌ 사용 금지 (deprecated / shutdown)

| 모델 | 상태 |
|------|------|
| `gemini-3-pro-preview` | **shutdown (2026.03.09)** — 사용 시 오류 |
| `gemini-2.5-flash-lite-preview-09-2025` | shutdown (2026.03.31) |
| `gemini-2.0-flash`, `gemini-2.0-flash-lite` | **shutdown 예정 2026.06.01** |
| `gemini-2.5-flash`, `gemini-2.5-pro` | **shutdown 예정 2026.06.17** |
| `gemini-1.5-*`, `gemini-1.0-*` | 이미 종료, 404 반환 |

### 주의사항

- `gemini-3.1-flash` (일반 텍스트 모델)와 `gemini-3.1-flash-image-preview`
  (이미지 생성/편집 모델)를 혼동하지 말 것
- Gemini 웹에서 Nano Banana 도구 호출 가능 여부는 API 모델명과 별개다.
  웹 자동화 코드를 작성할 때는 대화 모델 선택 UI와 이미지 생성 도구 유도 프롬프트를
  별도 경로로 취급한다.
- `gemini-3-flash` deprecated 예정이라는 주장은 **근거 없음** (2026.03 기준)
- 모든 Gemini 3 계열은 현재 preview 상태 (GA 미완료)

#### Thinking Budget 설정 (⚠️ 누락 시 max_tokens 초과 오류 발생)

Gemini thinking 모델은 `thinking_budget`을 명시하지 않으면 모델 기본값이 활성화되어
응답 토큰이 급격히 늘어나고 max_tokens 초과로 응답이 잘린다.
**Gemini 코드 작성 시 반드시 작업 유형에 맞는 budget을 설정하거나, 사용자에게 확인한다.**

| 작업 유형 | thinking_budget | 이유 |
|----------|----------------|------|
| 단순 분류 / 추출 / 포맷 변환 | `0` (no thinking) | thinking 불필요, 비용/속도 최적 |
| 문맥 번역 / 요약 / 품질 필요 작업 | `1024` | 최소한의 reasoning으로 품질 확보 |
| 복잡한 추론 / 다단계 분석 | `8192` 이상 | 작업 복잡도에 따라 조정 |

> **Agent 행동 규칙**: Gemini API 코드를 작성할 때는 thinking_budget 값을 코드에
> 명시하거나, 불명확한 경우 사용자에게 "이 작업이 단순 분류인지, 품질이 필요한
> 작업인지" 확인한 뒤 위 표를 기준으로 설정한다. 기본값(미설정)으로 코드를 작성하지 않는다.

### 예시 코드 (Python)

> ⚠️ **패키지 주의**: `google-genai` 패키지 사용 (`import google.genai`)
> `google-generativeai` (`import google.generativeai`) 는 **구형/deprecated — 절대 사용 금지**

```python
# ✅ 반드시 이 import 사용 (pip install google-genai)
import google.genai as genai
from google.genai import types

client = genai.Client(api_key="YOUR_API_KEY")

# ✅ 단순 분류 / 추출 — thinking 없음 (budget=0)
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="다음 텍스트의 감정을 긍정/부정/중립 중 하나로만 답해줘: ...",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0),
        max_output_tokens=10,
    )
)

# ✅ 문맥 번역 / 품질 필요 작업 — budget=1024
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="다음 문장을 자연스러운 한국어로 번역해줘: ...",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024),
        max_output_tokens=2048,
    )
)

# ✅ 복잡한 추론 — budget 높게
response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="...",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=8192),
        max_output_tokens=4096,
    )
)

# ✅ 일반 요청 (thinking 불필요한 경우)
response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="..."
)
print(response.text)

# 이미지 생성/편집 고효율
response = client.models.generate_content(
    model="gemini-3.1-flash-image-preview",
    contents="Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme",
    config=types.GenerateContentConfig(
        response_modalities=["Image"]
    )
)

# 이미지 생성/편집 최고 품질
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Create a Korean comic cover typography layout.",
    config=types.GenerateContentConfig(
        response_modalities=["Image"]
    )
)

# ❌ 사용 금지 — 아래 패턴은 구형 SDK (google-generativeai)
# import google.generativeai as genai          ← 금지
# genai.configure(api_key=...)                 ← 금지
# genai.GenerativeModel("gemini-...")          ← 금지
# model.generate_content(...)                  ← 금지 (client 패턴 사용할 것)

# ❌ 사용 금지 모델명
# client.models.generate_content(model="gemini-2.5-flash", ...)   # 6월 종료 예정
# client.models.generate_content(model="gemini-1.5-pro", ...)     # 이미 종료

# ❌ thinking_budget 미설정 — 기본값 활성화로 max_tokens 초과 위험
# config=types.GenerateContentConfig(max_output_tokens=512)  # thinking_budget 없음 ← 위험
```

---

## OpenAI

### ✅ 현행 사용 가능 모델 (2026.05)

| 용도 | 모델 문자열 | 비고 |
|------|------------|------|
| 최신 flagship | `gpt-5.5` | developers 문서의 Latest 모델 |
| 최고 성능 flagship | `gpt-5.4` | snapshot: `gpt-5.4-2026-03-05` |
| 고볼륨 / 저비용 | `gpt-5.4-mini` | snapshot: `gpt-5.4-mini-2026-03-17` |
| 초경량 단순 작업 | `gpt-5.4-nano` | compaction 지원 |
| agentic 코딩 특화 | `gpt-5.3-codex` | Codex + GPT-5 통합 모델 |
| 이전 세대 (여전히 유효) | `gpt-5.2` | deprecated 아님, 구세대 |
| 이미지 생성/편집 최신 | `gpt-image-2` | GPT Image 2, 고해상도/텍스트 레이아웃 개선 |
| 이미지 생성/편집 이전 세대 | `gpt-image-1.5` | GPT Image 2 이전 세대 |
| 이미지 생성/편집 구세대 | `gpt-image-1` | 기존 GPT Image |
| 이미지 생성/편집 경량 | `gpt-image-1-mini` | 저비용 이미지 생성 |

### ❌ 사용 금지

| 모델 | 상태 |
|------|------|
| `gpt-5.1` | ChatGPT에서 2026.03.11 종료 (API는 유지, 신규 사용 비권장) |
| `gpt-4o`, `gpt-4.1`, `gpt-4.5-preview` | deprecated 발표됨 |
| `gpt-4-*`, `gpt-3.5-*` | 구세대, 사용 금지 |

### 주의사항

- reasoning 제어: `reasoning_effort` 파라미터 — `"low"` / `"medium"` / `"high"` / `"xhigh"`
- 신규 프로젝트는 developers 모델 문서에서 최신 flagship을 확인한 뒤 `gpt-5.5`, `gpt-5.4`, `gpt-5.4-mini` 중 선택
- Responses API 권장 (Chat Completions API도 여전히 유효)
- `gpt-image-2`는 이미지 입력을 항상 high fidelity로 처리하므로 `input_fidelity`를 보내지 않는다.
- `gpt-image-2`는 `size`에 다양한 해상도를 받을 수 있지만, 최대 변 길이,
  16px 배수, 비율, 총 픽셀 수 제약을 developers 이미지 생성 문서에서 확인한다.
- ChatGPT 웹의 이미지 생성 도구 호출 가능 여부와 API 모델명 노출 여부는 별개다.
  웹 자동화 코드를 작성할 때는 대화 모델/도구 선택 UI와 프롬프트 제어를 별도 경로로 취급한다.

### 예시 코드 (Python)

```python
from openai import OpenAI

client = OpenAI()

# ✅ 현행 flagship
response = client.responses.create(
    model="gpt-5.4",
    input="...",
    reasoning={"effort": "high"}
)

# 이미지 편집
response = client.images.edit(
    model="gpt-image-2",
    image=[open("comic-page.png", "rb")],
    prompt="Replace speech bubble text with the provided Korean translation.",
    size="auto",
    quality="medium"
)

# ❌ 사용 금지
# model="gpt-4o"    # deprecated
# model="gpt-3.5-turbo"  # 구세대
```

---

## Anthropic Claude

### ✅ 현행 사용 가능 모델 (2026.03)

| 용도 | 모델 문자열 | 비고 |
|------|------------|------|
| 최고 성능 | `claude-opus-4-6` | 현재 최신 Opus |
| 일상 균형 (권장) | `claude-sonnet-4-6` | 성능/비용 균형 최적 |
| 경량 / 고속 | `claude-haiku-4-5-20251001` | 저비용 고속 |

### ❌ 사용 금지

| 모델 | 상태 |
|------|------|
| `claude-opus-4`, `claude-opus-4-1` | API에서 제거됨 (`4-6`으로 자동 마이그레이션) |
| `claude-3-5-sonnet-*`, `claude-3-*` | 구세대, 신규 사용 비권장 |
| `claude-2-*`, `claude-1-*` | 종료 |

### 주의사항

- Claude 4.6 패밀리: Opus 4.6 / Sonnet 4.6 / Haiku 4.5
- extended thinking: `thinking` 파라미터로 제어 (`budget_tokens` 설정)
- 1M 토큰 컨텍스트: Max/Team/Enterprise 플랜에서만 사용 가능

### 예시 코드 (Python)

```python
import anthropic

client = anthropic.Anthropic()

# ✅ 현행 모델
response = client.messages.create(
    model="claude-sonnet-4-6",  # 일반 권장
    max_tokens=1024,
    messages=[{"role": "user", "content": "..."}]
)

# 최고 성능 필요 시
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=2048,
    messages=[{"role": "user", "content": "..."}]
)

# ❌ 사용 금지
# model="claude-3-5-sonnet-20241022"  # 구세대
```

---

## 모델 선택 가이드 (요약)

| 상황 | 추천 |
|------|------|
| 복잡한 추론, 고품질 우선 | `gemini-3.1-pro-preview` / `gpt-5.4` / `claude-opus-4-6` |
| 일반 개발, 균형 | `gemini-3-flash-preview` / `gpt-5.4-mini` / `claude-sonnet-4-6` |
| 고볼륨, 비용 민감 | `gemini-3.1-flash-lite-preview` / `gpt-5.4-nano` / `claude-haiku-4-5-20251001` |
| agentic 코딩 특화 | `gemini-3.1-pro-preview-customtools` / `gpt-5.3-codex` |
| 이미지 생성/편집 최고 품질 | `gemini-3-pro-image-preview` / `gpt-image-2` |
| 이미지 생성/편집 빠른 처리 | `gemini-3.1-flash-image-preview` / `gpt-image-1-mini` |

---

## 업데이트 주기

이 SKILL은 최소 월 1회 업데이트 권장.
공식 deprecation/모델 문서 확인 출처:
- Gemini: https://ai.google.dev/gemini-api/docs/models,
  https://ai.google.dev/gemini-api/docs/image-generation,
  https://ai.google.dev/gemini-api/docs/deprecations
- OpenAI: https://developers.openai.com/api/docs/models,
  https://developers.openai.com/api/docs/guides/image-generation,
  https://developers.openai.com/api/docs/changelog
- Claude: https://docs.anthropic.com/en/docs/about-claude/models

> 마지막 업데이트: 2026.06.25
