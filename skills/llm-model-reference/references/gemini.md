<!-- Google Gemini 모델명·thinking budget·deprecation 상세 참조 문서 -->
# Google Gemini 모델 레퍼런스 — 2026.07 기준

> 상위 문서: [SKILL.md](../SKILL.md). 훈련 데이터 기반 추론 금지 원칙은 상위 문서를 따른다.

## 공식 문서 확인 순서

1. 모델 목록: https://ai.google.dev/gemini-api/docs/models
2. 이미지 생성: https://ai.google.dev/gemini-api/docs/image-generation
3. 모델 버전/지원 상태: https://ai.google.dev/gemini-api/docs/models/gemini
4. 사용 중단: https://ai.google.dev/gemini-api/docs/deprecations

---

## ✅ 현행 사용 가능 모델

| 용도 | 모델 문자열 | 비고 |
|------|------------|------|
| 최고 성능 / 복잡한 추론 | `gemini-3.1-pro-preview` | **여전히 preview** — Pro 계열 GA 모델 없음 |
| 최신 범용 (agentic / 멀티모달) | `gemini-3.6-flash` | GA, 최신 flash |
| agentic / 코딩 프론티어 | `gemini-3.5-flash` | GA |
| 경량 / 고볼륨 / 저비용 | `gemini-3.5-flash-lite` | GA, 고처리량 |
| 저비용 프론티어급 | `gemini-3.1-flash-lite` | GA (shutdown 예정 2027.05.07) |
| 고성능 균형 (구 preview) | `gemini-3-flash-preview` | 아직 preview 상태로 유지 |
| 이미지 생성/편집 최고 품질 | `gemini-3-pro-image` | Nano Banana Pro, 4K |
| 이미지 생성/편집 범용 | `gemini-3.1-flash-image` | Nano Banana 2, 4K |
| 이미지 생성/편집 초고속 | `gemini-3.1-flash-lite-image` | Nano Banana 2 Lite, 1K 전용 |

---

## ❌ 사용 금지 (deprecated / shutdown)

| 모델 | 상태 |
|------|------|
| `gemini-3-pro-preview` | **shutdown (2026.03.09)** — 사용 시 오류 |
| `gemini-3-pro-image-preview`, `gemini-3.1-flash-image-preview` | GA 승격으로 **`-preview` 접미사 제거됨** |
| `gemini-3.1-flash-lite-preview` | GA 승격 → `gemini-3.1-flash-lite` 사용 |
| `gemini-3.1-pro-preview-customtools` | **공식 문서에서 사라짐** — 종료일 미공개, 사용 금지 |
| `gemini-2.5-flash-lite-preview-09-2025` | shutdown (2026.03.31) |
| `gemini-2.0-flash`, `gemini-2.0-flash-lite` | **shutdown 완료 (2026.06.01)** |
| `gemini-2.5-pro`, `gemini-2.5-flash`, `gemini-2.5-flash-lite` | **shutdown 예정 2026.10.16** |
| `gemini-2.5-flash-image` | Nano Banana 1 — legacy, 이전 권고 |
| `gemini-1.5-*`, `gemini-1.0-*` | 이미 종료, 404 반환 |

---

## 주의사항

- **`-preview` 접미사 대거 제거됨.** 이미지 모델 3종과 flash-lite가 GA로 승격되면서
  기존 코드의 `gemini-3-pro-image-preview` / `gemini-3.1-flash-image-preview` /
  `gemini-3.1-flash-lite-preview` 는 모두 접미사 없는 이름으로 바꿔야 한다.
- 텍스트 모델 `gemini-3.1-flash` 는 **존재하지 않는다** (문서상 3.1 계열 텍스트는
  `gemini-3.1-flash-lite` 뿐). `gemini-3.1-flash-image` 는 이미지 전용 모델이다.
- Pro 계열은 `gemini-3.1-pro-preview` 하나뿐이고 아직 preview다.
  프로덕션 안정성이 필요하면 GA인 `gemini-3.6-flash` / `gemini-3.5-flash` 를 우선 고려한다.
- Gemini 웹에서 Nano Banana 도구 호출 가능 여부는 API 모델명과 별개다.
  웹 자동화 코드를 작성할 때는 대화 모델 선택 UI와 이미지 생성 도구 유도 프롬프트를
  별도 경로로 취급한다.
- `gemini-3.1-flash-lite-image` 는 1K 해상도만 지원하고 Google Search grounding이 없다.

---

## Thinking Budget 설정 (⚠️ 누락 시 max_tokens 초과 오류 발생)

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

---

## 예시 코드 (Python)

> ⚠️ **패키지 주의**: `google-genai` 패키지 사용 (`import google.genai`)
> `google-generativeai` (`import google.generativeai`) 는 **구형/deprecated — 절대 사용 금지**

```python
# ✅ 반드시 이 import 사용 (pip install google-genai)
import google.genai as genai
from google.genai import types

client = genai.Client(api_key="YOUR_API_KEY")

# ✅ 단순 분류 / 추출 — thinking 없음 (budget=0)
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="다음 텍스트의 감정을 긍정/부정/중립 중 하나로만 답해줘: ...",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0),
        max_output_tokens=10,
    )
)

# ✅ 문맥 번역 / 품질 필요 작업 — budget=1024
response = client.models.generate_content(
    model="gemini-3.6-flash",
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

# 이미지 생성/편집 범용 (GA — preview 접미사 없음)
response = client.models.generate_content(
    model="gemini-3.1-flash-image",
    contents="Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme",
    config=types.GenerateContentConfig(
        response_modalities=["Image"]
    )
)

# 이미지 생성/편집 최고 품질 (GA — preview 접미사 없음)
response = client.models.generate_content(
    model="gemini-3-pro-image",
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
# client.models.generate_content(model="gemini-2.5-flash", ...)          # 2026.10.16 종료 예정
# client.models.generate_content(model="gemini-2.0-flash", ...)          # 2026.06.01 종료 완료
# client.models.generate_content(model="gemini-3.1-flash-image-preview", ...)  # GA 승격, 접미사 제거
# client.models.generate_content(model="gemini-1.5-pro", ...)            # 이미 종료

# ❌ thinking_budget 미설정 — 기본값 활성화로 max_tokens 초과 위험
# config=types.GenerateContentConfig(max_output_tokens=512)  # thinking_budget 없음 ← 위험
```

> 마지막 업데이트: 2026.07.28
