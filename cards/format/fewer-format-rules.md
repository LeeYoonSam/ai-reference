---
id: fewer-format-rules
title: 포맷 규칙은 적을수록 지켜진다. 기본값에서 벗어나게 하는 규칙만 남긴다
type: principle
scope: both
tags: [format, instruction, context]
source_note: research/2026-10-30_답변-포맷/report.md
source_url: "https://arxiv.org/html/2310.20410"
author: Jiang 외 (FollowBench), Pyatkin 외 (IFBench), Thariq Shihipar (Anthropic)
tier: T1
source_date: 2025-07-03
valid_as_of: 2026-10-30
model_context: Claude Fable 5.1, Claude Code v2.1
half_life: long
review_by: 2027-10-30
status: active
superseded_by:
---
## 원칙

사용자는 포맷 규칙의 수를 줄인다. 지시 준수율은 규칙 수에 따라 떨어진다. 제약이 1개에서 5개로 늘면 동시 준수율은 50~62% 로 내려간다. 규칙 500개에서는 최고 모델도 68% 만 지킨다. 그래서 모델이 이미 하는 것을 규칙으로 쓰지 않는다. 남길 규칙은 모델 기본값에서 벗어나게 하는 것만이다. 하나의 금지 대신 기준을 준다. "불릿 금지" 대신 "내용이 다면적일 때 불릿을 쓴다" 가 기준형 규칙이다.

## 언제 쓰나

- CLAUDE.md 의 포맷 규칙이 10개를 넘을 때 쓴다. 기본값과 같은 규칙을 지운다.
- 규칙을 더했는데 다른 규칙이 깨질 때 쓴다. 총량이 원인이다.
- 긴 세션에서 규칙 준수가 흐려질 때 쓴다. 파일 구조보다 지시 총량과 세션 길이가 준수율을 좌우한다.
- 금지 규칙을 쓸 때 쓴다. 기준과 이유로 바꾼다.

## 프롬프트 문장

```text
CLAUDE.md 의 포맷 규칙을 하나씩 검사해 줘. 규칙마다 3가지를 답해 줘.
1) 규칙을 빼도 지금 모델이 같은 결과를 내는가.
2) 금지형이면 기준형으로 어떻게 바꾸는가.
3) 다른 규칙과 겹치거나 충돌하는가.
빼도 되는 규칙 목록과 바꾼 문장을 표로 보여 줘.
```

## 근거

- FollowBench 에서 제약을 1개에서 5개로 늘리면 GPT-4 의 전체 HSR 은 84.7% 에서 61.9% 로, GPT-3.5 의 Format HSR 은 90.0% 에서 50.0% 로 떨어졌다. [FollowBench](https://arxiv.org/html/2310.20410)
- IFBench 는 새 제약 유형에서 같은 모델이 50포인트 이상 낮게 나오고, GPT-4.1 과 Claude 4 Sonnet 도 "below 50%" 라고 보고했다. NeurIPS 2025 논문이다. [IFBench](https://arxiv.org/abs/2507.02833)
- IFScale 은 지시 500개에서 최고 모델도 68% 정확도이고 "bias towards earlier instructions" 를 보인다고 적었다. [IFScale](https://arxiv.org/abs/2507.11538)
- McMillan 의 요인 실험은 CLAUDE.md 의 크기, 위치, 구조, 모순 4변수가 준수율에 유의한 영향이 없다고 보고했다. 대신 세션 안에서 함수를 1개 더 만들 때마다 준수 확률이 약 5.6% 낮아졌다. [McMillan 2026](https://arxiv.org/abs/2605.10039)
- Thariq Shihipar 는 Claude Code 시스템 프롬프트의 80% 이상을 지웠고 코딩 평가 손실이 없었다고 밝혔다. 핵심 전환은 "Then: Give Claude rules / Now: Let Claude use judgement" 다. 사례로 "Never write multi-paragraph docstrings" 를 "Write code that reads like the surrounding code: match its comment density, naming, and idiom." 으로 바꿨다. [claude.dev 블로그](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/)
- Thariq 는 "a rule that's right 90% of the time is wrong the other 10%" 라고 쓰고, 대부분의 CLAUDE.md 가 "still walls of hard rules and banned phrases" 라고 지적했다. 이 인용은 X 원문을 2차 사이트로 확인했다. [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)
- OpenAI Model Spec 도 같은 방향이다. 2025-02-12 판의 구체 포맷 절이 2026-10-29 판에서 사라지고 일반 원칙으로 줄었다. [Model Spec 2026-10-29](https://model-spec.openai.com/2026-10-29.html)
- 충돌: 실무자 일부는 구체 규칙을 더하라고 한다. "Be concise" 대신 "3문장 이하" 같은 이진 규칙이 지켜진다는 보고다. 두 입장은 양립한다. 남기는 규칙은 적게, 남긴 규칙은 검증 가능하게 쓴다. [dev.to Peter Huang](https://dev.to/peterverse180/writing-a-claudemd-that-claude-actually-follows-4llo)
- 주의: Claude 4.x 와 5.x 의 IFEval·IFBench 공식 수치는 1차 출처에 없다.
- 관련 카드: `positive-format-instructions`, `check-model-default-before-format-rules`, `feedback-to-rules`.
