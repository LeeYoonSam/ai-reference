# 실무자와 비 Anthropic 벤더가 말하는 AI 답변 포맷

조사일: 2026-10-30. 인용 영문은 원문 그대로 둔다. 유출·비공식 프롬프트는 각 항목에 `[유출/미검증]` 으로 표시한다. 1차 출처를 직접 열지 못한 항목은 `[2차 출처]` 로 표시한다.

## 1. 실무자들은 답변 포맷·장황함·"AI 티" 에 대해 무엇을 말하나

### Takeaway
실무자들의 공통 처방은 3 가지다. 모델에게 통제 언어나 구체적 길이 규칙을 주라. "be concise" 같은 척도형 규칙 대신 이진 규칙을 쓰라. 산출물 포맷을 Markdown 에서 HTML 같은 더 읽기 좋은 형식으로 바꾸라. em dash 는 널리 퍼진 "AI 티" 로 지목되지만, Willison 과 Karpathy 는 그 기준이 부당하다고 본다.

### Cited Findings

**Andrej Karpathy**
- 2026-10-02 X 게시글 (status 2105819303471976479) 도입부: "We'll be spending a lot more time trying to understand the outputs of language models." "A few thoughts, tips & tricks:" — [max.nardit.com 재수록](https://max.nardit.com/articles/karpathy-understanding-llm-outputs) [2차 출처, X 원문은 접근 불가]
- 같은 글, 팁 1 (글쓰기): "Writing. Something I've had success with: Ask your LLM to explain something in ASD-STE100," "it's a controlled language specification originally developed for aerospace maintenance documentation." — [max.nardit.com](https://max.nardit.com/articles/karpathy-understanding-llm-outputs)
- 같은 글, 팁 2~4: "Diagrams / images. Instead of writing, ask your LLM to create a diagram." / "Web pages. Ask for output "in HTML" to get a beautiful, interactive webpage." / "Explainer videos. The output format I am most bullish on is fully custom / bespoke explainer videos" — [max.nardit.com](https://max.nardit.com/articles/karpathy-understanding-llm-outputs)
- 2차 요약은 Karpathy 가 사양이 엄격해 "80% of the way to ASD-STE100" 정도를 요청한다고 전한다. — [munderdiffl.in](https://munderdiffl.in/blog/asd-ste100-prompting/); [dev.to aj1thkr1sh](https://dev.to/aj1thkr1sh/i-turned-andrej-karpathys-tips-on-understanding-llm-output-into-an-open-source-agent-skill-1mia) [2차 출처]
- 게시글에 첨부된 치트시트는 ASD-STE100 Issue 9 와 어긋나는 항목이 있다. 예: APPROXIMATELY 를 비승인으로 표시했지만 표준은 부사로 승인한다. TEST 를 동사로 승인했지만 표준은 명사만 승인한다. — [max.nardit.com 팩트체크](https://max.nardit.com/articles/karpathy-understanding-llm-outputs)
- 2026-07-15 X 답글 (status 2077433347085930882). Bret Taylor 가 AI 처럼 보이지 않으려고 em dash 를 버렸다고 쓴 글에 대한 답. 검색 스니펫에 보이는 본문: "It's not just em dashes, it's that many other legitimate & useful language constructs are suddenly and somewhat arbitrarily super awkw[ard] and cringe" — [x.com/karpathy](https://x.com/karpathy/status/2077433347085930882) [스니펫에서 잘림. 원문 페이지는 402 로 접근 불가]
- 2026-04-04 "LLM Wiki" gist 에는 문체·길이·불릿 대 산문 규칙이 없다. 답변 형식은 질문에 따라 달라진다고 쓴다: "Answers can take different forms depending on the question" — 마크다운 페이지, 비교표, 슬라이드, 차트를 든다. 답변에는 "with citations" 를 요구한다. — [gist.github.com/karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- Karpathy 가 불릿 과용을 직접 비판한 게시글은 찾지 못했다. 자세한 내용은 Gaps 를 본다.

**Simon Willison**
- 2026-02-15 "Finally, do em dashes": "I'm occasionally accused of using LLMs to write the content on my blog. I don't do that, and I don't think my writing has much of an LLM smell to it... with one notable exception:" 이어서 2015 년부터 블로그 코드가 ` - ` 를 em dash 로 바꿔 왔다고 밝힌다. — [simonwillison.net](https://simonwillison.net/2026/Feb/15/em-dashes/)
- 2025-05-25 Claude 4 시스템 프롬프트 해설. 리스트 금지 조항에 대해: "That "should not use lists in chit chat" note hints at the fact that LLMs love to answer with lists of things!" 그리고 "And _yet another_ instruction not to use too many lists!" 칭찬으로 시작하지 말라는 조항은 "an attempt at tamping down on the naturally sycophantic tendencies of LLMs" 라고 평했다. — [simonwillison.net](https://simonwillison.net/2025/May/25/claude-4-system-prompt/)
- 2024-05-08 slop 정의: "Slop describes AI-generated content that is both unrequested and unreviewed." — [simonwillison.net](https://simonwillison.net/2024/May/8/slop/)
- 2026-02-23 "reply guy" 봇 글. 참여를 유도하려고 질문으로 끝나는 "generic, banal commentary slop" 을 지적했다. — [simonwillison.net/tags/slop](https://simonwillison.net/tags/slop/)
- 2026-05-08 Thariq 의 HTML 글 소개. "Thought-provoking piece by Thariq Shihipar (on the Claude Code team at Anthropic)". GPT-4 시절 "the 8,192 token limit meant that Markdown's token-efficiency over HTML was extremely worthwhile" 라서 Markdown 을 기본으로 썼지만, "especially for output" 에서 재고 중이라고 썼다. HTML 은 "SVG diagrams, interactive widgets" 와 "in-page navigation" 을 담을 수 있다고 본다. — [simonwillison.net](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/)
- 2026-07-03. 고정 규칙 대신 모델이 테스트 작성 여부를 스스로 판단하게 두는 팁을 공유했다. — [simonwillison.net/tags/thariq-shihipar](https://simonwillison.net/tags/thariq-shihipar/)
- Willison 이 "it's not X, it's Y" 구문이나 불릿을 직접 "AI 티" 로 논한 글은 찾지 못했다.

**Thariq Shihipar (Claude Code 팀, Anthropic)**
- 2026-05 "Using Claude Code: The Unreasonable Effectiveness of HTML" (X 글, status 2052809885763747935). 추천 프롬프트 첫 문장: "Help me review this PR by creating an HTML artifact that describes it." — [simonwillison.net 인용](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/)
- 동반 페이지의 주장: "Each one trades a document you'd skim for one you'd actually read." / "Diffs and call-graphs are spatial information; markdown flattens them." / "reading three sequential walls of text and trying to hold them all in your head." — [thariqs.github.io/html-effectiveness](https://thariqs.github.io/html-effectiveness/)
- 2026-07-03 X 글. 계획 문서는 "lead with the decisions I'm most likely to tweak" 해야 하고, 기계적 리팩터링은 아래로 내리라고 썼다. 변경 보고는 "an HTML report on the changes" 로 "context, intuition, and what was done" 을 담게 했다. — [howborisusesclaudecode.com 인용](https://howborisusesclaudecode.com/), 원문 [x.com/trq212](https://x.com/trq212/status/2073100352921215386)
- 2026-07-24 X 글. 팀이 "deleted over 80% of the system prompt" 했고 코딩 평가에서 손실이 없었다. "a rule that's right 90% of the time is wrong the other 10%". 대부분의 CLAUDE.md 는 "still walls of hard rules and banned phrases" 라고 썼다. — [x.com/trq212](https://x.com/trq212/status/2080710971228918066) [howborisusesclaudecode.com 경유]
- 2026-09-18. CLAUDE.md 가 없으면 Claude Code 가 AGENTS.md 를 읽는다고 발표했다. — [simonwillison.net/tags/thariq-shihipar](https://simonwillison.net/tags/thariq-shihipar/)

**Boris Cherny (Claude Code 제작자)**
- 2026-04-16: "I've been loving the new focus mode in the CLI, which hides all the intermediate work to just focus on the final result." — [x.com/bcherny](https://x.com/bcherny/status/2044847855006024147) [howborisusesclaudecode.com 경유]
- 2026-01-02: "Anytime we see Claude do something incorrectly we add it to the CLAUDE.md, so Claude knows not to do it next time." — [x.com/bcherny](https://x.com/bcherny/status/2007179840848597422)
- 2026-06-08: 최소한의 시스템 프롬프트와 도구만 주라고 말했다. 같은 자리에서 Cat Wu: "Tell the model only what it needs to know and let it figure out the rest." — [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)
- 2026-06-09, Fable 5 에 대해: "There's nothing in Claude Code's prompting telling it to do that; it's just part of its personality." — [x.com/bcherny](https://x.com/bcherny/status/2064402671898075579)
- Boris 가 답변 길이·마크다운·이모지 규칙을 직접 공개한 글은 찾지 못했다. Recaps 기능은 "Short summaries of what the agent did and what's next" 로 설명된다. — [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)

**Paul Graham**
- 2025-05 "Good Writing": "there are two senses in which writing can be good: it can sound good, and the ideas can be right." / "When writing sounds good, it's mostly because it has good rhythm." / "It's less work to read writing that flows well". AI 언급은 없다. — [paulgraham.com/goodwriting.html](https://paulgraham.com/goodwriting.html)
- 2024-10 "Writes and Write-Nots": 글쓰기 능력이 희소해져 사회가 쓰는 사람과 못 쓰는 사람으로 갈린다고 주장한다. — [paulgraham.com/writes.html](https://paulgraham.com/writes.html) [검색 요약 경유]
- 2025~2026 년에 AI 산문 포맷을 다룬 에세이는 없다. 에세이 목록에 AI·LLM 제목이 없다. — [paulgraham.com/articles.html](https://paulgraham.com/articles.html)

**Hamel Husain**
- 자기 블로그용 CLAUDE.md 에 "Never use em dashes (—) or spaced hyphens ( - ) as punctuation." 규칙을 두고 쉼표·마침표·콜론·괄호를 대안으로 든다. 직설적이고 회의적인 산문을 요구하고 헤징과 수동태를 피하라고 한다. 인용 문구: "AI overuses rhetorical devices indiscriminately, which degrades their effectiveness." — [hamel.dev/CLAUDE.html](https://hamel.dev/CLAUDE.html) [검색 스니펫만 확인. 직접 접속 시 404]

**Ethan Mollick** [모두 2차 출처]
- 2026-04-30 보도: 잦은 AI 사용자는 "load bearing" 과 "not X, but Y" 같은 상투어로 AI 산문을 알아본다고 Mollick 이 썼다고 전한다. — [blockchain.news](https://blockchain.news/ainews/ai-writing-tells-exposed-5-phrases-analysis) [집계 사이트, 원문 미확인]
- Mollick 은 em dash 같은 문체 티보다 서사 수준의 티를 다룬 논문을 소개하면서, 문체를 바꾸라고 요청해도 서사 패턴은 잘 바뀌지 않는다고 썼다고 전해진다. — [Google News 집계](https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pnNjVPX0NSSE0tSWpvMFJYcFB5Z0FQAQ) [원문 미확인]
- Mollick 의 1차 글은 찾지 못했다.

**Shreya Shankar** (추가 실무자, 2025-06-16 "Writing in the Age of LLMs")
- "LLMs often overuse bullet points, especially nested ones." / "LLM writing leans heavily on words like this, that, these, and those—often without a clear noun in sight." / "Empty summary sentences feel conclusive, but say nothing." — [sh-reya.com](https://www.sh-reya.com/blog/ai-writing)
- 삼중 구조·헤더·em dash 는 옹호한다: "Em dashes are great for inserting clarifying details, quick shifts, or sharp asides." 길이 원칙: "The contribution is commensurate with the length." — [sh-reya.com](https://www.sh-reya.com/blog/ai-writing)

**기타**
- Peter Huang (DEV, 6월 10일, 연도 미표기): "'Be concise' isn't actionable. It's an aspiration." 대안으로 쓴 규칙: "answer in 3 sentences or fewer unless I explicitly ask you to elaborate" + "No bullet lists in conversational responses". 원칙: "Binary instructions are enforceable; scalar ones get interpreted." — [dev.to/peterverse180](https://dev.to/peterverse180/writing-a-claudemd-that-claude-actually-follows-4llo)

### Inferences
- 실무자들은 "AI 티" 를 어휘 수준에서 구조 수준으로 옮겨 본다. em dash 보다 불릿 과용, 빈 요약 문장, 질문으로 끝내기, 상투어가 더 자주 지목된다.
- Anthropic 내부 인사 2 명 (Thariq, Boris) 과 Willison 은 규칙을 늘리는 대신 줄이고 모델 판단에 맡기는 쪽으로 움직였다. 이는 "no bullets, no summary" 같은 금지 목록 중심 CLAUDE.md 와 상반된다.
- Karpathy 의 처방은 포맷 사다리다. 텍스트 → 다이어그램 → HTML → 영상. 텍스트 단계에서만 통제 언어를 쓴다.

### Gaps
- Karpathy 가 불릿·헤더 과용이나 "slop" 을 직접 비판한 1차 글은 찾지 못했다. X 원문은 402 로 접근 불가했고 미러 (xcancel) 는 451 이었다.
- Mollick, swyx 의 1차 글은 찾지 못했다. swyx 관련 결과는 전혀 없었다.
- Paul Graham 의 2025~2026 AI 산문 관련 에세이는 없다. RSS 피드도 접속 실패했다.
- Boris Cherny 의 개인 CLAUDE.md 내용은 2차 출처가 서로 다르다 (2.5k 토큰 vs 2 줄). 포맷 규칙은 어느 쪽에도 없다.
- Hamel Husain 의 CLAUDE.md 원문 전체는 확인하지 못했다.

## 2. 비 Anthropic 벤더의 공개 사양은 어떤 포맷 규칙을 두나

### Takeaway
OpenAI Model Spec 은 Markdown+LaTeX 를 기본으로 하되 "programmatic" 상황에서는 포맷을 빼라고 하고, 길이는 "thorough but efficient" 로 양쪽 고려사항을 나열한다. GPT-5 계열은 API 기본값이 Markdown 비사용이며 `verbosity` 파라미터와 자연어 길이 지시로 길이를 조절한다. Google 은 Gemini 3 가 기본적으로 "direct and efficient" 하다고 명시한다. xAI 공개 프롬프트는 "shortest answer you can" 과 X 답글용 "under 550 characters", "Do not use markdown formatting" 을 둔다.

### Cited Findings

**OpenAI Model Spec (2025-12-18 판. 페이지에 "A newer version of the Model Spec is available" 표시가 있어 더 새 판이 존재한다)**
- "Use Markdown with LaTeX extensions" (Guideline): "Unless otherwise specified, assistant outputs should be formatted in Markdown with LaTeX extensions. Standard Markdown features can be used, including headings, italics, bold, ~~strikethroughs~~, tables, inline code, and fenced code blocks (which must include a language immediately after the initial triple backticks)." — [model-spec.openai.com/2025-12-18](https://model-spec.openai.com/2025-12-18.html)
- "Be thorough but efficient, while respecting length limits" (Guideline): "There are several competing considerations around the length of the assistant's responses." 긴 쪽 근거: "The assistant should favor producing an immediately usable artifact, such as a runnable piece of code or a complete email message, over a partial artifact that requires further work from the user." 짧은 쪽 근거: "The assistant should avoid writing uninformative or redundant text, as it wastes the users' time (to wait for the response and to read), and it wastes the developers' money (as they generally pay by the token)." — [model-spec.openai.com/2025-12-18](https://model-spec.openai.com/2025-12-18.html)
- "Support the different needs of interactive chat and programmatic use" (Guideline): "In the latter case, the assistant's output generally needs to have a specific structure without surrounding text or formatting." 대화형에서만 허용되는 행동: "Clarifying questions", "Follow-up questions — asking the user if their problem was solved, or if they'd like for the assistant to provide more detail on something", "Placing code inside code blocks (surrounded by triple backticks) even if it's the sole content of the message". — [model-spec.openai.com/2025-12-18](https://model-spec.openai.com/2025-12-18.html)
- "Don't be sycophantic" (User-level): "The assistant exists to help the user, not flatter them or agree with them all the time." / "behave more like a firm sounding board that users can bounce ideas off of — rather than a sponge that doles out praise." — [model-spec.openai.com/2025-12-18](https://model-spec.openai.com/2025-12-18.html)
- "Avoid factual, reasoning, and formatting errors": "If parts of the response are in a specific format (e.g., Markdown, code, JSON, LaTeX), the assistant should adhe[re to that format]". — [model-spec.openai.com/2025-12-18](https://model-spec.openai.com/2025-12-18.html)
- 음성 모드 조항 "Be concise and conversational" 과 "Adapt length and structure to user objectives": "If the user prompt is a clear, discrete question, the assistant should typically answer directly and without a follow-up question." 위반 예시는 사실을 길게 나열하고 질문으로 끝나는 답이다. — [model-spec.openai.com/2025-12-18](https://model-spec.openai.com/2025-12-18.html)
- "don't use headers for short answers" 라는 문구는 이 판에 없다.

**OpenAI GPT-5 / GPT-5.1 / GPT-5.2 프롬프팅 가이드**
- GPT-5 가이드: "By default, GPT-5 in the API does not format its final answers in Markdown, in order to preserve maximum compatibility with developers whose applications may not support Markdown rendering." 추천 프롬프트: "- Use Markdown **only where semantically correct** (e.g., `inline code`, ```code fences```, lists, tables)." / "- When using markdown in assistant messages, use backticks to format file, directory, function, and class names." — [developers.openai.com cookbook](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide) [페이지에 "archived" 표시]
- GPT-5 는 "a new API parameter called verbosity, which influences the length of the model's final answer" 를 도입했고, "GPT-5 is trained to respond to natural-language verbosity overrides in the prompt for specific contexts". 값은 low/medium/high. — [developers.openai.com cookbook](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide); [GPT-5 New Params](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_new_params_and_tools)
- GPT-5.1 가이드: "GPT-5.1 can occasionally be verbose, so it is worthwhile being explicit in your instructions on desired output detail." / "GPT-5.1 adheres well to concrete length guidance". — [developers.openai.com cookbook](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide)
- GPT-5.1 가이드의 코딩 에이전트 예시 `final_answer_formatting`: "Tiny/small single-file change (≤ ~10 lines): 2–5 sentences or ≤3 bullets. No headings." / "Medium change (single area or a few files): ≤6 bullets or 6–10 sentences." / "Large/multi-file change: Summarize per file with 1–2 bullets; avoid inlining code unless critical" / "No multi-section recaps for simple changes; stick to What/Where/Outcome and stop." / "Prefer natural-language references (file/symbol/function) over code fences in the final answer." — [developers.openai.com cookbook](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide)
- GPT-5.1 가이드의 `output_verbosity_spec` 예시: "Respond in plain text styled in Markdown, using at most 2 concise sentences." / "Lead with what you did (or found) and context only if needed." — [developers.openai.com cookbook](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide)
- GPT-5.1 가이드의 이벤트 플래닝 예시: "Most responses should be about 3–6 sentences total." / "Prefer short paragraphs, not bullet lists." / "Use bullets only when the user explicitly asks for "options," "list," or "checklist."" / "long walls of text are discouraged." — [developers.openai.com cookbook](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide)
- GPT-5.1 가이드의 진행 알림 (user updates/preambles): "Send short updates (1–2 sentences) every few tool calls when there are meaningful changes." / "End with a brief recap and any follow-up steps." — [developers.openai.com cookbook](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-1_prompting_guide)
- GPT-5.2: verbosity 는 설정 가능하고 기본값은 medium 이다. low 는 짧은 코드와 최소 주석, medium/high 는 더 긴 구조화된 코드와 인라인 설명을 낸다. — [developers.openai.com GPT-5.2](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.2.md) [검색 요약 경유]
- o-시리즈 추론 모델은 API 에서 Markdown 을 피하도록 학습됐고, 개발자가 "Formatting re-enabled" 문구로 되살렸다. o3/o4-mini 에서 이 방법이 멈췄다는 커뮤니티 보고가 있다. — [community.openai.com](https://community.openai.com/t/o3-o4-mini-restore-markdown-formatting/1230243)

**Google Gemini**
- Gemini API 프롬프트 전략 문서 (최종 수정 2026-10-13): "You can give instructions that specify the format of the response." 예: "formatted as a table, bulleted list, elevator pitch, keywords, sentence, or paragraph". 시스템 지시 예: "All questions should be answered comprehensively with details, unless the user requests a concise response specifically." — [ai.google.dev](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- Gemini 3 절: "Control output verbosity: By default, Gemini 3 models provide direct and efficient answers." / "If you need a more conversational or detailed response, you must explicitly request it in your instructions." — [ai.google.dev](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- 템플릿 예시에 "Verbosity: [Specify Low/Medium/High]" 항목이 있다. few-shot 예시는 포맷을 통일하라고 한다: "Make sure that the structure and formatting of few-shot examples are the same to avoid responses with undesired formats." — [ai.google.dev](https://ai.google.dev/gemini-api/docs/prompting-strategies)
- Gemini 가 XML 태그와 Markdown 둘 다에 잘 반응한다는 서술은 3자 가이드에서만 확인했다. — [philschmid.de](https://www.philschmid.de/gemini-3-prompt-practices) [2차 출처]
- "Gemini for Workspace" 전용 포맷 규칙은 찾지 못했다.

**xAI Grok (공식 리포지토리 xai-org/grok-prompts. 마지막 커밋 2025-11-17)**
- `grok3_official0330_p1.j2`: "* You provide the shortest answer you can, while respecting any stated length and comprehensiveness preferences of the user." 사용자 지정 스타일 블록: "Response Style Guide: - The user has specified the following preference for your response style: "{{custom_personality}}". - Apply this style consistently to all your responses. If the description is long, prioritize its key aspects while keeping responses clear and relevant." — [github.com/xai-org/grok-prompts](https://github.com/xai-org/grok-prompts/blob/main/grok3_official0330_p1.j2)
- `ask_grok_system_prompt.j2` (X 의 @grok 답글용): "- In your final answer, write economically. Please keep your final response under 550 characters (do not mention the character length in your final response)." / "- Do not use markdown formatting." / "- Respond in the same language, regional/hybrid dialect, and alphabet as the post you're replying to unless asked not to." / "- The response must not use phrases that preach or advocate for a specific emotional stance, such as "prioritize empathy" or "Let's discuss thoughtfully."" — [github.com/xai-org/grok-prompts](https://github.com/xai-org/grok-prompts/blob/main/ask_grok_system_prompt.j2)
- `grok4_system_turn_prompt_v8.j2`: 일반 포맷 규칙은 없다. 수학 문제에 대해서만 "in addition to giving the solution in your final response, also explain how to arrive at the solution. Your reasoning should be structured and transparent to the reader." — [github.com/xai-org/grok-prompts](https://github.com/xai-org/grok-prompts/blob/main/grok4_system_turn_prompt_v8.j2)

**Microsoft Copilot / GitHub Copilot**
- Word 용 Copilot 프롬프트로 알려진 문서는 Markdown 으로 가독성을 높이고 수식에 LaTeX 를 쓰며 요청에 따라 응답 길이를 조절하라고 한다. — [mintlify asgeirtj/system_prompts_leaks](https://www.mintlify.com/asgeirtj/system_prompts_leaks/other/copilot) [유출/미검증. 직접 접속 시 410 Gone. 검색 요약만 확인]
- Microsoft 의 사용자용 가이드는 좋은 프롬프트의 4 요소를 목표·맥락·출처·기대 (길이·포맷·톤) 로 설명한다고 2차 출처가 전한다. — [hubsite365](https://www.hubsite365.com/en-ww/crm-pages/the-10-copilot-prompting-rules-that-actually-work.htm) [2차 출처]
- GitHub Copilot 에이전트 모드 프롬프트를 VS Code 1.107 의 Chat Debug 로그에서 해석한 글 (2025-12-27): 톤 "warm, professional, approachable", 길이 "keep it short and structured", "Use **Markdown**", "Wrap symbols in backticks", "Use linkable file paths (workspace-relative) when possible". 글쓴이가 "may contain mistakes" 라고 경고한다. — [dev.to/seiwan-maikuma](https://dev.to/seiwan-maikuma/a-deep-dive-into-github-copilot-agent-modes-prompt-structure-2i4g) [비공식 해석]
- "Keep your answers short and impersonal" 문구는 어느 출처에서도 확인하지 못했다.

### Inferences
- OpenAI 는 기본 포맷을 Model Spec (대화형 Markdown) 과 API (Markdown 비사용) 로 갈라 둔다. 포맷을 요청자가 명시해야 한다는 점은 Google 과 같다.
- 벤더 3 사 (OpenAI, Google, xAI) 모두 "길이는 사용자 지시가 우선" 을 전제한다. 기본값만 다르다. OpenAI 는 medium, Gemini 3 는 direct/efficient, Grok 3 는 shortest.
- OpenAI 의 코딩 에이전트 예시는 변경 크기별 길이 상한을 수치로 둔다. 이는 "be concise" 대신 이진·수치 규칙을 권하는 실무자 조언과 일치한다.

### Gaps
- Model Spec 최신 판 (2025-12-18 이후) 은 확인하지 못했다. WebFetch 가 거부돼 HTML 을 직접 내려받아 2025-12-18 판만 읽었다.
- Microsoft Copilot 공식 시스템 프롬프트는 공개된 것이 없다. 유출본도 직접 열지 못했다.
- Gemini for Workspace 의 포맷 규칙 문서는 찾지 못했다.

## 3. 오픈소스·상용 에이전트 하네스는 최종 메시지 작성 규칙을 어떻게 두나

### Takeaway
Codex CLI 와 Gemini CLI 는 공개 소스에 최종 메시지 규칙을 명시한다. 두 쪽 모두 "매우 간결", "요약 반복 금지", "경로는 백틱" 을 공유한다. Codex 는 플레인 텍스트와 불릿 4~6 개 상한, 중첩 불릿 금지를 둔다. Gemini CLI 는 "3 줄 미만" 과 "변경 후 요약 금지" 를 둔다. Cline 은 결과를 질문이나 추가 제안으로 끝내지 말라고 한다.

### Cited Findings

**OpenAI Codex CLI (공식 리포지토리 `codex-rs/core/gpt-5.1-codex-max_prompt.md`, 마지막 커밋 2026-01-12. `gpt-5.2-codex_prompt.md` 의 같은 절과 내용이 동일함을 diff 로 확인)**
- "## Presenting your work and final message" 도입: "You are producing plain text that will later be styled by the CLI. Follow these rules exactly. Formatting should make results easy to scan, but not feel mechanical. Use judgment to decide how much structure adds value." — [raw.githubusercontent.com/openai/codex](https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/gpt-5.1-codex-max_prompt.md)
- "- Default: be very concise; friendly coding teammate tone." / "- Skip heavy formatting for simple confirmations." / "- Don't dump large files you've written; reference paths only." / "- No "save/copy this file" - User is on the same machine." — 같은 출처
- 코드 변경 보고: "Lead with a quick explanation of the change, and then give more details on the context covering where and why a change was made. Do not start this explanation with "summary", just jump right in." / "If there are natural next steps the user may want to take, suggest them at the end of your response. Do not make suggestions if there are no natural next steps." / "When suggesting multiple options, use numeric lists for the suggestions so the user can quickly respond with a single number." — 같은 출처
- "The user does not command execution outputs. When asked to show the output of a command (e.g. `git show`), relay the important details in your answer or summarize the key lines so the user understands the result." — 같은 출처 (원문 오타 그대로)
- "### Final answer structure and style guidelines": "- Plain text; CLI handles styling. Use structure only when it helps scanability." / "- Headers: optional; short Title Case (1-3 words) wrapped in **…**; no blank line before the first bullet; add only if they truly help." / "- Bullets: use - ; merge related points; keep to one line when possible; 4–6 per list ordered by importance; keep phrasing consistent." / "- Monospace: backticks for commands/paths/env vars/code ids and inline examples; use for literal keyword bullets; never combine with **." / "- Tone: collaborative, concise, factual; present tense, active voice; self‑contained; no "above/below"; parallel wording." / "- Don'ts: no nested bullets/hierarchies; no ANSI codes; don't cram unrelated keywords; keep keyword lists short—wrap/reformat if long; avoid naming formatting styles in answers." / "- Adaptation: code explanations → precise, structured with code refs; simple tasks → lead with outcome; big changes → logical walkthrough + rationale + next actions; casual one-offs → plain sentences, no headers/bullets." — 같은 출처
- 파일 참조: "Use inline code to make file paths clickable." / "Each reference should have a stand alone path. Even if it's the same file." / "Do not use URIs like file://, vscode://, or https://." / "Do not provide range of lines" / 예: "src/app.ts, src/app.ts:42, b/server/index.js#L10, C:\repo\project\main.rs:12:5" — 같은 출처
- 2025-09-16 자 구버전 Codex 프롬프트는 Markdown 으로 상세한 답을 쓰고 인용을 마침표 뒤에 두라고 했다고 전해진다. — [nieta-zjj.github.io (중국어 블로그 재수록)](https://nieta-zjj.github.io/docs/01-博客/宝玉/Codex-system-prompt-（2025-09-16）-89587280) [2차 출처]
- 공식 AGENTS.md 가이드와 agents.md 사이트는 응답 스타일 지침을 전혀 두지 않는다. 내용 예시는 빌드·테스트·PR 규칙만이다. 사이트는 "AGENTS.md is now stewarded by the Agentic AI Foundation under the Linux Foundation." 이라고 밝힌다. — [agents.md](https://agents.md/); [learn.chatgpt.com AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

**Google Gemini CLI (공식 리포지토리 `packages/core/src/prompts/snippets.ts`, 마지막 커밋 2026-09-29)**
- "## Tone and Style": "- **Role:** A senior software engineer and collaborative peer programmer." / "- **High-Signal Output:** Focus exclusively on **intent** and **technical rationale**. Avoid conversational filler, apologies, and [...] mechanical tool-use narration (e.g., "I will now call...")." — [raw.githubusercontent.com/google-gemini/gemini-cli](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/packages/core/src/prompts/snippets.ts)
- "- **Concise & Direct:** Adopt a professional, direct, and concise tone suitable for a CLI environment." / "- **Minimal Output:** Aim for fewer than 3 lines of text output (excluding tool use/code generation) per response whenever practical." / "- **No Chitchat:** Avoid conversational filler, preambles ("Okay, I will now..."), or postambles ("I have finished the changes...") unless they are [...] part of the 'Explain Before Acting' mandate." — 같은 출처
- "- **No Repetition:** Once you have provided a final synthesis of your work, do not repeat yourself or provide additional summaries. For simple or direct requests, prioritize extreme brevity." / "- **Formatting:** Use GitHub-flavored Markdown. Responses will be rendered in monospace." / "- **Tools vs. Text:** Use tools for actions, text output *only* for communication." / "- **Handling Inability:** If unable/unwilling to fulfill a request, state so briefly without excessive justification. Offer alternatives if appropriate." — 같은 출처
- 변경 설명: "- **Explaining Changes:** After completing a code modification or file operation *do not* provide summaries unless asked." 행동 전 설명: "- **Explain Before Acting:** Never call tools in silence. You MUST provide a concise, one-sentence explanation of your intent or strategy immediately before executing tool calls." — 같은 출처
- 계획 제시는 최소 출력 규칙을 덮어쓴다: "When seeking informal agreement on a plan, or any time the user asks to see the plan, you MUST output the full content of the plan in the chat response. This overrides the "Minimal Output" guideline." — 같은 출처
- 공식 문서는 `GEMINI_WRITE_SYSTEM_MD=1` 로 현재 내장 프롬프트를 파일로 쓸 수 있다고 안내한다. — [geminicli.com/docs/cli/system-prompt](https://geminicli.com/docs/cli/system-prompt/)

**Cline** [재수록본, 2024-11-18 게시·2026-07-10 수정. 현재 버전과 대조 못함]
- `attempt_completion` 도구 설명: "Don't end your result with questions or offers for further assistance." RULES 절: "NEVER end attempt_completion result with a question or request to engage in further conversation!" — [zhuang-weiming.github.io](https://zhuang-weiming.github.io/2024/11/18/Code-Robot-Agent-Key-Prompt)
- "You are STRICTLY FORBIDDEN from starting your messages with "Great", "Certainly", "Okay", "Sure"." / "You should NOT be conversational in your responses, but rather direct and to the point." / "It is important you be clear and technical in your messages." — 같은 출처
- 현재 Cline 리포지토리의 프롬프트 파일 경로는 추측한 3 개 모두 비어 있었다. 공식 소스에서 재확인하지 못했다.

**Cursor** [유출/미검증, 2025-04-23 포럼 스레드]
- "Communication Guidelines": "Be conversational but professional." / "Refer to the USER in the second person and yourself in the first person." / "Format your responses in markdown. Use backticks to format file, directory, function, and class names." / "NEVER lie or make things up." / "Refrain from apologizing all the time when results are unexpected." — [forum.cursor.com](https://forum.cursor.com/t/what-we-can-learn-from-the-leaked-cursor-system-prompt-full-text-included/82643)
- 스레드 댓글 1 개는 이 텍스트가 Cline 의 프롬프트라고 주장한다. 다른 댓글은 "only a partial copy" 라고 한다. 두 주장 모두 검증되지 않았다. — 같은 출처
- 2025 년 유출 분석 글은 Cursor 가 "powerful agentic AI coding assistant, powered by Claude 3.5 Sonnet" 페르소나를 쓰고 도구 호출 전 이유를 설명하라고 했다고 전한다. — [patmcguinness.substack.com](https://patmcguinness.substack.com/p/cursor-system-prompt-revealed) [유출/미검증]

**Aider (공식 리포지토리 `aider/coders/editblock_prompts.py`, main 브랜치)**
- "2. Think step-by-step and explain the needed changes in a few short sentences." / "Keep *SEARCH/REPLACE* blocks concise." 그 외 사용자 메시지 포맷 규칙은 없다. — [raw.githubusercontent.com/Aider-AI/aider](https://raw.githubusercontent.com/Aider-AI/aider/main/aider/coders/editblock_prompts.py)

### Inferences
- CLI 하네스는 터미널 렌더링 제약 때문에 Markdown 을 제한한다. Codex 는 "plain text" 를 선언하고 Gemini CLI 는 "rendered in monospace" 를 경고한다. 웹 챗 중심의 Model Spec 과 정반대 방향이다.
- "변경 후 요약 금지" (Gemini CLI) 와 "요약으로 시작 금지" (Codex) 는 공통적으로 작업 결과 보고에서 메타 서술을 빼라는 규칙이다.
- 클릭 가능한 파일 경로 규칙은 Codex, GitHub Copilot 해석본 모두에 있다. CLI/IDE 하네스에서 사용자가 복사할 가치가 높은 규칙이다.

### Gaps
- Cline 과 Cursor 의 현재 공식 프롬프트는 확인하지 못했다. 재수록본만 있다.
- Codex 의 `gpt_5_2_prompt.md` (비 Codex 모델용) 에는 같은 절 제목이 없어 내용을 비교하지 못했다.

## 4. 커뮤니티 CLAUDE.md / AGENTS.md 의 답변 포맷 규칙과 실효성

### Takeaway
커뮤니티에서 반복되는 규칙은 "간결", "아첨 금지", "서두·마무리 군말 금지", "이모지 금지", "불필요 요약 금지" 다. 실효성 보고는 엇갈린다. 이진 규칙은 지켜지고 척도형 규칙은 무시된다는 보고가 있고, 요약·아첨 금지 규칙은 최신 모델 기본값이 이미 그러해서 효과가 없다는 측정도 있다. 파일 구조 변수는 준수율에 유의한 영향이 없었다는 요인 실험이 2026-05 에 나왔다.

### Cited Findings
- Peter Huang 의 실패 규칙: "Be concise in explanations." → 여전히 긴 답. 성공 규칙: "answer in 3 sentences or fewer unless I explicitly ask you to elaborate" + "No bullet lists in conversational responses" + "Do not write an introduction paragraph that summarizes what you're about to do". 상위 3 개 이진 규칙이 "have changed my sessions more than the other 40 instructions combined". — [dev.to/peterverse180](https://dev.to/peterverse180/writing-a-claudemd-that-claude-actually-follows-4llo)
- drona23/claude-token-efficient ("Universal Claude.md"): 8 개 규칙 요약 — "Think first; read files before writing", "Keep output concise", "Prefer targeted edits", "Read each file once unless it changed", "Run tests before finishing", "No flattering preamble/closing fluff", "Favor simple direct fixes", "User instructions always override". — [github.com/drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient)
- 같은 리포지토리의 63% 수치는 5 개 프롬프트 1 회 실행의 단어 수 (465 → 170) 다. 2026-06 재현 벤치마크 (N=5, 실제 토큰) 에서는 haiku 4%, sonnet 12%, opus 7% 감소였다. 리포지토리는 "Current baselines already show 0% preamble, sycophancy, "as an AI," and smart quotes" 라서 이를 겨냥한 규칙은 입력 토큰만 늘린다고 적는다. — [github.com/drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient)
- HumanLayer "Writing a good CLAUDE.md": 프론티어 사고 모델은 약 150~200 개 지시를 일관되게 따른다. HumanLayer 의 루트 CLAUDE.md 는 60 줄 미만이다. — [humanlayer.dev 블로그](https://www.humanlayer.dev/blog/writing-a-good-claude-md) [미러·2차 출처로만 확인]
- Jaroslawicz 등 (2025-07-15, IFScale): "even the best frontier models only achieve 68% accuracy at the max density of 500 instructions." 모델은 "bias towards earlier instructions" 를 보인다. — [arxiv.org/abs/2507.11538](https://arxiv.org/abs/2507.11538)
- McMillan (2026-05-11) 요인 실험: 파일 크기·지시 위치·파일 구조·인접 파일 간 모순 4 변수 중 "None of the four structural variables or three two-way interactions produces a detectable contrast". 크기와 모순은 베이즈 인자로 귀무가설 지지 (BF10 0.05~0.10). 세션 내에서는 "each additional function the agent generates is associated with approximately 5.6% lower odds of compliance per step". — [arxiv.org/abs/2605.10039](https://arxiv.org/abs/2605.10039)
- Thariq (2026-07-24): 대부분의 CLAUDE.md 는 "still walls of hard rules and banned phrases". 스킬에는 "avoid over-constraining except in high-stakes areas". — [x.com/trq212](https://x.com/trq212/status/2080710971228918066) [howborisusesclaudecode.com 경유]
- howborisusesclaudecode.com 의 스킬 팁 목록: "Write it for the model, not humans." / "Give info, not step-by-step scripts." / "Claude already has defaults" 이므로 기본 경로에서 벗어나게 할 것만 쓴다. — [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)
- 커뮤니티 블로그 보고: 약 80 줄을 넘으면 규칙이 빠지고 200 줄을 넘으면 블록 전체가 무시된다. 깊이 묻힌 규칙을 상단으로 옮기고 "must" 를 붙이자 지켜졌다. — [dev.to/dylan_1e07ca370a5576](https://dev.to/dylan_1e07ca370a5576/why-claude-code-ignores-your-claudemd-and-how-to-fix-it-2hip) [일화, 측정 없음]
- 이모지 금지 사례: 한 엄격한 CLAUDE.md 가 "Do not use emojis" 를 두며, 글쓴이는 이를 "more for aesthetics" 라고 설명한다. — [nessimbena.github.io](https://nessimbena.github.io/blogposts/mitigating-claude-code-reward-hacking.html) [2차 출처]
- "You're absolutely right!" 아첨 구문 억제는 anthropics/claude-code 이슈 #3382 가 자주 인용된다. — [neura.market](https://www.neura.market/errors/fix-claude-says-youre-absolutely-right-sycophancy-bug) [2차 출처]
- awesome-claude-code 는 HumanLayer 에세이와 multica-ai/andrej-karpathy-skills (Karpathy 의 공개 메모에서 뽑은 코딩 행동 지침 4 개) 를 수록한다. 처음 100k 자 안에서 답변 포맷 전용 항목은 없었다. — [raw README](https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/refs/heads/main/README.md)
- Simon Willison (2026-07-03): 고정 규칙 대신 "letting the model use its own judgement" 을 택했고, Claude 가 이를 메모리 파일로 저장했다. — [simonwillison.net/tags/thariq-shihipar](https://simonwillison.net/tags/thariq-shihipar/)

### Inferences
- "지켜지는 규칙" 의 공통점은 검증 가능성이다. 문장 수·불릿 유무·서두 단락 유무는 검사할 수 있다. "concise", "clean" 은 검사할 수 없다.
- 아첨·서두 금지 규칙의 효과는 모델 세대에 따라 다르다. 2026 년 중반 Claude 기본값이 이미 0% 라는 측정이 있어, 이런 규칙은 구형 모델 시대의 잔재일 수 있다.
- 구조 실험 (McMillan) 과 지시 수 실험 (Jaroslawicz) 을 합치면, 파일을 어디에 어떻게 두느냐보다 지시 총량과 세션 길이가 준수율을 좌우한다.

### Gaps
- "no summaries at end", "no emojis" 규칙만 따로 측정한 실험은 찾지 못했다.
- besthub.dev 의 "8 Lines… 63%" 글은 로그인 벽 뒤에 있어 읽지 못했다. 같은 수치가 drona23 리포지토리에서 나온 것으로 보인다.
- HumanLayer 원문 페이지는 직접 열지 못했다. 150~200 수치가 Jaroslawicz 논문에서 왔다는 2차 주장은 논문 초록 (500 개에서 68%) 과 직접 맞지 않는다.
- Anthropic 자체 리포지토리의 CLAUDE.md 는 이번 조사 범위에서 확인하지 않았다.

## 5. 통제 언어 (ASD-STE100, 플레인 랭귀지) 를 LLM 에 적용한 사례와 보고

### Takeaway
2026 년 7~10 월 사이 ASD-STE100 을 LLM 출력에 적용하는 흐름이 생겼다. SimpleEnglish 스킬 (HN 363 점), Karpathy 의 10월 2일 글, Menon Lab 글이 축이다. 보고된 효과는 "짧은 문장, 눈에 띄게 적은 slop" 수준의 정성 평가와 저자 자체 벤치마크다. 통제 실험은 없다. 한 줄 지시로 충분하다는 의견과 지시가 곧 드리프트한다는 보고가 함께 있다.

### Cited Findings
- SimpleEnglish 스킬 README (v2.1.1, 벤치마크 폴더 2026-09-02): 채팅 답변 규칙은 "prose only (no headers, bullets, bold, or tables), answer in the first sentence, no em-dashes, briefly define jargon, and no contractions, openers, or closers". 문서 규칙은 지시문 20 단어·설명문 25 단어 상한, 조건 선행, 능동태, should/would/may/might 금지, 한 단어 한 뜻. — [github.com/AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish)
- 같은 README 의 수치: 가시 결함 (em dash, 볼드, 헤더, 불릿) 218 → 11 (95% 감소, 16 개 답변). 린터 위반 81.3% 감소 (9 개 Claude 모델, 144 생성). 문서 재작성 위반 100 단어당 4.09 → 0.91. 저자 주의: 심사자가 Claude 모델이라 가족 편향 가능. 1 셀 1 회 실행. "Output is not STE-certified." — [github.com/AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish)
- HN 스레드 (SimpleEnglish, 363 점, 121 댓글): hsaliak — "Output tokens are precious, be succinct in your responses. Use ASD-STE100 simplified technical english" 가 "all you need". 결과는 "visibly less slop". danielbarla — 문장이 짧아지고 유행어식 절 제목이 줄어 "significant quality increase". — [news.ycombinator.com/item?id=49114639](https://news.ycombinator.com/item?id=49114639)
- 같은 스레드의 반론: lab14 — "STE is part of the training set, so the skill is redundant and only pollutes your context window." Syntaf — 설정에 규칙이 있어도 모델이 "eventually go off the rails". boardwaalk — 지시가 "drift immediately" 하므로 커밋 훅으로 강제하라. solenoid0937 — "It definitely seems like this should be a post processing layer instead of an instruction." thomascountz — STE 는 "will not make something unambiguous simply by replacing words." gillesjacobs — Orwell 의 6 규칙이 STE 스킬보다 나았다는 영상 인용. — [news.ycombinator.com/item?id=49114639](https://news.ycombinator.com/item?id=49114639)
- Karpathy (2026-10-02): "Ask your LLM to explain something in ASD-STE100". 2차 출처는 "80% of the way" 완화 요청을 전한다. — [max.nardit.com](https://max.nardit.com/articles/karpathy-understanding-llm-outputs); [munderdiffl.in](https://munderdiffl.in/blog/asd-ste100-prompting/)
- Menon Lab (Prahlad G. Menon, 2026-10-08): 차용 규칙은 20 단어 상한, 한 문장 한 지시, 능동태·현재형, 명령 동사 시작, 관사 유지, 명사의 동사화 금지, 한 단어 한 뜻 ("obey" 를 "follow" 대신). 핵심 문장: "Flat text has nowhere to hide ambiguity." / "The model hedges because the source hedged." / "Use it where ambiguity is the enemy: instructions, runbooks, agent output you have to act on quickly." / "Do not force a risk discussion or a research summary into it." 정량 결과는 없다. RAG 에서 통제 문체 원문이 더 깨끗하게 검색된다는 경험만 보고한다. — [themenonlab.blog](https://themenonlab.blog/blog/asd-ste100-simplified-technical-english-prompting)
- 같은 글은 Karpathy 가 이 기법을 "released" 했다는 바이럴 프레임이 부정확하다고 지적한다. STE-Prompt 는 Claude Code 용 `/ste` 명령·출력 스타일과 Codex 용 AGENTS.md 절을 담은 MIT 플러그인이다. — [themenonlab.blog](https://themenonlab.blog/blog/asd-ste100-simplified-technical-english-prompting)
- Nardit 의 80% 모드 프롬프트 발췌: "Rewrite the text below in ASD-STE100 Simplified Technical English (Issue 9), about 80% of the way." / "Keep identifiers, commands, paths, error strings, numbers and versions exactly as written." / "Add nothing that is not in the source." / "Do not claim the result is STE-compliant." — [max.nardit.com](https://max.nardit.com/articles/karpathy-understanding-llm-outputs)
- Karpathy 치트시트의 오류가 이미 전파됐다. 한 리포지토리가 시트에서 수치를 가져왔고, 다른 STE 스킬에는 승인 단어 12 개를 금지한 이슈가 열려 있다. — [max.nardit.com](https://max.nardit.com/articles/karpathy-understanding-llm-outputs)
- 파생 스킬: ashryaagr/karpathy-output-style, undefined-ui/explain-skill (STE 텍스트·다이어그램·HTML·영상 사다리). — [github.com/ashryaagr/karpathy-output-style](https://github.com/ashryaagr/karpathy-output-style); [github.com/undefined-ui/explain-skill](https://github.com/undefined-ui/explain-skill)
- 비판: 한 평가자는 세션에 따라 "great for some sessions and very bad for others, especially knowledge work" 라고 보고했다. — [bretkerr.substack.com](https://bretkerr.substack.com/p/the-innocent-prompt-that-contains) [검색 요약 경유]
- 관련 논문 제목만 확인: "The Last Fingerprint: How Markdown Training Shapes LLM Prose" (arXiv 2603.27006). Markdown 중심 학습 데이터가 LLM 산문 특성을 만든다는 주장으로 보인다. — [arxiv.org/pdf/2603.27006](https://arxiv.org/pdf/2603.27006) [초록 미확인]

### Inferences
- ASD-STE100 의 LLM 적용은 "출력 규칙" 과 "입력 원문 규칙" 두 갈래다. Menon 은 원문이 통제 문체면 RAG 답변도 명확해진다고 본다. 이는 이 저장소의 CLAUDE.md 가 지침 문장에 STE 를 적용한 것과 같은 방향이다.
- 가장 신뢰할 수 있는 수치는 SimpleEnglish 의 자체 벤치마크다. 그러나 심사자 편향과 1 회 실행 한계가 있다. 독립 재현은 없다.
- 실무자들은 STE 를 절차·런북·에이전트 보고에 한정하라고 권한다. 뉘앙스·위험 논의·연구 요약에는 맞지 않는다는 데 Menon 과 HN 댓글이 일치한다.

### Gaps
- 플레인 랭귀지 (UK GDS, 미 Plain Writing Act) 를 LLM 프롬프트에 적용한 2024~2026 년 보고는 HN 댓글의 제안 외에 찾지 못했다.
- ASD-STE100 적용의 통제 실험이나 동료 심사 논문은 없다.
- Karpathy 의 10월 2일 X 원문과 첨부 이미지는 직접 보지 못했다. 재수록본과 팩트체크 글에 의존했다.
