# 카드 목록

Claude 는 이 파일을 가장 먼저 읽는다. 카드마다 1줄이다. 형식은 `DESIGN.md` 9.3절이다.

## 맡기는 방식

- [맡기기 전에 깊이 프롬프트의 4가지 질문을 먼저 묻는다](cards/delegation/deeper-not-bigger.md): 작업을 맡기기 직전에 Claude 가 4가지 질문에 답하고 프롬프트 전체를 더 깊게 다시 쓴다. · prompt · delegation, depth, prompt · review_by 2027-10-29
- [작업을 하나씩 집어 주지 말고 목표로 맡긴다](cards/delegation/delegate-goal-not-task.md): 사용자는 개별 작업 대신 결과를 목표로 준다. Claude 가 우선순위를 스스로 판단한다. 목표가 모델의 한계에 닿으면, 사용자는 다음 세대 모델에서 다시 시도한다. · principle · delegation, altitude, goal · review_by 2027-10-29
- [과제를 명사가 아니라 동사로 다시 정의하고 다른 분야의 방법을 끌어온다](cards/delegation/nouns-to-verbs.md): 사용자는 결과물 이름 대신 결과물이 하는 일로 과제를 다시 정의한다. 그다음 사용자는 그 일을 잘하는 분야의 실제 방법을 적용하게 한다. · pattern · delegation, range · review_by 2027-10-29
- [역할을 씌우면 말투만 바뀐다. 전문가의 방법과 도구를 쓰게 한다](cards/delegation/role-sentence-roleplay-trap.md): 사용자는 역할 문장 대신 Claude 에게 최고 전문가의 방법과 도구를 먼저 말하게 한다. 그다음 Claude 가 그 방법과 도구를 실제로 쓴다. · anti-pattern · delegation, role-prompt, depth · review_by 2027-01-29
- [목표는 일부러 터무니없이 높게 잡고 해 볼 만하다고 말해 준다](cards/delegation/set-absurd-goal.md): 사용자는 필요한 값보다 훨씬 높은 목표를 준다. 예: 10초를 5초로 줄여야 하면 0.2초를 요구한다. 그리고 그 목표가 해 볼 만하다고 말한다. · pattern · delegation, depth, goal · review_by 2027-01-29

## 검증과 리뷰

- [적대적 리뷰 여러 개를 돌리고 판사 Claude 가 타당한 비판만 거른다](cards/verification/adversarial-review-with-judge.md): 리뷰 스레드 여러 개가 결과물이 틀렸다는 것을 증명한다. 판사 Claude 가 타당한 비판만 걸러 만든 Claude 에게 넘긴다. · pattern · verification, review, adversarial-review · review_by 2027-10-29
- [팩트 체크는 1차 자료를 찾고 그 자료의 신뢰성까지 확인하게 한다](cards/verification/fact-check-primary-sources.md): 사용자는 스레드 1개에 모든 수치의 1차 자료를 찾게 한다. 그 스레드가 자료의 신뢰성도 판정한다. · prompt · verification, fact-check, prompt · review_by 2027-10-29
- [만든 세션이 아니라 바깥에서 채점한다](cards/verification/grade-outside-session.md): 사용자는 작업한 세션에게 채점을 맡기지 않는다. 검증은 외부 지표나 다른 세션으로 한다. 펠릭스의 블로그는 이 한계가 모델 지능과 함께 풀릴 수 있다고 본다. · principle · verification, review · review_by 2027-10-29
- [넘기기 불안하면 내 피드백과 Claude 의 피드백을 나란히 비교한다](cards/verification/side-by-side-with-claude.md): 사용자는 2개 메시지로 Claude 의 독립 피드백을 먼저 받는다. 그다음 사용자는 자기 피드백과 비교해 차이를 규칙으로 만든다. · pattern · verification, review, delegation · review_by 2027-10-29

## 컨텍스트, skill, 작업 이어 가기

- [작업 정리 문서와 다음 프롬프트로 세션을 이어 간다](cards/context/end-of-day-handoff-doc.md): 하루 작업을 끝낼 때 Claude 에게 논의 내용을 문서로 정리하게 한다. 다음 세션 첫 프롬프트까지 쓰게 하고 다음 날 그것으로 재개한다. 상위 세션이 cards/context/ 로 옮겨야 한다. · pattern · context, delegation · review_by 2027-01-29
- [내가 준 피드백을 모아 규칙 목록으로 바꾸고 리뷰 입력으로 쓴다](cards/context/feedback-to-rules.md): Claude 가 사용자의 피드백을 모은다. 그다음 Claude 가 피드백을 규칙과 숨은 원칙 목록으로 줄인다. 사용자는 그 목록을 이후 리뷰의 입력 자료로 쓴다. · pattern · context, feedback, review · review_by 2027-10-29
- [골라 준 요약 대신 원본 데이터와 컴퓨터를 열어 준다](cards/context/open-raw-data-and-computer.md): 사용자는 요약 대신 원본 데이터, 직접 쓸 컴퓨터, 데이터를 가져오는 도구를 준다. 사용자는 각 도구가 가져오는 데이터를 설명한다. · principle · context, raw-data, tools · review_by 2027-10-29
- [스킬은 금방 낡는다. 스킬 없는 기본 프롬프트와 비교한다](cards/context/skill-half-life-try-plain-prompt.md): 사용자는 스킬을 쓴 결과와 기본 프롬프트 결과를 함께 만든다. Claude 는 두 결과의 차이 목록만 만든다. 어느 쪽이 나은지는 사용자가 판단한다. · principle · context, skills, model-upgrade · review_by 2027-01-29

## HR 업무 자동화 사례

- [조직 목표와 개인 이력을 함께 주고 목표 후보를 제안받는다](cards/hr-automation/context-based-goal-suggestion.md): 조직 OKR, 리더 미션, 지난 반기 미션, 직무를 함께 주고 목표 후보와 지표를 제안받는다. 사람은 '왜 이 목표인가' 대화에 시간을 쓴다. 원티드 사례에서 리더 점검 기간이 약 7일에서 1.5일로 줄었다. · case · hr-automation, context, performance · review_by 2027-10-29
- [설문 폼을 공감하고 이어 묻는 대화로 바꾼다](cards/hr-automation/conversational-survey.md): 폼 설문 대신 AI 가 질문하고 공감하며 이어 묻는다. 대화가 끝나면 리포트로 요약한다. 원티드 온보딩 피드백 챗봇 사례에서 답이 길고 솔직해졌다. · case · hr-automation, survey · review_by 2027-10-29
- [AI 가 전 건을 판정하고 사람은 확인 필요 건만 본다](cards/hr-automation/exception-based-review.md): AI 가 증빙을 전 건 대조해 자동 확정과 확인 필요로 나누고 사유와 재확인 메시지 초안을 붙인다. 사람은 확인 필요 건만 본다. 원티드 성장지원비 사례에서 수동 검토가 8건으로 줄었다. · case · hr-automation, verification, review · review_by 2027-10-29
- [원천 파일을 올리면 계산과 브리핑을 한 번에 받는다](cards/hr-automation/upload-then-briefing.md): 도구가 원천 파일로 지표를 계산하고 AI 가 전월 대비 변화를 브리핑한다. 사람의 관심은 수식 검증에서 조직 관리 해석으로 옮겨 간다. 원티드 근태 대시보드 사례에서 2~3시간이 1~2분으로 줄었다. · case · hr-automation, reporting · review_by 2027-10-29
