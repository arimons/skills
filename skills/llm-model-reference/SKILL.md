---
name: llm-model-reference
description: >
  Use BEFORE writing any model name, SDK call, or API code involving an LLM,
  and when choosing a model, comparing cost, or migrating an existing model name.
  Triggers on: LLM, AI, 모델명, 모델 이름, model name, 모델 선택, 어떤 모델,
  OpenAI, GPT, gpt-5, Codex, Responses API, Gemini, google-genai, Nano Banana,
  Claude, Anthropic, API 키, API key, SDK, thinking budget, reasoning effort,
  이미지 생성, gpt-image, deprecated 모델, 모델 마이그레이션, 모델 교체.
  IMPORTANT: Never infer a model name from training data. If a model string is
  not in this skill's tables, do not write or recommend it.
---

# LLM Model Reference — 2026.07 기준

> 이 SKILL의 목적: 코드에서 LLM 모델명을 사용할 때 outdated/deprecated 모델이
> 들어가지 않도록 현행 모델 기준을 강제한다.

## ⚠️ 원칙

- **훈련 데이터 기반으로 모델명을 추론하지 말 것.** 아래 표와 참조 문서에 없는
  모델명은 절대 코드에 사용하거나 추천하지 말 것.
- **Context7을 기준으로 삼지 않는다.** GA/안정 문서 중심으로 인덱싱되어
  preview 또는 갓 출시된 모델을 누락한다. 각 참조 문서에 적힌 공식 문서를 직접 확인한다.
- OpenAI는 `platform.openai.com/docs` 보다 `developers.openai.com/api/docs` 를 우선한다.

---

## 현행 모델 (이 표에 없으면 쓰지 말 것)

| 용도 | OpenAI | Gemini | Claude |
|------|--------|--------|--------|
| 최상위 | `gpt-5.6-sol` | `gemini-3.1-pro-preview` | `claude-fable-5` |
| 고성능 | `gpt-5.6-sol` | `gemini-3.5-flash` | `claude-opus-5` |
| 균형 (기본값) | `gpt-5.6-terra` | `gemini-3.6-flash` | `claude-sonnet-5` |
| 경량 / 고볼륨 / 초저가 대량 처리 | `gpt-5.6-luna` | `gemini-3.5-flash-lite` | `claude-haiku-4-5-20251001` |
| 이미지 최고 품질 | `gpt-image-2` | `gemini-3-pro-image` | — |
| 이미지 고속 | `gpt-image-2` (`quality="low"`) | `gemini-3.1-flash-lite-image` | — |

### 가장 자주 나는 실수

- `gpt-5.6-mini` / `gpt-5.6-nano` — **존재하지 않음.** 5.6은 sol / terra / luna 3티어.
- `gpt-5.4-nano`를 초저가 대안으로 고정 추천하는 것 — **2026.07.30 가격 인하로 luna가
  더 싸졌다.** 이제 초경량 작업도 `gpt-5.6-luna`로 통일한다.
- `gemini-3.1-flash-image-preview`, `gemini-3-pro-image-preview` — GA 승격으로
  **`-preview` 접미사 제거됨.**
- `gemini-3.1-flash` (텍스트) — **존재하지 않음.**
- `claude-opus-5` / `claude-sonnet-5` 에 `thinking={"type": "enabled"}` — **미지원.**
- Claude Opus 4.7 이후 모델에 `temperature` / `top_p` / `top_k` — **400 오류.**

---

## 상세 참조 문서

모델명·가격·종료일·예시 코드·파라미터 제약은 해당 provider 문서를 읽는다.

| Provider | 문서 | 언제 읽나 |
|----------|------|----------|
| OpenAI | [references/openai.md](references/openai.md) | GPT / Codex / GPT Image 코드 작성, 가격 비교, 종료일 확인 |
| Gemini | [references/gemini.md](references/gemini.md) | Gemini / Nano Banana 코드 작성, **thinking_budget 설정 시 필수** |
| Claude | [references/claude.md](references/claude.md) | Claude API 코드 작성, thinking·temperature 제약 확인 |

### 반드시 참조 문서를 열어야 하는 경우

- Gemini 코드를 쓸 때 — `thinking_budget` 미설정은 max_tokens 초과 오류로 이어진다.
- Claude 코드를 쓸 때 — 세대별로 `thinking` / `temperature` 지원 여부가 갈린다.
- 비용을 근거로 모델을 고를 때 — 단가는 참조 문서에만 있다.
- 기존 코드의 모델명을 마이그레이션할 때 — 종료일과 대체 모델 매핑이 필요하다.

---

## 업데이트 주기

이 SKILL은 최소 월 1회 업데이트 권장. 각 참조 문서 상단의 "공식 문서 확인 순서"를
그대로 따라 확인하고, 확인되지 않은 항목은 추측해서 채우지 않는다.

> 마지막 업데이트: 2026.07.31
