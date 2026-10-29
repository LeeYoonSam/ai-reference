---
id: end-of-day-handoff-doc
title: 작업 정리 문서와 다음 프롬프트로 세션을 이어 간다
type: pattern
scope: agent-task
tags: [context, delegation]
source_note: notes/2026-10-28_wanted_hr-ai-agent-ep03.md
source_url: "https://www.youtube.com/watch?v=IrK71LslbFQ&t=974s"
author: 장진희 (원티드 피플팀)
tier: T2
source_date: 2026-10-28
valid_as_of: 2026-10-29
model_context: Claude Opus 5.5, Claude Code v2.1
half_life: short
review_by: 2027-01-29
status: active
superseded_by:
---
## 원칙

하루 작업을 끝낼 때 Claude 에게 논의 내용을 문서로 정리하게 한다. 같은 문서를 바탕으로 다음 세션의 첫 프롬프트까지 쓰게 한다. 다음 날에는 그 문서와 프롬프트로 작업을 재개한다. 사람도 AI 도 맥락을 잊기 때문이다.

## 언제 쓰나

- 여러 날에 걸쳐 Claude Code 로 서비스를 만들 때 쓴다.
- 문서 없이 요청만 이어 가다가 결과의 일관성이 흔들릴 때 쓴다.
- 오늘 세션을 닫고 내일 새 세션에서 이어 가야 할 때 쓴다.

## 프롬프트 문장

```text
오늘 작업을 여기서 멈춘다. 내일은 이 대화 없이 새 세션에서 이어 간다. 너도 나도 오늘 맥락을 잊는다.
지금까지 논의한 내용을 작업 정리.md 로 정리해 줘. 내일 세션이 이 문서만 읽고 작업을 재개할 수 있어야 한다.
문서 끝에 내일 세션에 그대로 붙여 넣을 첫 프롬프트를 써 줘.
다 쓰면, 문서에 적은 파일 경로가 실제로 있는지 확인해 줘. 없는 경로는 고쳐 줘.
```

## 근거

- 발표자는 처음에 문서 작업 없이 Claude 에게 요청만 계속했다. [▶ 16:14](https://www.youtube.com/watch?v=IrK71LslbFQ&t=974s)
- 발표자는 문서로 정리해서 Claude 에게 줘야 일관성을 잃지 않는다고 느꼈다. 발표자는 자신도 Claude 도 잊는다고 말했다. [▶ 16:20](https://www.youtube.com/watch?v=IrK71LslbFQ&t=980s)
- 하루 업무를 끝낼 때 논의 내용을 문서로 정리하게 한다. 그 문서를 바탕으로 다음 작업을 이어 갈 프롬프트까지 쓰게 하고 하루를 끝낸다. [▶ 16:26](https://www.youtube.com/watch?v=IrK71LslbFQ&t=986s), [▶ 16:33](https://www.youtube.com/watch?v=IrK71LslbFQ&t=993s)
- 이 팁은 성과관리 에이전트를 Claude Code 로 바이브 코딩한 경험에서 나왔다. [▶ 15:54](https://www.youtube.com/watch?v=IrK71LslbFQ&t=954s)
- 도구: 발표자는 Claude Code 를 썼다. 영상은 모델과 버전을 밝히지 않는다. `model_context` 는 이 카드의 프롬프트를 쓴 기준 시점의 모델이다.
- 유형: 이 카드는 type 을 pattern 으로 둔다. 발표자가 특정 서비스가 아니라 작업 습관 일반을 권했기 때문이다.
- 등급: 발표자가 자기 경험을 직접 말한 1차 발언이므로 tier 를 T2 로 둔다. DESIGN.md 12.2절은 이 채널을 T3 로 분류하므로, 이 판단은 예외다.
- 주의: 발표자는 원티드 직원이고, 영상은 원티드 채널의 기획 시리즈다. 따라서 발표자는 독립 실무자가 아니다.
- 주의: 프롬프트 마지막 줄의 파일 경로 확인은 영상에 없다. 이 카드가 더한 검증 방법이다.
- 주의: 요약 노트의 5항목 종료 프롬프트는 발표자의 말이 아니다. 그 프롬프트는 요약 노트 작성자가 제안한 템플릿이다. 발표자가 밝힌 것은 문서 정리와 다음 프롬프트 작성의 2단계뿐이다.
- 주의: 이 카드는 모델이 세션 사이 맥락을 잃는다는 전제에 기댄다. Claude Code 에 세션 기억 기능이 늘면, 사용자는 이 카드를 기본 프롬프트와 비교해 재검토한다.
