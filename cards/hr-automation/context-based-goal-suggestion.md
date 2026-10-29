---
id: context-based-goal-suggestion
title: 조직 목표와 개인 이력을 함께 주고 목표 후보를 제안받는다
type: case
scope: both
tags: [hr-automation, context, performance]
source_note: notes/2026-10-28_wanted_hr-ai-agent-ep03.md
source_url: "https://www.youtube.com/watch?v=IrK71LslbFQ&t=869s"
author: 장진희 (원티드 피플팀)
tier: T2
source_date: 2026-10-28
valid_as_of: 2026-10-29
model_context: Claude Opus 5.5, Claude Code v2.1
half_life: medium
review_by: 2027-10-29
status: active
superseded_by:
---
## 원칙

AI 에게 조직 OKR, 리더의 미션, 본인의 지난 반기 미션, 직무·역할·소속 조직을 함께 준다. AI 는 이 맥락으로 목표 후보와 측정 지표를 제안한다. 사람은 양식 채우기 대신 "왜 이 목표인가" 를 이야기하는 데 시간을 쓴다.

## 언제 쓰나

- 목표 수립이 양식 제출로, 평가가 달성 여부 확인으로 끝날 때 쓴다.
- 전사 목표와 개인 목표의 정렬을 점검해야 할 때 쓴다.
- 비슷한 구조의 추천 업무에도 쓴다. 예: 교육 과정 추천, 개인 개발 계획 작성, 면접 질문 생성.
- 성과 데이터를 다루므로, 사용자는 먼저 데이터를 올릴 곳이 사내 보안 기준을 통과했는지 확인한다.

## 프롬프트 문장

```text
[구성원] 의 이번 반기 목표 후보를 제안해 줘.
목표는 양식 채우기 부담을 줄이고, 리더와 구성원이 "왜 이 목표인가" 를 이야기하는 데 시간을 쓰게 하는 것이다.
입력: 조직 OKR [경로], 리더의 미션 [경로], 이 구성원이 지난 반기에 완료한 미션 [경로], 직무·역할·소속 조직 [경로].
후보 3개를 내고, 후보마다 세부 목표와 측정 지표를 붙여 줘.
후보마다 어느 조직 OKR 과 리더 미션에 연결되는지 원천 문장을 인용해 줘. 연결되는 문장이 없으면 없다고 적어 줘.
```

## 근거

- 이전 문제: 목표 수립과 평가는 잘 된다. 그러나 그 사이에 방향을 스스로 점검하는 대화가 부족했다. 수립 시즌에는 양식 제출이, 평가 시즌에는 달성 여부 확인이 목적이 됐다. [▶ 13:26](https://www.youtube.com/watch?v=IrK71LslbFQ&t=806s)
- 발표자는 운영 부담을 줄이고 목표 중심의 의미 있는 소통을 늘리려고 에이전트를 만들었다. [▶ 14:03](https://www.youtube.com/watch?v=IrK71LslbFQ&t=843s)
- 목표 수립 화면은 소속 조직의 OKR, 리더의 미션, 본인이 지난 반기에 가져간 미션을 함께 보여 준다. [▶ 14:29](https://www.youtube.com/watch?v=IrK71LslbFQ&t=869s)
- AI 는 로그인한 계정의 직무·역할·조직을 종합해 목표를 제안한다. 시연 계정은 채용 직무였다. [▶ 14:44](https://www.youtube.com/watch?v=IrK71LslbFQ&t=884s)
- 후보 1개를 고르면 AI 가 세부 목표와 지표까지 도출한다. [▶ 14:58](https://www.youtube.com/watch?v=IrK71LslbFQ&t=898s)
- 효과: 대부분의 구성원이 하루 만에 목표를 작성했다. 리더의 목표 점검 기간은 도입 전 거의 일주일에서 1.5일로 줄었다. 영상 표기는 약 7일 → 1.5일이다. [▶ 15:17](https://www.youtube.com/watch?v=IrK71LslbFQ&t=917s), [▶ 15:32](https://www.youtube.com/watch?v=IrK71LslbFQ&t=932s)
- 보안: 회사 성과 데이터는 검증되지 않은 시스템에 올리지 않는다. 원티드는 사내 서비스 엔노이아에 데이터를 넣었다. 개발은 Claude Code 로 바이브 코딩했다. [▶ 15:39](https://www.youtube.com/watch?v=IrK71LslbFQ&t=939s)
- 도구: 영상의 서비스는 사내 LLM 엔노이아와 Claude Code 로 만들었다. `model_context` 는 이 카드의 프롬프트를 쓴 기준 시점의 모델이다.
- 등급: 발표자가 자기 업무를 직접 말한 1차 발언이므로 tier 를 T2 로 둔다. DESIGN.md 12.2절은 이 채널을 T3 로 분류하므로, 이 판단은 예외다.
- 주의: 발표자는 원티드 직원이고, 영상은 원티드 채널의 기획 시리즈다. 따라서 발표자는 독립 실무자가 아니다.
- 주의: 프롬프트 마지막 줄의 원천 문장 인용은 영상에 없다. 이 카드가 더한 검증 방법이다.
- 주의: 화면 속 데이터 중 일부는 영상에서 "가상 데이터" 로 표시되어 있다. 요약 노트는 화면 표기 "5.5일 절감, 리소스 약 56% 감축" 도 옮긴다. 56% 는 7일 → 1.5일과 계산이 맞지 않는다. 그래서 이 카드는 56% 를 쓰지 않는다.
