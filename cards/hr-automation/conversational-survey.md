---
id: conversational-survey
title: 설문 폼을 공감하고 이어 묻는 대화로 바꾼다
type: case
scope: both
tags: [hr-automation, survey]
source_note: notes/2026-10-28_wanted_hr-ai-agent-ep03.md
source_url: "https://www.youtube.com/watch?v=IrK71LslbFQ&t=319s"
author: 김서희 (원티드 피플팀)
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

설문 폼 대신 AI 가 질문한다. AI 는 답에 공감하고 다음 질문으로 이어 간다. 대화가 끝나면 AI 가 대화를 리포트로 요약한다.

## 언제 쓰나

- 폼 설문의 답이 짧고 형식적일 때 쓴다. 예: 온보딩 피드백, 퇴사 인터뷰, 교육 만족도, 펄스 서베이.
- 점수보다 솔직한 서술이 더 필요할 때 쓴다.
- 응답을 사람이 한 건씩 읽기 어려워서 요약 리포트가 필요할 때 쓴다.

## 프롬프트 문장

```text
입사 3개월차 구성원의 온보딩 경험을 듣는 대화형 설문 챗봇을 만들어 줘.
지금은 구글 폼으로 받는데 답이 짧고 형식적이다. 목표는 구성원이 편하게, 길게, 솔직하게 말하게 하는 것이다.
기존 설문 문항: [경로]. 이 문항들이 다루는 주제는 모두 대화에서 다뤄야 한다.
챗봇은 답을 들으면 짧게 공감하고, 그 답에 맞춘 다음 질문으로 넘어간다.
대화가 끝나면 응답자별 리포트를 만든다. 리포트에는 3개월 경험 요약, 온보딩 만족도, 개선이 필요한 부분이 들어간다.
완성되면 성향이 다른 가상 응답자 3명으로 대화를 돌려 봐. 기존 문항의 주제가 모두 다뤄졌는지 표로 보여 줘.
```

## 근거

- 대상: 입사 약 3개월 된 신규 입사자가 AI 와 대화로 온보딩 경험을 말한다. [▶ 04:43](https://www.youtube.com/watch?v=IrK71LslbFQ&t=283s)
- 이전 방식: 구글 폼 설문을 받았다. 답은 형식적이었고 솔직하다는 느낌이 부족했다. [▶ 04:55](https://www.youtube.com/watch?v=IrK71LslbFQ&t=295s)
- 사내 AI 해커톤에서 아이디어가 나왔다. 개발자가 만들었고, 피플팀이 도입해서 운영한다. [▶ 05:07](https://www.youtube.com/watch?v=IrK71LslbFQ&t=307s)
- 구성원이 답하면 챗봇이 공감하고 다음 질문으로 넘어간다. [▶ 05:19](https://www.youtube.com/watch?v=IrK71LslbFQ&t=319s)
- 효과: 폼의 단답식 답이 길고 편한 답으로 바뀌었다. 반말로 답한 구성원도 있었다. [▶ 05:33](https://www.youtube.com/watch?v=IrK71LslbFQ&t=333s)
- 대화가 끝나면 챗봇이 대화를 바탕으로 리포트를 쓴다. 챗봇은 만족도와 개선이 필요한 부분도 받는다. [▶ 05:54](https://www.youtube.com/watch?v=IrK71LslbFQ&t=354s), [▶ 06:02](https://www.youtube.com/watch?v=IrK71LslbFQ&t=362s)
- 도구: 영상은 이 챗봇이 쓴 모델을 밝히지 않는다. `model_context` 는 이 카드의 프롬프트를 쓴 기준 시점의 모델이다.
- 등급: 발표자가 자기 업무를 직접 말한 1차 발언이므로 tier 를 T2 로 둔다. DESIGN.md 12.2절은 이 채널을 T3 로 분류하므로, 이 판단은 예외다.
- 주의: 발표자는 원티드 직원이고, 영상은 원티드 채널의 기획 시리즈다. 따라서 발표자는 독립 실무자가 아니다.
- 주의: 프롬프트 마지막 줄의 가상 응답자 3명 시험은 영상에 없다. 이 카드가 더한 검증 방법이다.
- 주의: 효과는 담당자의 체감이다. 영상은 응답 길이나 응답률 수치를 내지 않는다. 화면 속 데이터 중 일부는 영상에서 "가상 데이터" 로 표시되어 있다.
- 주의: 이 챗봇은 개발자가 만들었다. 같은 발표자의 성장지원비 서비스와 달리, 비개발자가 직접 만든 사례가 아니다.
