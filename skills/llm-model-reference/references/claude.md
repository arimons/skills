<!-- Anthropic Claude 모델명·파라미터 제약·deprecation 상세 참조 문서 -->
# Anthropic Claude 모델 레퍼런스 — 2026.07 기준

> 상위 문서: [SKILL.md](../SKILL.md). 훈련 데이터 기반 추론 금지 원칙은 상위 문서를 따른다.

## 공식 문서 확인 순서

1. 모델 목록: https://docs.anthropic.com/en/docs/about-claude/models
   → `https://platform.claude.com/docs/en/docs/about-claude/models` 로 **301 리다이렉트**
2. 사용 중단: https://platform.claude.com/docs/en/docs/about-claude/model-deprecations
3. 마이그레이션: https://platform.claude.com/docs/en/docs/about-claude/models/migration-guide

---

## ✅ 현행 사용 가능 모델

| 용도 | 모델 문자열 | 가격 (in/out per 1M) | 컨텍스트 | 비고 |
|------|------------|------|------|------|
| 최상위 / 장시간 agent | `claude-fable-5` | $10 / $50 | 1M | 2026.06.09 GA |
| 최고 성능 (복잡한 agentic 코딩) | `claude-opus-5` | $5 / $25 | 1M | 공식 권장 출발점 |
| 일상 균형 (권장) | `claude-sonnet-5` | $3 / $15 | 1M | 도입가 $2/$10 (~2026.08.31) |
| 경량 / 고속 | `claude-haiku-4-5-20251001` | $1 / $5 | 200k | 별칭 `claude-haiku-4-5` |

모든 현행 모델 최대 출력은 128k (Haiku 4.5는 64k).

**Legacy (아직 사용 가능하나 신규 채택 비권장)**
`claude-opus-4-8` / `claude-opus-4-7` / `claude-opus-4-6` /
`claude-sonnet-4-6` / `claude-sonnet-4-5-20250929` / `claude-opus-4-5-20251101`

---

## ❌ 사용 금지

| 모델 | 상태 |
|------|------|
| `claude-opus-4-1-20250805` | deprecated — **종료 2026.08.05** → `claude-opus-5` |
| `claude-opus-4-20250514`, `claude-sonnet-4-20250514` | **종료 완료 (2026.06.15)** |
| `claude-3-haiku-20240307` | 종료 완료 (2026.04.20) |
| `claude-3-7-sonnet-*`, `claude-3-5-haiku-*` | 종료 완료 (2026.02.19) |
| `claude-3-opus-*`, `claude-3-5-sonnet-*`, `claude-3-*` | 종료 완료 |
| `claude-2-*`, `claude-1-*`, `claude-instant-*` | 종료 |

---

## 주의사항

- Claude 5 패밀리: Fable 5 / Opus 5 / Sonnet 5 (+ Haiku 4.5)
- ⚠️ **extended thinking 미지원**: Fable 5 / Opus 5 / Sonnet 5는
  `thinking.type: "enabled"` 를 지원하지 않는다. 대신 **adaptive thinking**이 동작한다.
  `thinking` + `budget_tokens` 패턴은 `claude-haiku-4-5-20251001` 에서만 유효하다.
  (Fable 5는 adaptive thinking이 항상 켜져 있다.)
- ⚠️ **`temperature` / `top_p` / `top_k` deprecated** (Opus 4.7 이후 전 모델).
  기본값이 아닌 값을 넣으면 **400 오류**. 생략하고 프롬프트로 제어한다.
- `effort` 파라미터는 Opus 5 / Sonnet 5에서 Claude API 기준 기본값이 `high`다.
  다른 수준이 필요하면 명시적으로 지정한다.
- **모델 ID는 전부 pinned snapshot이다.** 4.6 세대부터 날짜 없는 형식(`claude-opus-5`)을
  쓰지만 이것도 evergreen 포인터가 아니라 고정 스냅샷이다.
- Batch API에서 `output-300k-2026-03-24` 베타 헤더로 최대 300k 출력 토큰 사용 가능
  (Opus 5 / 4.8 / 4.7 / 4.6, Sonnet 5 / 4.6).
- `claude-mythos-5` 는 초대 전용(Project Glasswing)이라 일반 코드에 넣지 않는다.
- 1M 토큰 컨텍스트: Max/Team/Enterprise 플랜에서만 사용 가능.
- Bedrock / Google Cloud는 모델 ID 체계와 종료 일정이 별도다
  (예: `anthropic.claude-haiku-4-5-20251001-v1:0`, `claude-haiku-4-5@20251001`).

---

## 예시 코드 (Python)

```python
import anthropic

client = anthropic.Anthropic()

# ✅ 현행 모델 — temperature/top_p/top_k 넣지 말 것 (400 오류)
response = client.messages.create(
    model="claude-sonnet-5",  # 일반 권장
    max_tokens=1024,
    messages=[{"role": "user", "content": "..."}]
)

# 최고 성능 필요 시
response = client.messages.create(
    model="claude-opus-5",
    max_tokens=2048,
    messages=[{"role": "user", "content": "..."}]
)

# extended thinking은 Haiku 4.5에서만 유효
response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=2048,
    thinking={"type": "enabled", "budget_tokens": 1024},
    messages=[{"role": "user", "content": "..."}]
)

# ❌ 사용 금지
# model="claude-opus-4-1-20250805"    # 2026.08.05 종료
# model="claude-3-5-sonnet-20241022"  # 종료 완료
# thinking={"type": "enabled", ...} 를 claude-opus-5 / sonnet-5 에 사용  ← 미지원
# temperature=0.7 을 Opus 4.7 이후 모델에 사용                          ← 400 오류
```

> 마지막 업데이트: 2026.07.28
