# 출처 4갈래가 "결론 먼저, 포맷은 조건부" 로 수렴한다

Anthropic 공식 지침, 기술 문서 표준, 실증 연구, 실무자·타 벤더 자료는 AI 답변 포맷에서 3가지에 합의한다. 첫 문장에 결론을 쓴다. 길이는 요청의 복잡도에 맞춘다. 마크다운과 불릿은 내용이 다면적일 때만 쓴다. Anthropic 의 공개 규칙은 2024년 "불릿 금지" 에서 2026년 9월 "다면적일 때 허용" 으로 완화됐고, 모델 세대마다 장황함과 포맷 기본값이 반대로 움직여서 고정 규칙은 모델 교체 시 역효과를 낸다 ([Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#formatting-in-chat)). 실증 연구는 LLM 판정자의 길이 편향과 마크다운 선호 편향을 크게 측정했지만, 사람의 마크다운 선호는 약 57% 에 그친다 ([Judging the Judges](https://arxiv.org/html/2604.23178)). 산문과 불릿의 이해도를 직접 비교한 통제 실험은 1건뿐이다. 사용자의 ASD-STE100 기반 문장 규칙은 GOV.UK, Google, Microsoft, 미국 연방 지침과 대부분 일치한다. 충돌 지점은 3곳이다. 불릿의 허용 범위, 규칙 수의 적정선, 통제 언어의 적용 범위다. 포맷을 Claude 에게 지시하는 방법은 4가지로 정리된다. 긍정형으로 쓴다. 검증 가능한 수치로 쓴다. 모델별 기본값을 확인한 뒤 보정한다. 규칙 수를 줄인다.

## Anthropic 은 2년 동안 "금지" 에서 "조건부 허용" 으로 이동했다

claude.ai 공개 시스템 프롬프트의 포맷 규칙은 5단계로 변했다. 2024년 9월 Sonnet 3.5 는 간결함과 필러 금지를 기본값으로 뒀다. 같은 해 10월 판은 **"Claude should not use bullet points or numbered lists unless the human explicitly asks for a list"** 라는 강한 금지 규칙을 더했다 ([Claude Sonnet 3.5 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-sonnet-3-5)). 2025년 2월 Sonnet 3.7 은 "Claude provides the shortest answer it can" 과 추천은 1개만 제시하라는 규칙을 뒀다 ([Claude Sonnet 3.7 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-sonnet-3-7)). 2026년 2월 Opus 4.6 은 보고서·설명문을 산문으로 쓰고 불릿은 1~2문장 이상으로 쓰라고 명시했다 ([Claude Opus 4.6 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-4-6)). 2026년 9월 1일 Fable 5.1 판은 이 금지를 풀었다. 원문은 **"Claude uses lists and bullet points when asked to or when the content is multifaceted enough that they help with clarity"** 다 ([Claude Fable 5.1 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1)). 같은 판은 "Claude balances the need to give a dense comprehensive answer with the person's need to be able to quickly scan and understand the most important part of the response" 라고 적는다. 보고서를 산문으로 쓰라는 문장은 이 판에서 사라졌다.

2년 내내 유지된 규칙은 2개다. 친밀한 대화나 감정적 대화에서는 포맷을 쓰지 않는다. 거절할 때는 불릿을 쓰지 않는다. Fable 5.1 판은 그 이유를 적는다. "any kind of formatting lends a more formal and professional tone to the conversation" 이다 ([Claude Fable 5.1 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1)). 새로 더해진 규칙은 도구 호출 뒤 답변 의무다. **"After its last tool call in a turn, Claude states the answer the person asked for in one or two sentences; a sign-off alone, such as "Done.", is not a reply."** 이 문장은 에이전트 작업 보고의 최소 형식을 정한다.

### 모델 세대마다 장황함 기본값이 반대로 움직인다

완화의 원인은 모델 변화다. 개발자 문서는 Opus 5 를 "its default user-facing responses run longer than prior models'" 로, Fable 5.1 을 "it uses bold less and is less likely to reach for headers, lists, or quotation marks" 로 설명한다 ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#communication-style-and-verbosity)). Anthropic 은 Fable 5.1 에서 anti-formatting 규칙을 지우라고 권한다. 원문은 **"If your prompt contains anti-formatting language, remove it or replace it with a rule that says when specific formatting is appropriate"** 다 ([Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#formatting-in-chat)). Thariq Shihipar 는 2026년 7월 Claude Code 시스템 프롬프트의 80% 이상을 지웠고 코딩 평가 손실이 없었다고 밝혔다 ([claude.dev 블로그](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/)). 이 글의 핵심 전환은 "Then: Give Claude rules / Now: Let Claude use judgement" 다. 다만 이 글에는 응답 포맷에 관한 문장이 없다.

### 결론 먼저와 가독성 우선은 세대를 넘어 반복된다

포맷 규칙이 바뀌는 동안 2개 원칙은 Fable 5, Opus 5, Claude Code 문서에 같은 문장으로 반복된다. 첫째는 결론 먼저다. Fable 5 가이드의 샘플은 **"Lead with the outcome. Your first sentence after finishing should answer "what happened" or "what did you find""** 다 ([Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5#strong-instruction-following)). Claude Code 의 Concise output style 도 "the first sentence of a response states what happened or what the answer is" 로 설명된다 ([Output styles](https://code.claude.com/docs/en/output-styles)). 둘째는 가독성이 간결함보다 앞선다는 원칙이다. 같은 Fable 5 가이드는 **"Being readable and being concise are different things, and readability matters more"** 라고 적는다. 짧게 쓰는 방법은 내용을 고르는 것이고, 문장을 조각이나 화살표 연쇄로 압축하는 것이 아니다. 최종 요약은 작업을 보지 않은 독자를 위해 완전한 문장으로 다시 쓴다 ([Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5#readability-when-communicating-with-the-user)).

헌법은 이 규칙들의 상위 기본값을 정한다. 마크다운은 "using Markdown only if Markdown is likely to be rendered" 로, 길이는 "Response length should be calibrated to the complexity and nature of the request" 로 적는다 ([Claude's constitution](https://www.anthropic.com/constitution)). 헌법은 "excessive warnings, disclaimers, or caveats" 와 "unnecessarily preachy, sanctimonious, or paternalistic" 응답을 나쁜 응답으로 열거한다. Anthropic 체계에서 포맷 규칙의 우선순위는 사용자 지시, 운영자 지시, 헌법 기본값 순이다. 마크다운을 렌더링 여부로 판단하라는 공개 1차 출처는 헌법 1곳이다.

## 글쓰기 표준은 짧은 문장과 결론 먼저에서 사용자 규칙과 일치한다

ASD-STE100 Issue 9 는 2025년 1월 15일에 나왔다. 규칙은 53개이고 새 규칙은 없다 ([tcworld](https://www.tcworld.info/news/asd-ste100-issue-9-setting-a-standard-for-technical-documentation)). 공개 출처가 확인하는 수치 규칙은 절차 문장 20단어, 설명 문장 25단어, 단락 6문장이다 ([Wikipedia Simplified Technical English](https://en.wikipedia.org/wiki/Simplified_Technical_English)). 어휘 원칙은 "One word, one part of speech, one meaning" 이다. 다른 표준의 수치는 이보다 느슨하다. GOV.UK 는 **"Try to split up sentences that are over 25 words long"** 과 단락 5문장을 둔다 ([GOV.UK Use clear language](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/)). 미국 연방 지침은 수치 없이 "Express only one idea in each sentence" 를 둔다 ([plainlanguage.gov 보관본](https://raw.githubusercontent.com/GSA/plainlanguage.gov/main/_pages/guidelines/concise/write-short-sentences.md)). Microsoft 는 단락을 "Three to seven lines" 로 둔다 ([Microsoft Scannable content](https://learn.microsoft.com/en-us/style-guide/scannable-content/)). 수치의 강도는 ASD-STE100, GOV.UK, Microsoft, 미국 연방 순으로 약해진다.

결론 먼저는 출처가 다른 4개 전통이 수렴하는 규칙이다. NN/g 의 역피라미드는 "The story should start with the main point" 다 ([NN/g Inverted Pyramid](https://www.nngroup.com/articles/inverted-pyramid/)). 미 육군 규정 AR 25-50 의 BLUF, Minto 피라미드의 Answer-first, GOV.UK 의 "Put the most important information first" 가 같은 규칙이다 ([Wikipedia BLUF](https://en.wikipedia.org/wiki/BLUF_(communication)); [GOV.UK Create a clear structure](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/)). Microsoft 는 이를 3단계로 줄인다. **"Use short, simple words." "Get to the point." "Then stop."** ([Microsoft Scannable content](https://learn.microsoft.com/en-us/style-guide/scannable-content/)). 근거는 공통이다. 사용자는 웹 페이지 단어의 20~28% 만 읽고 F 패턴으로 스캔한다 ([NN/g How Little Do Users Read?](https://www.nngroup.com/articles/how-little-do-users-read/)).

조건 선행과 괄호 금지도 근거까지 일치한다. Google 은 **"try to mention the circumstance, conditions, or goal before you provide the instruction"** 이라고 쓰고, 이유를 "Mentioning the circumstance first lets the reader skip the instruction if it doesn't apply" 로 든다 ([Google Sentence structure](https://developers.google.com/style/sentence-structure)). 괄호에 대해서는 "don't put important information in parentheses if you can help it" 과 "some readers ignore anything that appears in parentheses" 를 적는다 ([Google Parentheses](https://developers.google.com/style/parentheses)). 미국 연방 지침은 "if" 절을 별도 문장으로 떼는 "Suppose / In this case" 기법을 권한다. 사용자 CLAUDE.md 의 "조건은 문장 앞에 쓴다" 와 "괄호 안 보충 설명을 쓰지 않는다" 는 이 2개 가이드와 같은 규칙이다.

### 불릿은 스캔용 문서와 논증용 문서에서 반대 평가를 받는다

불릿에 대한 입장은 문서 목적에 따라 갈린다. NN/g 는 1997년 실험에서 간결한 글 58%, 스캔 가능한 레이아웃 47%, 셋을 합친 버전 **"124% better usability"** 를 보고하고 불릿 목록을 권고 6개에 넣었다 ([NN/g How Users Read on the Web](https://www.nngroup.com/articles/how-users-read-on-the-web/)). 반대로 Bezos 는 "We don't do PowerPoint" 라고 쓰고 6쪽 서사 메모를 요구했다 ([2017 Letter to Shareholders](https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders)). Tufte 는 불릿 목록이 "a misleading façade of objectivity and neutrality" 를 만든다고 비판했다 ([Wikipedia The Cognitive Style of PowerPoint](https://en.wikipedia.org/wiki/The_Cognitive_Style_of_PowerPoint)). 두 진영은 다른 문서를 말한다. NN/g 는 웹 조회용 짧은 글을, Bezos 와 Tufte 는 관계와 논증을 다루는 의사결정 문서를 말한다. AI 답변은 단순 질의에서 전자에, 비교·추론 설명에서 후자에 가깝다. 통제 실험은 Radboud 대학 논문 1건만 찾았다. 123명 실험에서 시각적 목록 구조가 논증 회상을 높였지만, 형식별 순위는 초록에서 확인하지 못했다 ([Radboud thesis](https://theses.ubn.ru.nl/items/59a7a81b-d28f-4273-a09f-120f16567733/full)).

불릿을 쓸 때의 형식 규칙은 Google 과 Microsoft 가 구체적이다. Google 은 "Don't use a list to show only one item" 과 병렬 구조를 둔다 ([Google Lists](https://developers.google.com/style/lists)). Microsoft 는 **"A list should have at least two items but (if possible) no more than seven items"** 를 둔다 ([Microsoft Lists](https://learn.microsoft.com/en-us/style-guide/scannable-content/lists)). GOV.UK 는 도입문 필수, 불릿 1개당 1문장, 마지막 불릿 뒤 마침표 없음을 둔다 ([GOV.UK A to Z style guide](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/style-guides/a-to-z-style-guide/)). 이 하한 2개와 상한 7개는 AI 답변의 불릿 사용 기준으로 바로 옮길 수 있다.

## 실증 연구는 평가자 편향을 측정했지만 사람의 선호는 약하게 나왔다

길이 편향은 LLM 판정자에서 가장 크다. Zheng 외 연구에서 내용을 반복해 길이만 늘린 "repetitive list" 공격에 GPT-3.5 와 Claude-v1 은 **91.3%** 속았고 GPT-4 는 8.7% 만 속았다 ([Judging LLM-as-a-Judge](https://arxiv.org/html/2306.05685)). Dubois 외 연구는 길이를 통제하면 Chatbot Arena 와의 상관이 0.94 에서 0.98 로 오른다고 보고했다 ([Length-Controlled AlpacaEval](https://arxiv.org/abs/2404.04475)). Singhal 외 연구는 보상 모델이 길이 편향의 주 원인이고, 길이만으로 만든 보상이 RLHF 개선의 대부분을 재현한다고 밝혔다 ([A Long Way to Go](https://arxiv.org/abs/2310.03716)). 사람의 편향은 더 약하다. Wu 와 Aji 는 "GPT-4 demonstrates the most bias and the expert annotators demonstrate the least bias" 라고 적었다 ([Style Over Substance](https://arxiv.org/abs/2307.03025)). 이 논문은 "Work in progress" 표기가 있는 preprint 다. Chatbot Arena 회귀 분석에서 길이 계수는 0.249 이고 마크다운 리스트 0.031, 헤더 0.024, 볼드 0.019 였다. 저자는 "all other markdown effects are second order" 라고 결론지었다 ([LMSYS style control](https://www.lmsys.org/blog/2024-08-28-style-control)).

마크다운 편향은 2026년 연구에서 가장 큰 판정자 편향으로 측정됐다. 같은 내용을 마크다운과 평문으로 보였을 때 Claude Sonnet 4 판정자의 style bias 는 +0.68, Gemini 2.5 Pro 는 +0.76 이었다. 같은 연구의 소규모 사람 실험에서 사람은 마크다운을 **약 57%** 만 선호했고 LLM 판정자 4개는 73~97% 선호했다 ([Judging the Judges](https://arxiv.org/html/2604.23178)). 이 논문은 단독 저자 preprint 이고 사람 실험의 n 은 확인하지 못했다. 그래도 "bullet-point disease" 의 기계적 원인을 설명한다. 판정자가 마크다운을 강하게 선호하고, 그 판정자로 학습하면 모델이 불릿과 볼드를 늘린다. 사람의 선호 57% 는 이를 정당화할 만큼 크지 않다. YapBench 는 사용자 관점에서 장황함을 측정했다. 짧은 답이 이상적인 질문에서 모델 간 초과 길이가 "order-of-magnitude spread" 를 보였고, 한 줄 코딩 요청의 "explanation/formatting overhead" 를 별도 실패 유형으로 분류했다 ([YapBench](https://arxiv.org/abs/2601.00624)).

### 길이는 오류 발견에도 영향을 준다

Friedman 외 연구는 24명 피험자에게 틀린 LLM 설명을 보였다. 중간 길이 설명에서 피험자 정답률이 짧거나 긴 설명보다 높았다. 설명이 맞을 때는 길이와 무관하게 정답률이 높았다 ([Not Too Short, Not Too Long](https://arxiv.org/abs/2603.06878)). 이 결과는 "짧을수록 좋다" 가 아니라 "오류를 검증할 만큼의 근거를 남긴다" 를 뜻한다. 가독성 연구는 의료 도메인에 편중돼 있다. 안과 메타분석 11편에서 ChatGPT 의 FKGL 은 9.82 로 기존 자료 9.54 와 유의 차이가 없었다. 학년 지시는 가독성을 유의하게 개선했다 ([Review of Optometry 보도](https://www.reviewofoptometry.com/article/ai-chatbot-responses-on-eye-care-dont-outperform-existing-materials-in-readability)). 피부과 연구에서 자외선차단제 자료는 지시 2회로 FKGL 9.1 에서 3.8 로 내려갔지만, 흑색종 자료는 10.5 에서 7.9 에 머물렀다 ([JMIR Dermatology](https://pmc.ncbi.nlm.nih.gov/articles/PMC10955394/)). 한 번의 지시가 목표 수준을 보장하지 않는다.

### 포맷 규칙은 겹칠수록 지켜지지 않는다

지시 준수 벤치마크는 규칙 수의 한계를 보인다. IFEval 에서 2023년 GPT-4 는 단일 포맷 제약을 prompt-level strict **76.89%** 따랐다 ([IFEval](https://arxiv.org/abs/2311.07911)). FollowBench 에서 제약을 1개에서 5개로 늘리면 GPT-4 의 전체 HSR 은 84.7% 에서 61.9% 로, GPT-3.5 의 Format HSR 은 90.0% 에서 50.0% 로 떨어졌다 ([FollowBench](https://arxiv.org/html/2310.20410)). IFBench 는 새 제약 유형에서 같은 모델이 50포인트 이상 낮게 나오고, GPT-4.1 과 Claude 4 Sonnet 도 "below 50%" 라고 보고했다 ([IFBench](https://arxiv.org/abs/2507.02833)). IFScale 은 지시 500개에서 최고 모델도 68% 정확도이고 "bias towards earlier instructions" 를 보인다고 적었다 ([IFScale](https://arxiv.org/abs/2507.11538)). McMillan 의 요인 실험은 CLAUDE.md 의 크기·위치·구조·모순 4변수가 준수율에 유의한 영향이 없다고 보고했다. 대신 세션 안에서 함수를 1개 더 만들 때마다 준수 확률이 약 5.6% 낮아졌다 ([McMillan 2026](https://arxiv.org/abs/2605.10039)). 두 연구를 합치면 파일 구조보다 지시 총량과 세션 길이가 준수율을 좌우한다.

### 구조화 출력은 "먼저 추론하고 나중에 포맷한다" 로 수렴한다

기계 파싱용 포맷의 연구도 사람 독자용 지시에 시사점을 준다. Tam 외 연구는 "a significant decline in LLMs reasoning abilities under format restrictions" 를 보고했다 ([Let Me Speak Freely?](https://arxiv.org/abs/2408.02442)). 2026년 후속 연구는 원인을 포맷 자체가 아닌 필드 순서와 모델 여유 용량으로 좁혔다. "Structure Tax" 는 reasoning-first 필드 순서가 자유 형식과 같거나 높고 answer-first 순서가 급락을 일으킨다고 보고했다 ([Structure Tax](https://arxiv.org/abs/2610.12056)). "Capacity, Not Format" 은 Opus 4.7 도 AIME 에서 96.2% 에서 91.0% 로 떨어지지만, 추론 후 포맷하는 절제 실험이 손실의 80~87% 를 회복한다고 적었다 ([Capacity, Not Format](https://arxiv.org/abs/2606.09410)). 이 논문은 단독 저자 preprint 다. Anthropic API 는 이 처방을 설계에 넣었다. "Grammar state resets between sections, allowing Claude to think freely while still producing structured output in the final response" 다 ([Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)). 사람 독자용 답변에서도 같은 원리가 적용된다. 답을 먼저 쓰라는 "결론 먼저" 규칙은 응답 구조에 관한 것이고, 추론 자체는 thinking 블록에서 먼저 끝난다.

## 실무자와 타 벤더는 이진 규칙, 채널별 포맷, 규칙 삭감을 권한다

실무자의 첫 처방은 척도형 규칙을 이진 규칙으로 바꾸는 것이다. Peter Huang 은 **"'Be concise' isn't actionable. It's an aspiration."** 이라고 쓰고, 대안으로 "answer in 3 sentences or fewer unless I explicitly ask you to elaborate" 와 "No bullet lists in conversational responses" 를 들었다. 원칙은 "Binary instructions are enforceable; scalar ones get interpreted." 다 ([dev.to Peter Huang](https://dev.to/peterverse180/writing-a-claudemd-that-claude-actually-follows-4llo)). OpenAI 의 GPT-5.1 가이드도 같은 방식이다. 코딩 에이전트 예시는 변경 크기별 상한을 수치로 둔다. **"Tiny/small single-file change (≤ ~10 lines): 2–5 sentences or ≤3 bullets. No headings."** 과 "Medium change (single area or a few files): ≤6 bullets or 6–10 sentences." 다 ([GPT-5.1 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide)). 같은 가이드는 "GPT-5.1 adheres well to concrete length guidance" 라고 적는다.

둘째 처방은 채널에 따라 마크다운을 켜고 끄는 것이다. OpenAI Model Spec 2025-02-12 판은 대화형 기본값을 "Unless otherwise specified, assistant outputs should be formatted in Markdown with LateX extensions" 로 뒀다 ([Model Spec 2025-02-12](https://model-spec.openai.com/2025-02-12.html)). 반대로 GPT-5 API 는 "By default, GPT-5 in the API does not format its final answers in Markdown" 이다 ([GPT-5 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide)). CLI 하네스는 터미널 렌더링 때문에 마크다운을 제한한다. Codex CLI 프롬프트는 **"You are producing plain text that will later be styled by the CLI"** 라고 선언하고, 불릿은 "4–6 per list ordered by importance", "no nested bullets/hierarchies" 를 둔다 ([Codex CLI prompt](https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/gpt-5.1-codex-max_prompt.md)). Gemini CLI 는 "Aim for fewer than 3 lines of text output" 과 "After completing a code modification or file operation *do not* provide summaries unless asked" 를 둔다 ([Gemini CLI snippets.ts](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/packages/core/src/prompts/snippets.ts)). xAI 의 X 답글용 프롬프트는 "under 550 characters" 와 "Do not use markdown formatting" 을 둔다 ([xai-org/grok-prompts](https://github.com/xai-org/grok-prompts/blob/main/ask_grok_system_prompt.j2)). 이 규칙들은 헌법의 "Markdown only if Markdown is likely to be rendered" 를 각 제품이 구현한 형태다.

셋째 처방은 규칙을 줄이는 것이다. Thariq Shihipar 는 "a rule that's right 90% of the time is wrong the other 10%" 라고 쓰고, 대부분의 CLAUDE.md 가 "still walls of hard rules and banned phrases" 라고 지적했다 ([howborisusesclaudecode.com 경유](https://howborisusesclaudecode.com/)). 이 인용은 X 원문을 2차 사이트로 확인한 것이다. drona23 리포지토리는 2026년 6월 재현 벤치마크에서 "간결" 규칙의 토큰 감소가 haiku 4%, sonnet 12%, opus 7% 에 그쳤고, 기본값이 이미 "0% preamble, sycophancy" 라서 아첨·서두 금지 규칙은 입력 토큰만 늘린다고 적었다 ([drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient)). OpenAI Model Spec 도 같은 방향이다. 2025-02-12 판의 "Be clear and direct" 와 "Use Markdown with LaTeX extensions" 절은 2026-10-29 판에서 사라지고 "If parts of the response are in a specific format (e.g., Markdown, code, JSON, LaTeX), GPT should adhere to the specifications of that format" 로 일반화됐다 ([Model Spec 2026-10-29](https://model-spec.openai.com/2026-10-29.html)).

### ASD-STE100 의 LLM 적용은 2026년 하반기에 퍼졌지만 통제 실험이 없다

Karpathy 는 2026년 10월 2일 **"Ask your LLM to explain something in ASD-STE100"** 이라고 썼다 ([max.nardit.com 재수록](https://max.nardit.com/articles/karpathy-understanding-llm-outputs)). X 원문은 접근하지 못했고 재수록본에 의존한다. 같은 재수록본은 첨부 치트시트가 Issue 9 와 어긋나는 항목을 지적한다. SimpleEnglish 스킬은 채팅 답변 규칙을 "prose only (no headers, bullets, bold, or tables), answer in the first sentence, no em-dashes" 로 두고, 자체 벤치마크에서 가시 결함 218 에서 11 로 95% 감소를 보고했다 ([AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish)). 저자는 심사자가 Claude 모델이라 편향 가능성이 있고 "Output is not STE-certified" 라고 적었다. HN 스레드에서는 한 줄 지시로 충분하다는 의견과 지시가 "drift immediately" 한다는 보고가 함께 나왔다 ([HN SimpleEnglish](https://news.ycombinator.com/item?id=49114639)). Menon Lab 은 적용 범위를 좁혔다. **"Use it where ambiguity is the enemy: instructions, runbooks, agent output you have to act on quickly."** 와 "Do not force a risk discussion or a research summary into it." 다 ([Menon Lab](https://themenonlab.blog/blog/asd-ste100-simplified-technical-english-prompting)). Shreya Shankar 는 "LLMs often overuse bullet points, especially nested ones" 과 "Empty summary sentences feel conclusive, but say nothing" 을 지적하면서도 em dash 와 헤더는 옹호했다 ([sh-reya.com](https://www.sh-reya.com/blog/ai-writing)).

## 출처별 구체 규칙 비교

아래 표는 각 출처가 명시한 규칙만 적는다. "미명시" 는 그 출처에 해당 규칙이 없거나 이번 조사에서 원문을 가져오지 못한 칸이다.

| 항목 | Anthropic 공식 | ASD-STE100 | Plain language 계열 | 기술 문서 가이드 | OpenAI | CLI 하네스 | 실무자 |
|---|---|---|---|---|---|---|---|
| 문장 길이 | 미명시. "Write complete sentences" | 절차 20단어, 설명 25단어 | GOV.UK 25단어. 미국 연방은 수치 없이 1문장 1생각 | Microsoft "short sentences" | 미명시 | 미명시 | SimpleEnglish 20/25단어. Menon 20단어 |
| 단락 길이 | 미명시 | 6문장 | GOV.UK 5문장 | Microsoft 3~7줄 | 미명시 | Gemini CLI 응답 3줄 미만 | 미명시 |
| 산문 대 목록 | 2026-09: 다면적일 때 목록. 감정적 대화·거절은 산문 | 미확인 | GOV.UK 불릿 1개당 1문장, 도입문 필수 | Google 1항목 금지. Microsoft 2~7항목 | 2025-02: "judiciously to aid the user in scanning". 5.1 가이드: 짧은 변경은 ≤3불릿 | Codex 4~6불릿, 중첩 금지 | Huang 대화에서 불릿 금지. SimpleEnglish 산문만 |
| 마크다운 | 헌법: 렌더링될 때만. Fable 5.1: anti-formatting 규칙 제거 | 해당 없음 | 미명시 | 미명시 | 챗은 Markdown+LaTeX 기본. API 는 비사용 기본 | Codex 플레인 텍스트. Gemini CLI GFM 이지만 monospace 경고. Grok X 답글 금지 | Karpathy HTML 사다리. Willison HTML 재고 |
| 길이 보정 | 복잡도에 맞춤. 짧은 질문은 몇 문장. 모델별 반대 보정 | 해당 없음 | GOV.UK "Keep chunks of text short" | Microsoft "Get to the point. Then stop." | verbosity low/medium/high. 변경 크기별 수치 상한 | Codex "be very concise". Grok "shortest answer you can" | Huang 3문장 이하. Shankar "contribution is commensurate with the length" |
| 결론 먼저 | "Lead with the outcome". Concise style 첫 문장 | 안전 지시는 명령·조건으로 시작 | GOV.UK "Put the most important information first". NN/g 역피라미드 | Google 조건 선행. Microsoft "lead with what's most important" | "direct answer rather than a list of facts" | Codex "simple tasks → lead with outcome". "Do not start this explanation with "summary"" | SimpleEnglish "answer in the first sentence" |
| 마무리 제안 | 3.7: 1~2문장 거절, 질문 1개 이하. 5.1: 필요하면 더 할 말이 있다고 알림 | 해당 없음 | GOV.UK 요약 중복 금지 | 미명시 | 음성: 질문 없이 직접 답. 대화형에서만 follow-up 허용 | Codex 다음 단계 있을 때만 제안, 없으면 금지. Gemini CLI 요약 금지. Cline 질문·제안으로 끝내기 금지 | Willison 질문으로 끝내는 slop 비판 |
| 서두·필러 | 2024: "Certainly" 금지. 5.1: "genuinely", "honestly" 금지. 모든 단어가 다른 의미를 더해야 함 | 해당 없음 | 미명시 | 미명시 | 과잉 헤징·사과·"as a large language model" 금지 | Gemini CLI 전·후 서술 금지. Cline "Great", "Certainly" 금지 | drona23 서두·마무리 금지 |

## 출처가 충돌하는 지점과 합의하는 지점

| 쟁점 | 한쪽 | 다른쪽 | 판정 |
|---|---|---|---|
| 불릿 허용 범위 | NN/g, GOV.UK, Microsoft 는 스캔용으로 권장. Codex 는 4~6개 허용 | Bezos, Tufte, SimpleEnglish, Claude Opus 4.6 프롬프트는 보고서·설명에서 배제 | 문서 목적이 다르다. 조회·절차는 불릿, 논증·비교는 산문이 맞다. Fable 5.1 의 "다면적일 때" 가 절충안이다 |
| 규칙 수 | Huang, SimpleEnglish, 커뮤니티 CLAUDE.md 는 구체 규칙을 더한다 | Thariq, Boris Cherny, Willison, Anthropic Fable 5.1 가이드는 규칙을 지우라고 한다 | 벤치마크가 후자를 지지한다. 제약 5개에서 준수율 50~62% 로 떨어진다. 남길 규칙은 모델 기본값에서 벗어나게 하는 것만이다 |
| "간결" 지시의 효과 | Opus 5 가이드와 Huang 은 명시 지시가 필요하다고 본다 | drona23 벤치마크는 토큰 감소 4~12% 에 그치고 기본값이 이미 간결하다고 본다 | 모델 세대에 따라 다르다. 지시 전에 기본값을 측정해야 한다 |
| 통제 언어 적용 범위 | Karpathy, hsaliak 은 설명 전반에 ASD-STE100 을 권한다 | Menon, HN 댓글, bretkerr 는 절차·런북에 한정하고 지식 노동에는 "very bad" 라고 본다 | 적용 범위를 한정하는 쪽이 맞다. 보고서는 가독성 우선 원칙과 충돌한다 |
| 마크다운 기본값 | OpenAI 2025 Model Spec 은 Markdown 기본 | 헌법, GPT-5 API, Codex, Grok 은 렌더링 안 되면 비사용 | 충돌이 아니라 채널 차이다. 렌더링 여부가 기준이다 |
| 마무리 제안·질문 | Sonnet 3.5 2024-09 는 "offers to elaborate". Fable 5.1 은 더 할 말이 있다고 알릴 수 있다 | Cline, Gemini CLI 는 금지. Codex 는 자연스러운 다음 단계만 | 에이전트 작업 보고에서는 금지가 우세하다. 대화형 답변에서는 1개 제안이 허용된다 |
| 길이와 품질 | LLM 판정자와 Arena 는 긴 답을 선호 | 전문가 평가자와 YapBench 는 짧은 답을 선호. Whittaker·Sun 은 품질과 가독성이 음의 상관 | 독자가 전문가면 긴 답의 이점이 작다. 그러나 오류 검증에는 중간 길이가 유리하다 |
| em dash | Hamel Husain, Bret Taylor 는 금지 | Willison, Karpathy, Shankar 는 정당한 구문으로 옹호 | 가독성 근거가 없는 "AI 티" 회피 규칙이다. 사용자 규칙의 대시 금지는 절 연결 방지가 근거이므로 다른 성격이다 |

합의 지점은 5개다. 첫째, 결론을 첫 문장에 쓴다. Anthropic, NN/g, BLUF, Minto, GOV.UK, Microsoft, OpenAI, Codex, SimpleEnglish 가 모두 같은 규칙을 둔다. 둘째, 길이는 요청의 복잡도에 맞춘다. 헌법, Sonnet 5 가이드, OpenAI, Gemini 3 가 같은 전제를 둔다. 셋째, 필러·과잉 caveat·반복을 뺀다. 헌법, OpenAI Model Spec, Gemini CLI, Cline 이 같은 금지를 둔다. 넷째, 조건은 지시 앞에 쓴다. ASD-STE100, Google, 미국 연방 지침이 같은 근거를 든다. 다섯째, 감정적 대화와 거절에서는 포맷을 쓰지 않는다. 이 규칙은 Anthropic 에만 있지만 2025년부터 2026년까지 바뀌지 않았다.

## 사용자의 CLAUDE.md 규칙은 대부분 뒷받침되고 3곳에서 확장이 필요하다

사용자의 전역 CLAUDE.md 는 ASD-STE100 을 지침 문장에 적용한다. 조사 결과는 그 규칙을 아래처럼 평가한다.

| 사용자 규칙 | 뒷받침하는 출처 | 평가 |
|---|---|---|
| 한 문장에 한 가지 정보 | 미국 연방 "Express only one idea in each sentence". ASD-STE100 지시 1개 = 문장 1개 | 일치 |
| 절차 20단어, 설명 25단어 | ASD-STE100. GOV.UK 25단어 | 일치. 한국어 어절 환산은 어느 출처에도 없다 |
| 단락 6문장 이하 | ASD-STE100 6문장. GOV.UK 5문장. Microsoft 3~7줄 | 일치. GOV.UK 가 더 엄격하다 |
| 조건은 문장 앞 | Google Sentence structure. 미국 연방 "Suppose / In this case" | 일치. 근거까지 같다 |
| 이중 부정 금지 | 공개 출처에서 원문 미확인 | 미검증. ASD-STE100 공식 PDF 확인 필요 |
| 괄호 안 보충 설명 금지 | Google Parentheses "some readers ignore anything that appears in parentheses" | 일치 |
| 세미콜론·대시로 절 연결 금지 | Microsoft 목록 끝 세미콜론 금지. Hamel Husain em dash 금지 | 부분 일치. Willison 과 Shankar 는 em dash 를 옹호한다 |
| 명령형 지시, 능동태, 현재형 | ASD-STE100, 미국 연방, GOV.UK, Codex "present tense, active voice" | 일치 |
| 주어 생략 금지 | 미국 연방 "Active voice makes it clear who should do what" | 일치 |
| 한 개념에 한 용어 | ASD-STE100 "One word, one part of speech, one meaning". Menon "obey" 사례 | 일치 |
| "등" 금지, 전부 나열 | 직접 출처 없음 | ASD-STE100 의 명확성 원칙에서 추론한 규칙이다 |
| 아라비아 숫자 | GOV.UK "Write all other numbers in numerals (including 2 to 9)" | 일치 |
| 금지 규칙에 이유 1문장 | Thariq "Let Claude use judgement". 헌법의 이유 설명 방식 | 일치. 조사 결과가 이 규칙의 가치를 강하게 지지한다 |

확장이 필요한 지점은 3곳이다. 첫째, 사용자 규칙은 문장 수준만 다룬다. 답변 구조 규칙이 없다. 결론 먼저, 다면적일 때만 목록, 마무리 제안 조건은 모든 출처가 합의하는 규칙이므로 추가할 가치가 있다. 둘째, 사용자 규칙은 적용 범위를 "지침·참조 문서·Claude 의 답변" 으로 둔다. Menon 과 HN 댓글은 통제 언어가 위험 논의와 연구 요약에 맞지 않는다고 본다. Anthropic 의 "readability matters more" 도 압축된 문장을 경계한다. 답변 유형별 적용 강도를 나눌 필요가 있다. 셋째, 사용자 규칙은 모델 세대를 가정하지 않는다. Fable 5.1 은 이미 포맷을 적게 쓰고 문장이 길어지는 경향이 있다. 짧은 문장 규칙은 이 모델에서 유효하지만, 포맷 억제 규칙을 더하면 "suppress structure the content needs" 위험이 있다 ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#control-the-format-of-responses)).

## Claude 에게 포맷을 지시하는 방법은 4가지로 정리된다

첫째, 금지 대신 원하는 형태를 쓴다. Anthropic 의 포맷 제어 4원칙 중 첫째는 **"Tell Claude what to do instead of what not to do"** 다. 예시는 "Do not use markdown in your response" 대신 "Your response should be composed of smoothly flowing prose paragraphs." 다 ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#control-the-format-of-responses)). 나머지 3원칙은 XML 포맷 태그, 프롬프트 스타일과 출력 스타일 일치, 상세 지시다. Opus 5 와 Sonnet 5 가이드는 "Positive examples of the communication style you want tend to be more effective than instructions about what not to do" 라고 반복한다 ([Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5#user-facing-progress-updates)). Fable 5.1 가이드는 예시 1개로 가르치는 방법을 든다. 사용자 요청, 올바른 응답, 그 응답이 옳은 이유 1문장을 함께 넣는다 ([Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#quoting-retrieved-sources)).

둘째, 검증 가능한 수치로 쓴다. "concise" 는 검사할 수 없고 "3문장 이하" 는 검사할 수 있다. Huang 의 상위 3개 이진 규칙은 "have changed my sessions more than the other 40 instructions combined" 였다 ([dev.to Peter Huang](https://dev.to/peterverse180/writing-a-claudemd-that-claude-actually-follows-4llo)). OpenAI 의 변경 크기별 수치 상한과 Codex 의 "4–6 per list" 가 같은 방식이다. 사용자의 20/25 어절 규칙도 이 범주에 든다.

셋째, 모델 기본값을 측정한 뒤 반대 방향으로만 보정한다. Opus 5 에는 "Keep responses focused, brief, and concise" 를 더하고, Fable 5.1 에는 anti-formatting 규칙을 지우고 진행 보고를 요청한다 ([Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5#response-length-and-verbosity); [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#ask-for-user-facing-progress-updates)). 긴 시스템 프롬프트에서는 말미에 `<tone_preference>` 같은 짧은 리마인더를 둔다. claude.ai 시스템 프롬프트도 같은 태그를 말미에 쓴다 ([Claude Fable 5.1 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1)). Claude Code 에서는 세션 단위 포맷을 output style 로, 프로젝트 관례를 CLAUDE.md 로, 예외 없는 강제를 hook 으로 나눈다 ([Output styles](https://code.claude.com/docs/en/output-styles)).

넷째, 규칙 수를 줄이고 기준을 준다. Thariq 의 사례는 "Never write multi-paragraph docstrings" 를 "Write code that reads like the surrounding code: match its comment density, naming, and idiom." 으로 바꿨다 ([claude.dev 블로그](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/)). 포맷 규칙도 같은 방식으로 쓸 수 있다. "불릿 금지" 대신 "내용이 다면적일 때 불릿을 쓴다. 관계나 논증을 설명할 때는 산문을 쓴다." 가 기준형 규칙이다. 금지 규칙에 이유를 붙이는 사용자 규칙은 이 방향과 일치한다.

## 미검증 출처와 조사 공백

아래 출처는 신뢰도가 낮다. 보고서 본문에서 인용했더라도 카드 근거로 쓸 때는 별도 확인이 필요하다.

| 출처 | 유형 | 주의점 |
|---|---|---|
| "Capacity, Not Format" arXiv:2606.09410 | 단독 저자 preprint | 전문 미확인. Opus 4.7 수치는 초록 기준 |
| "Judging the Judges" arXiv:2604.23178 | 단독 저자 preprint | 사람 실험 n 미확인. 버전 간 수치 변동 가능 |
| "AI Should Be More Human, Not More Complex" arXiv:2508.04713 | 산업계 단독 저자 preprint | 방법론·수치 없음. 참가자 수 "est." |
| "Style Over Substance" arXiv:2307.03025 | "Work in progress" preprint | 수치가 초록에 없음 |
| dottxt "Say What You Mean" | 벤더 블로그 | constrained decoding 라이브러리 개발사의 이해관계 |
| SimpleEnglish 벤치마크 | 저자 자체 벤치마크 | 심사자가 Claude 모델. 1회 실행. 독립 재현 없음 |
| drona23 벤치마크 | 커뮤니티 리포지토리 | N=5. 63% 수치는 단어 수 1회 실행 |
| Karpathy 2026-10-02 글 | 2차 재수록 | X 원문 접근 불가. 치트시트에 Issue 9 와 어긋나는 항목 |
| Thariq, Boris Cherny X 글 | 2차 사이트 경유 | howborisusesclaudecode.com 을 통해 확인 |
| Ethan Mollick 발언 | 2차 집계 사이트 | 1차 글 미발견 |
| Hamel Husain CLAUDE.md | 검색 스니펫 | 직접 접속 404 |
| Cursor 시스템 프롬프트 | 유출·미검증 | 포럼 댓글이 Cline 프롬프트라고 주장 |
| Cline 프롬프트 | 2024년 재수록본 | 현재 버전과 대조 못함 |
| Microsoft Copilot 프롬프트 | 유출·미검증 | 직접 접속 410 |
| GitHub Copilot 프롬프트 해석 | 비공식 로그 해석 | 글쓴이가 "may contain mistakes" 경고 |
| HumanLayer "150~200 지시" | 2차 미러 | IFScale 초록의 "500개에서 68%" 와 직접 맞지 않음 |
| 헌법 공개일 2026-01-21 | 2차 보도 | 헌법 페이지에 날짜 없음 |

조사 공백은 7개다. 첫째, 챗봇 답변을 산문과 불릿으로 동일 내용 제시하고 이해도를 측정한 동료 심사 HCI 연구가 없다. 둘째, 전문가 사용자의 길이 선호를 직접 측정한 2025~2026년 연구가 없다. 셋째, Claude 4.x·5.x 의 IFEval·IFBench 공식 수치가 1차 출처에 없다. 넷째, ASD-STE100 공식 PDF 를 열지 못해 이중 부정 금지와 괄호 규칙의 원문을 확인하지 못했다. 다섯째, 국립국어원 『쉬운 공문서 쓰기 길잡이』 PDF 본문을 읽지 못해 한국어 문장 길이 규칙을 확인하지 못했다. 여섯째, Claude Code 의 실제 시스템 프롬프트 중 최종 메시지 포맷 규칙은 공개 문서에 없다. 일곱째, ASD-STE100 을 LLM 에 적용한 통제 실험이나 동료 심사 논문이 없다.

## 결론

이번 조사의 가장 중요한 발견은 포맷 규칙의 수명이다. Anthropic 의 공개 규칙은 2년 동안 5번 바뀌었고, OpenAI Model Spec 은 2025년의 구체 규칙을 2026년에 지웠다. 바뀌지 않은 것은 구조 원칙이다. 결론 먼저, 복잡도에 맞춘 길이, 필러 제거, 감정적 대화에서 포맷 배제다. 바뀐 것은 포맷 수단에 관한 규칙이다. 불릿 금지, 마크다운 기본값, 간결 지시가 그렇다. 수단 규칙은 모델 기본값에 따라 방향이 뒤집힌다. 따라서 카드로 남길 가치가 있는 것은 구조 원칙과 지시 방법이고, 수단 규칙은 모델 버전을 적은 조건부 규칙으로만 남겨야 한다.

둘째 발견은 사용자 규칙의 위치다. ASD-STE100 문장 규칙은 지침 문장과 절차형 답변에서 모든 출처의 지지를 받는다. 그러나 보고서와 논증형 답변에서는 "readability matters more" 와 Menon 의 범위 한정이 경고를 준다. 사용자 규칙은 문장 수준에서 완성됐고, 다음 단계는 답변 유형별 구조 규칙이다. 조회형 답변은 첫 문장 결론과 3문장 이하, 절차형 답변은 번호 목록과 조건 선행, 논증형 답변은 산문과 역피라미드로 나누는 방식이 조사 결과와 맞는다.

## 카드 후보

| 번호 | 원칙 1줄 | 주장 | 가장 강한 근거 |
|---|---|---|---|
| 1 | 결론을 첫 문장에 쓴다 | 첫 문장이 "what happened" 또는 "what did you find" 에 답하면 독자가 어디서 멈춰도 핵심을 얻는다 | [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5#strong-instruction-following), [NN/g Inverted Pyramid](https://www.nngroup.com/articles/inverted-pyramid/), [GOV.UK Create a clear structure](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-structure/), [Codex CLI prompt](https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/gpt-5.1-codex-max_prompt.md) |
| 2 | 가독성이 간결함보다 앞선다 | 짧게 쓰는 방법은 내용 선택이다. 문장을 조각·화살표·약어로 압축하면 독자가 더 많이 일한다 | [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5#readability-when-communicating-with-the-user), [Not Too Short, Not Too Long](https://arxiv.org/abs/2603.06878) |
| 3 | 목록은 내용이 다면적일 때만 쓴다 | 사람의 마크다운 선호는 약 57% 다. 관계와 논증은 산문이, 병렬 항목과 절차는 목록이 맞다 | [Claude Fable 5.1 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1), [Judging the Judges](https://arxiv.org/html/2604.23178), [Wikipedia The Cognitive Style of PowerPoint](https://en.wikipedia.org/wiki/The_Cognitive_Style_of_PowerPoint), [Microsoft Lists](https://learn.microsoft.com/en-us/style-guide/scannable-content/lists) |
| 4 | 마크다운은 렌더링될 때만 쓴다 | 터미널, 음성, X 답글, API 는 마크다운을 렌더링하지 않는다. 채널이 포맷을 결정한다 | [Claude's constitution](https://www.anthropic.com/constitution), [GPT-5 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide), [Codex CLI prompt](https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/gpt-5.1-codex-max_prompt.md) |
| 5 | 포맷 지시는 금지형이 아니라 긍정형으로 쓴다 | "Do not use markdown" 보다 "smoothly flowing prose paragraphs" 가 잘 지켜진다. 예시 1개가 금지 목록보다 효과적이다 | [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#control-the-format-of-responses), [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5#user-facing-progress-updates) |
| 6 | 길이 규칙은 검증 가능한 수치로 쓴다 | "concise" 는 해석되고 "3문장 이하" 는 집행된다. 변경 크기별 상한이 한 사례다 | [dev.to Peter Huang](https://dev.to/peterverse180/writing-a-claudemd-that-claude-actually-follows-4llo), [GPT-5.1 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide) |
| 7 | 포맷 규칙을 더하기 전에 모델 기본값을 확인한다 | 장황함과 포맷 기본값은 모델 세대마다 반대로 움직인다. 고정 규칙은 모델 교체 시 역효과를 낸다 | [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#communication-style-and-verbosity), [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1#formatting-in-chat), [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient) |
| 8 | 포맷 규칙은 적을수록 지켜진다 | 제약 5개에서 동시 준수율은 50~62% 로 떨어진다. 남길 규칙은 모델 기본값에서 벗어나게 하는 것만이다 | [FollowBench](https://arxiv.org/html/2310.20410), [IFBench](https://arxiv.org/abs/2507.02833), [claude.dev 블로그](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) |
| 9 | 에이전트 작업 보고는 결과 1~2문장으로 시작하고 요약을 반복하지 않는다 | "Done." 은 답변이 아니다. 작업을 보지 않은 독자에게 완전한 문장으로 다시 쓴다. 메타 서술과 중복 요약은 뺀다 | [Claude Fable 5.1 system prompts](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-1), [Gemini CLI snippets.ts](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/packages/core/src/prompts/snippets.ts), [Output styles](https://code.claude.com/docs/en/output-styles) |
| 10 | 통제 언어는 절차와 지침에 쓰고 논증과 연구 요약에는 쓰지 않는다 | ASD-STE100 은 모호성이 적인 곳에서 효과가 있다. 뉘앙스가 필요한 글에 강제하면 품질이 떨어진다 | [Menon Lab](https://themenonlab.blog/blog/asd-ste100-simplified-technical-english-prompting), [HN SimpleEnglish](https://news.ycombinator.com/item?id=49114639), [Wikipedia Simplified Technical English](https://en.wikipedia.org/wiki/Simplified_Technical_English) |

카드 10 의 근거 중 Menon Lab 과 HN 스레드는 실무자 의견이다. 통제 실험이 없으므로 카드 본문에 그 한계를 적어야 한다. 카드 3 의 57% 수치는 단독 저자 preprint 에서 나왔다. 카드에 쓸 때 등급을 표시해야 한다.
