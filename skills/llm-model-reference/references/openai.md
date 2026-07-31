<!-- OpenAI 모델명·가격·deprecation 상세 참조 문서 -->
# OpenAI 모델 레퍼런스 — 2026.07 기준

> 상위 문서: [SKILL.md](../SKILL.md). 훈련 데이터 기반 추론 금지 원칙은 상위 문서를 따른다.

## 공식 문서 확인 순서

1. 모델 목록: https://developers.openai.com/api/docs/models
   (전체 카탈로그: https://developers.openai.com/api/docs/models/all)
2. 모델 가이드: https://developers.openai.com/api/docs/guides/latest-model
3. 이미지 생성: https://developers.openai.com/api/docs/guides/image-generation
4. 가격: https://developers.openai.com/api/docs/pricing
5. 변경사항: https://developers.openai.com/api/docs/changelog
6. 사용 중단: https://developers.openai.com/api/docs/deprecations
7. API 레퍼런스 세부 파라미터: https://developers.openai.com/api/docs/api-reference

`platform.openai.com/docs` 보다 위 `developers.openai.com` 문서를 우선한다.

---

## ✅ 현행 사용 가능 모델

> ⚠️ **네이밍 체계 변경 (2026.07.09).** GPT-5.6부터 `mini` / `nano` 대신
> **Sol / Terra / Luna** 티어명을 쓴다. 숫자는 세대, 이름은 성능 티어를 뜻한다.
>
> 💰 **가격 인하 (2026.07.30).** Terra -20%, Luna -80%. Sol은 가격 변동 없이
> fast mode가 추가됐다. ChatGPT/Codex 구독 가격·쿼터는 영향 없음, API 종량 요금만 인하.

**기본 방침: 신규 코드는 GPT-5.6 3티어(sol / terra / luna) 안에서 해결한다.**
agentic 코딩도 별도 codex 모델 대신 `gpt-5.6-terra` 또는 `gpt-5.6-sol` 로 처리한다.

| 용도 | 모델 문자열 | 가격 (in/cached/out per 1M) | 비고 |
|------|------------|------|------|
| 최신 flagship / 최고 난이도 | `gpt-5.6-sol` | $5 / $0.50 / $30 | 별칭 `gpt-5.6` 이 sol로 라우팅됨, fast mode 지원 |
| **기본값** — 일반 개발 / agentic 코딩 | `gpt-5.6-terra` | $2.00 / $0.20 / $12 | 2026.07.30 20% 인하 |
| 고볼륨 / 저비용 / 초경량 작업 | `gpt-5.6-luna` | $0.20 / $0.02 / $1.20 | 2026.07.30 80% 인하 — `gpt-5.4-nano`보다 저렴 |
| 이미지 생성/편집 | `gpt-image-2` | — | **현행 유일한 비-deprecated 이미지 모델** |

### 신규 채택 비권장 (deprecated는 아니나 5.6으로 대체 가능)

| 모델 | 가격 (in/out) | 대체 |
|------|------|------|
| `gpt-5.3-codex` | $1.75 / $14 | → `gpt-5.6-terra` (terra가 더 저렴: $12) |
| `gpt-5.5`, `gpt-5.5-pro` | $5 / $30 | → `gpt-5.6-sol` (동일 가격) |
| `gpt-5.4`, `gpt-5.4-pro` | $2.50 / $15 | → `gpt-5.6-terra` (terra가 20% 저렴) |
| `gpt-5.4-mini` | $0.75 / $4.50 | → `gpt-5.6-luna` (luna가 3.75배 저렴) |
| `gpt-5.4-nano` | $0.20 / $1.25 | → `gpt-5.6-luna` (입력가 동일, 출력가 luna가 더 저렴) |
| `gpt-5.2`, `gpt-5.2-pro` | $1.75 / $14 | → `gpt-5.6-terra` |

---

## ❌ 사용 금지

| 모델 | 상태 |
|------|------|
| `gpt-image-1.5`, `gpt-image-1`, `gpt-image-1-mini`, `chatgpt-image-latest` | deprecated — **종료 2026.12.01** → `gpt-image-2` |
| `dall-e-2`, `dall-e-3` | **제거 완료 (2026.05.12)** |
| `gpt-5-chat-latest`, `gpt-5-codex` | **종료 완료 (2026.07.23)** |
| `gpt-5.2-chat-latest`, `gpt-5.3-chat-latest` | 종료 예정 2026.08.10 |
| `sora-2`, `sora-2-pro` + Videos API | 종료 예정 2026.09.24 |
| `gpt-3.5-turbo-0125`, `gpt-4-0613`, `o1-*`, `o4-mini-*` | 종료 예정 2026.10.23 |
| `gpt-5-2025-08-07`, `gpt-5-mini/nano-2025-08-07`, `gpt-5-pro-2025-10-06`, `o3-*` | 종료 예정 2026.12.11 |
| `gpt-5.2-codex`, `gpt-5.1-codex`, `codex-mini-latest` | deprecated → `gpt-5.6-terra` |
| `gpt-realtime`, `gpt-audio`, `gpt-4o-audio/realtime/mini-*` | 종료 예정 2027.01.20 → `gpt-realtime-2.1` / `gpt-audio-1.5` |
| `gpt-4o`, `gpt-4.1`, `gpt-4.5-preview`, `gpt-4-*`, `gpt-3.5-*` | 구세대, 사용 금지 |

---

## 주의사항

- reasoning 제어: `reasoning_effort` 파라미터 — GPT-5.6부터 **6단계**로 확장
  (`"none"` / `"low"` / `"medium"` / `"high"` / `"xhigh"` / `"max"`).
  기본 출발점은 `"medium"`, `"max"`는 품질 최우선 작업에만 쓴다.
- 신규 프로젝트는 `gpt-5.6-sol` / `gpt-5.6-terra` / `gpt-5.6-luna` 중에서 선택한다.
  `gpt-5.6` 별칭은 sol로 라우팅되므로, 비용을 신경 쓴다면 티어를 명시적으로 지정한다.
- `mini` / `nano` 접미사는 5.4 세대까지만 존재한다. `gpt-5.6-mini` 같은 이름은 **없다**.
- ⚠️ **2026.07.30 가격 인하로 luna/5.4-mini·5.4-nano 비교가 뒤집혔다.**
  luna는 $1/$6 → **$0.20/$1.20** 으로 80% 인하되어, 이제 5.4-mini($0.75/$4.50)보다
  **3.75배 싸고**, 5.4-nano($0.20/$1.25)와 입력가는 같고 출력가는 더 싸다.
  **초경량 대량 작업도 이제 luna 하나로 통일 가능** — `gpt-5.4-nano`를 별도로
  유지할 비용상 이유가 사라졌다. terra도 $2.50/$15 → $2.00/$12 로 20% 인하되어
  `gpt-5.4`보다도 저렴하다.
- ⚠️ **codex 계열 방침**: 공식 문서는 아직 `gpt-5.3-codex` 를
  "most capable agentic coding model to date"로 두고 있고 5.6으로의 마이그레이션
  안내가 없다. 다만 가격 인하 후 terra가 codex보다 출력가도 싸므로($12 vs $14),
  **이 프로젝트에서는 codex 대신 `gpt-5.6-terra` / `gpt-5.6-sol` 로 통일한다.**
  codex는 Responses API 전용이라는 제약도 있다.
- Responses API 권장 (Chat Completions API도 여전히 유효)
- GPT-5.6은 명시적 cache breakpoint와 30분 최소 캐시 수명을 지원한다.
- `gpt-image-2`는 이미지 입력을 항상 high fidelity로 처리하므로 `input_fidelity`를 보내지 않는다.
- `gpt-image-2`는 `size`에 다양한 해상도를 받을 수 있지만, 최대 변 길이,
  16px 배수, 비율, 총 픽셀 수 제약을 developers 이미지 생성 문서에서 확인한다.
  저비용이 필요하면 별도 mini 모델 대신 `quality="low"` 로 조절한다.
- ChatGPT 웹의 이미지 생성 도구 호출 가능 여부와 API 모델명 노출 여부는 별개다.
  웹 자동화 코드를 작성할 때는 대화 모델/도구 선택 UI와 프롬프트 제어를 별도 경로로 취급한다.

---

## 예시 코드 (Python)

```python
from openai import OpenAI

client = OpenAI()

# ✅ 현행 flagship
response = client.responses.create(
    model="gpt-5.6-sol",
    input="...",
    reasoning={"effort": "high"}   # none / low / medium / high / xhigh / max
)

# ✅ 일상 개발 / agentic 코딩 — 기본값
response = client.responses.create(
    model="gpt-5.6-terra",
    input="...",
    reasoning={"effort": "medium"}
)

# ✅ 고볼륨 저비용 / 초경량 대량 분류 — 2026.07.30 인하로 5.4-nano보다 저렴
response = client.responses.create(
    model="gpt-5.6-luna",
    input="다음 텍스트를 긍정/부정/중립 중 하나로만 분류: ...",
    reasoning={"effort": "none"}
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
# model="gpt-5.6-mini"   # 존재하지 않는 이름 (5.6은 sol/terra/luna)
# model="gpt-5.3-codex"  # deprecated는 아니나 terra로 통일
# model="gpt-5.4-nano"   # 2026.07.30 인하 후 luna로 통일 권장 (가격 우위 사라짐)
# model="gpt-image-1.5"  # deprecated, 2026.12.01 종료
# model="gpt-4o"         # deprecated
# model="gpt-3.5-turbo"  # 구세대
```

> 마지막 업데이트: 2026.07.31
