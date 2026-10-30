---
id: readability-over-brevity
title: 가독성이 간결함보다 앞선다. 짧게 쓰는 방법은 내용 선택이다
type: principle
scope: agent-task
tags: [format, readability, length]
source_note: research/2026-10-30_답변-포맷/report.md
source_url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5#readability-when-communicating-with-the-user"
author: Anthropic (Developer Platform 문서)
tier: T1
source_date: 2026-09-01
valid_as_of: 2026-10-30
model_context: Claude Fable 5.1, Claude Code v2.1
half_life: medium
review_by: 2027-10-30
status: active
superseded_by:
---
## 원칙

Claude 는 답변을 짧게 쓸 때 내용을 고른다. 문장을 조각, 화살표, 약어로 압축하지 않는다. 압축된 문장은 글자 수를 줄이지만 독자의 일을 늘린다. 완전한 문장이 기준이다. 최종 보고는 작업을 보지 않은 독자가 읽는다. 그래서 Claude 는 작업 중에 쓴 메모 문체를 버리고 완전한 문장으로 다시 쓴다.

## 언제 쓰나

- "간결하게" 라는 지시를 받았을 때 쓴다. 간결은 내용을 빼는 것이다. 문장을 부수는 것이 아니다.
- 답변에 화살표, 콜론만 붙은 라벨, 문장 조각이 보일 때 쓴다.
- 긴 작업 뒤 최종 보고를 쓸 때 쓴다. 독자는 중간 과정을 보지 않았다.
- 사용자 지침에 짧은 문장 규칙이 있을 때 함께 쓴다. 짧은 문장은 완전한 문장이어야 한다.

## 프롬프트 문장

```text
완전한 문장으로 써 줘. 화살표, 라벨 뒤 콜론, 문장 조각으로 압축하지 말아 줘.
짧게 쓸 때는 덜 중요한 내용을 빼 줘. 문장을 부수지 말아 줘.
최종 보고는 작업 과정을 보지 않은 사람이 읽는다고 생각하고 다시 써 줘.
```

## 근거

- Anthropic 의 Fable 5 가이드는 "Being readable and being concise are different things, and readability matters more" 라고 쓴다. 짧게 쓰는 방법은 내용 선택이고 문장 압축이 아니라고 설명한다. [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5#readability-when-communicating-with-the-user)
- 같은 가이드는 최종 요약을 작업을 보지 않은 독자를 위해 완전한 문장으로 다시 쓰라고 권한다. [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5#readability-when-communicating-with-the-user)
- Claude 의 헌법은 길이를 "Response length should be calibrated to the complexity and nature of the request" 로 둔다. 짧음 자체가 목표가 아니다. [Claude's constitution](https://www.anthropic.com/constitution)
- Friedman 외 연구는 틀린 LLM 설명을 24명에게 보였다. 중간 길이 설명에서 오류 발견율이 짧거나 긴 설명보다 높았다. 오류를 검증할 근거를 남길 만큼의 길이가 필요하다. [Not Too Short, Not Too Long](https://arxiv.org/abs/2603.06878)
- Shreya Shankar 는 "Empty summary sentences feel conclusive, but say nothing" 을 지적한다. 길이는 기여에 비례해야 한다. [sh-reya.com](https://www.sh-reya.com/blog/ai-writing)
- 주의: Friedman 외 연구는 피험자 24명의 소규모 실험이다. 보조 근거로만 쓴다.
- 주의: 이 원칙의 원문은 Fable 5 세대 가이드에 있다. 모델 세대마다 장황함 기본값이 바뀌므로 half_life 는 medium 이다. `check-model-default-before-format-rules` 카드를 함께 본다.
- 관련 카드: `lead-with-outcome`, `agent-report-outcome-first`.
