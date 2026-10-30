# LLM 출력 포맷이 답변 품질과 사용자 인식에 미치는 영향: 문헌 조사 (2023–2026)

조사일: 2026-10-30. 범위: 2023–2026 발표 논문, 벤치마크, 공식 블로그, 공식 문서.
표기 규칙: `[preprint]` 는 동료 심사를 거치지 않은 arXiv 초고다. 숫자는 원문 그대로 적는다. 논문 제목과 인용문은 영어 원문을 유지한다.

---

## 핵심 질문 1. 출력 포맷 제약(JSON·XML·YAML·고정 템플릿)은 추론과 정확도를 떨어뜨리는가, 올리는가

### Takeaway
2024 년 Tam 외 연구는 "엄격한 포맷 제약이 추론 정확도를 크게 떨어뜨린다" 고 보고했다. 2024–2026 년 후속 연구는 이 결론을 부분적으로 수정했다. 하락의 원인은 포맷 자체가 아니라, 프롬프트 불일치, 스키마의 필드 순서(answer 가 reason 보다 먼저), 모델의 여유 용량 부족, 토큰 잘림이다. 공통 처방은 "먼저 자유롭게 추론하고, 마지막에 포맷한다" 다.

### Cited Findings

**원 논문: Tam et al. (2024)**
- 제목: "Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models". 저자: Zhi Rui Tam, Cheng-Kuang Wu, Yi-Lin Tsai, Chieh-Yen Lin, Hung-yi Lee, Yun-Nung Chen. 발표: EMNLP 2024 Industry Track. arXiv v1 2024-08-05, v3 2024-10-14. — [arXiv](https://arxiv.org/abs/2408.02442); [ACL Anthology](https://aclanthology.org/2024.emnlp-industry.91)
- 초록의 핵심 문장: "Surprisingly, we observe a significant decline in LLMs reasoning abilities under format restrictions." 제약이 엄격할수록 추론 과제 하락 폭이 커진다. — [arXiv](https://arxiv.org/abs/2408.02442)
- 세 가지 제약 수준을 비교했다. JSON-mode(constrained decoding), FRI(format-restricting instructions, 프롬프트로 포맷 지시), NL-to-Format(자연어로 먼저 답하고 2단계에서 포맷 변환). — [arXiv HTML v3](https://arxiv.org/html/2408.02442v3)
- GPT-4o-mini 결과(Table 2). GSM8K: NL 94.57, FRI 87.17, JSON-Mode 86.95, JSON-Schema 91.71. Shuffled Objects: NL 82.85, FRI 81.46, JSON-Mode 76.43, JSON-Schema 81.77. Last Letter: NL 83.11, FRI 84.73, JSON-Mode 76.00, JSON-Schema 86.07. — [arXiv HTML v3](https://arxiv.org/html/2408.02442v3)
- 스키마 제약을 더하면 GSM8K 정확도가 급락하는 모델이 있다(Table 1). Claude 3 Haiku JSON 86.99 → 23.44. GPT-3.5 Turbo JSON 74.70 → 49.25. LLaMA 3 8B JSON 64.67 → 48.90. Gemini 1.5 Flash 는 89.66 → 89.21 로 거의 변하지 않았다. — [arXiv HTML v3](https://arxiv.org/html/2408.02442v3)
- 포맷별 비교(Table 9, zero-shot). LLaMA 3 8B Last Letter: Text 70.1, JSON 28.0, XML 15.9, YAML 16.1. GPT-3.5 Turbo GSM8K: Text 76.6, JSON 49.3, XML 45.1, YAML 73.9. 어떤 포맷도 모든 모델에서 일관되게 우세하지 않았다. — [arXiv HTML v3](https://arxiv.org/html/2408.02442v3)
- 분류 과제는 반대 결과다(Table 10). Gemini 1.5 Flash DDXPlus: Text 41.6 → JSON 60.3. GPT-3.5 Turbo DDXPlus: 44.1 → 55.5. 저자는 JSON 이 답 공간을 제한해 분류 정확도를 올린다고 해석했다. — [arXiv HTML v3](https://arxiv.org/html/2408.02442v3)
- JSON-mode 실패 원인: GPT-3.5 Turbo 의 JSON-mode 응답 100% 가 "answer" 키를 "reason" 키보다 먼저 두었다. 모델이 추론 전에 답을 확정했다. — [arXiv HTML v3](https://arxiv.org/html/2408.02442v3)
- 파싱 오류는 주요 원인이 아니다. Gemini 와 GPT-3.5 는 파싱 오류가 0% 에 가깝지만 성능 하락이 있었다. Claude 3 Haiku 의 GSM8K JSON 파싱 오류는 60.07% 였다. — [arXiv HTML v3](https://arxiv.org/html/2408.02442v3)
- 논문 내부 불일치: Table 11 의 GPT-3.5 Last Letter JSON-mode 값(1.78)이 Table 9 의 JSON 값(25.2)과 다르다. 논문은 이 차이를 설명하지 않는다. — [arXiv HTML v3](https://arxiv.org/html/2408.02442v3)

**반박: .txt (dottxt) 블로그 (2024)**
- 제목: "Say What You Mean: A Response to 'Let Me Speak Freely'". 저자: Will Kurt (.txt, Outlines 개발사). 블로그 글이며 동료 심사 없음. 벤더 이해관계가 있다. — [dottxt](https://blog.dottxt.ai/say-what-you-mean.html)
- 주장한 결함 4개. (1) 자유 텍스트 조건과 구조화 조건의 프롬프트가 달랐다. (2) JSON 프롬프트가 스키마 정보를 빠뜨렸다. (3) 답 파싱에 claude-3-haiku 를 "Perfect Text Parser" 로 썼는데 완벽하지 않았다. (4) JSON-mode 와 constrained decoding 을 혼동했다. — [dottxt](https://blog.dottxt.ai/say-what-you-mean.html)
- 재실험(Llama-3-8B-Instruct, Outlines). GSM8K: 비구조화 0.77, 구조화 0.78. Last Letter: 0.73 vs 0.77. Shuffled Objects: 0.41 vs 0.44. 세 과제 모두 구조화가 같거나 높았다. — [dottxt](https://blog.dottxt.ai/say-what-you-mean.html)
- 파서 비교(Last Letter, 자연어 출력): strict regex 0.35, AI parser 0.57, flexible regex 0.61. 파서 선택만으로 26 포인트 차이가 났다. — [dottxt](https://blog.dottxt.ai/say-what-you-mean.html)

**확인·확장 연구 (2026)**
- "Capacity, Not Format: Rethinking Structured Reasoning Failures". 저자: Hengxin Fan. arXiv:2606.09410, 2026-06-08 `[preprint, 단독 저자]`. 4개 모델, 5개 벤치마크. — [arXiv](https://arxiv.org/abs/2606.09410)
  - 여유 용량이 있는 모델은 JSON 제약을 흡수한다. Sonnet MATH-Hard: JSON 88.7±4.0% vs CoT 89.3±1.7%.
  - 한계 근처 모델은 두 경로로 무너진다. Haiku 는 표준 토큰 예산에서 36.2pp 하락(p<0.0001)했고 원인은 주로 잘림(truncation)이다. GPT-4o-mini 는 예산을 늘려 잘림을 없애도 28.0pp 하락(p<0.001)했다. 저자는 이를 "pure capacity competition" 이라 부른다.
  - 프론티어 모델도 면제가 아니다. Opus 4.7 AIME: 96.2% → 91.0%(JSON).
  - 스키마 복잡도에 비례해 불이익이 커진다(McNemar p<0.0001).
  - "delayed-structure" 절제 실험(추론 후 포맷)은 손실의 대부분을 회복했다. 3회 평균 80–87%. 결론: "when a model is near its limits, think first, format later."
- "Structure Tax: How Structured Output affects LLMs Performance". 저자: Vineet Kumar, Kanishka, Bhuvanesh Mandora. arXiv:2610.12056, 2026-10-08. AACL-IJCNLP 2026 Main 채택 표기. — [arXiv](https://arxiv.org/abs/2610.12056)
  - reasoning-first 필드 순서는 자유 형식과 같거나 더 높은 정확도를 낸다. answer-first 순서는 급락을 일으키며 작은 모델에서 더 심하다.
  - 추론 순서를 보존한 스키마는 confidence calibration 도 개선한다. 저자 결론: 문제는 "whether to structure" 가 아니라 "how to structure" 다.
  - 초록 페이지에 모델명과 수치가 없다. 전문 미확인.
- "Thinking Before Constraining: A Unified Decoding Framework for Large Language Models". 저자: Ngoc Trinh Hung Nguyen, Alonso Silva, Laith Zumot, Liubov Tupikina, Armen Aghasaryan, Mehwish Alam. arXiv:2601.07525, v1 2026-01-12, v2 2026-05-28(EMNLP 태그). — [arXiv](https://www.arxiv.org/abs/2601.07525)
  - "In-Writing" 방식: 모델이 제약 없이 추론한 뒤 트리거 토큰을 내면 constrained decoding 으로 전환한다. 조기 트리거(premature triggering)를 "virtually eradicate" 하는 전략을 제안한다.
  - 자연 생성 대비 최대 27% 정확도 향상을 보고한다. 벤치마크 이름과 모델명은 초록에 없다.
- "The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models". arXiv:2604.25359 (2026) `[preprint]`. 스키마 유효성(JSON pass rate)과 값 정확도의 평균 격차가 15–25% 다. GPT-5.4 의 값 정확도는 0.798 이고 GPT-4.1·GPT-5 와 거의 같다. — [arXiv PDF](https://arxiv.org/pdf/2604.25359)
- "StructEval: Benchmarking LLMs' Capabilities to Generate Structural Outputs". 저자: Jialin Yang 외 19인(Wenhu Chen 교신). arXiv:2505.20139, v1 2025-05-26, v3 2026-04-02 `[preprint]`. 18개 포맷, 44개 과제 유형. o1-mini 평균 75.58. 오픈소스는 약 10 포인트 뒤. 생성(generation)이 변환(conversion)보다 어렵다. — [arXiv](https://arxiv.org/abs/2505.20139)
- "FOFO: A Benchmark to Evaluate LLMs' Format-Following Capability". Salesforce Research, ACL 2024. 포맷 준수 능력은 콘텐츠 품질과 별개 능력이다. 오픈소스 모델이 클로즈드 모델보다 뒤진다. 도메인별 편차가 크다. — [arXiv](https://arxiv.org/abs/2402.18667); [ACL](https://preview.aclanthology.org/setup/2024.acl-long.40)
- 공식 문서의 대응. Anthropic 문서는 structured outputs 의 grammar 가 thinking 블록에 적용되지 않는다고 적는다. 원문: "Grammar state resets between sections, allowing Claude to think freely while still producing structured output in the final response." 같은 문서는 "A property that asks for the model's thinking or step-by-step reasoning might lead to a `reasoning_extraction` refusal. Ask for a short explanation instead." 라고 적는다. — [Claude docs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- OpenAI structured outputs 가이드는 `steps` 배열을 `final_answer` 앞에 두는 "chain of thought" 스키마 예시를 보인다. 필드 순서에 관한 명시적 권고 문장은 확인한 범위에 없다. — [OpenAI docs](https://developers.openai.com/api/docs/guides/structured-outputs)

### Inferences
- Tam 외 연구의 "포맷 제약이 추론을 해친다" 는 결론은 2026 년 기준으로 조건부로만 성립한다. 조건은 (a) answer-first 스키마, (b) 모델이 과제 난도의 한계 근처, (c) 토큰 예산 부족, (d) 프롬프트 불일치다.
- 분류·추출 과제에서는 JSON 제약이 오히려 정확도를 올리는 경향이 세 연구(Tam, dottxt, StructEval 의 변환 과제)에서 일관된다.
- 실무 처방은 수렴한다. 자유 추론 → 마지막에 구조화. 또는 스키마에 reasoning 필드를 answer 앞에 둔다.

### Gaps
- Tam 외 연구와 dottxt 반박을 제3자가 독립 재현한 동료 심사 논문을 찾지 못했다.
- "Capacity, Not Format" 과 "Structure Tax" 는 전문을 확인하지 못했다. 모델명·수치가 초록에 일부만 있다.
- Claude 4.x 이후 모델에서 JSON-mode 와 자유 텍스트의 추론 정확도를 직접 비교한 공식(Anthropic) 수치는 찾지 못했다.

---

## 핵심 질문 2. 장황함(verbosity)·길이 편향: LLM 과 평가자(사람·LLM 판정자)는 긴 답을 선호하는가

### Takeaway
LLM 판정자와 보상 모델의 길이 편향은 여러 연구에서 크고 일관되게 측정됐다. 사람도 긴 답을 선호하지만 LLM 판정자보다 약하고, 전문가 평가자가 가장 약하다. Chatbot Arena 는 길이가 markdown 보다 훨씬 큰 스타일 요인이라고 측정했다.

### Cited Findings

**LLM 판정자의 길이 편향**
- "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (Zheng et al., NeurIPS 2023 Datasets & Benchmarks). "repetitive list" 공격(내용 반복으로 길이만 늘림)에 판정자가 속은 비율: GPT-3.5 91.3%, Claude-v1 91.3%, GPT-4 8.7%. 위치 편향 일관성(default prompt): Claude-v1 23.8%, GPT-3.5 46.2%, GPT-4 65.0%. 사람–GPT-4 일치율 85%, 사람–사람 일치율 81%. — [arXiv HTML](https://arxiv.org/html/2306.05685)
- "Verbosity Bias in Preference Labeling by Large Language Models". 저자: Keita Saito, Akifumi Wachi, Koki Wataoka, Youhei Akimoto. arXiv:2310.10076, 2023-10-16. NeurIPS 2023 Instruction Tuning and Instruction Following 워크숍 `[workshop paper]`. 초록: "GPT-4 prefers longer answers more than humans." 편향 측정 지표를 제안하지만 초록에 수치는 없다. — [arXiv](https://arxiv.org/abs/2310.10076); [LY Corp](https://research.lycorp.co.jp/en/publications/1795)
- "Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators". 저자: Yann Dubois, Balázs Galambosi, Percy Liang, Tatsunori B. Hashimoto. COLM 2024. arXiv:2404.04475. GLM 으로 길이 차이를 통제하면 Chatbot Arena 와의 Spearman 상관이 0.94 → 0.98 로 오른다. 저자는 길이 편향이 "significantly gamed by AI systems in ways that human biases would likely not have" 라고 적었다. — [arXiv](https://arxiv.org/abs/2404.04475)
- "Explaining Length Bias in LLM-Based Preference Evaluations". 저자: Zhengyu Hu 외 9인. arXiv:2407.01085, v1 2024-07-01, v5 2025-09-04 `[preprint]`. 승률을 길이 독립 요소 "desirability" 와 길이 의존 요소 "information mass" 로 분해한다. 길이는 주로 information mass 를 통해 평가에 영향을 준다. AdapAlpaca(같은 길이 구간 안에서 비교)를 제안한다. — [arXiv](https://arxiv.org/abs/2407.01085)
- "Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines". 저자: Sadman Kabir Soumik. arXiv:2604.23178, 2026-04 `[preprint, 단독 저자]`. 확장 쌍(expansion pairs)으로 측정한 verbosity bias 는 Llama 3.3-70B +0.44 에서 Claude Sonnet 4 −0.12 까지 분포한다. 즉 Claude 판정자는 긴 답을 약하게 불리하게 봤다. — [arXiv HTML](https://arxiv.org/html/2604.23178)

**보상 모델·RLHF 의 길이 편향**
- "A Long Way to Go: Investigating Length Correlations in RLHF". 저자: Prasann Singhal, Tanya Goyal, Jiacheng Xu, Greg Durrett. COLM 2024. arXiv:2310.03716. 세 helpfulness 선호 데이터셋(WebGPT, Stack, RLCD)에서 길이와 보상이 강하게 상관한다. 길이만으로 만든 보상이 SFT 대비 RLHF 개선의 대부분을 재현한다. 편향의 주 원인은 보상 모델이다. — [arXiv](https://arxiv.org/abs/2310.03716)
- "Loose lips sink ships: Mitigating Length Bias in Reinforcement Learning from Human Feedback" (Shen et al., Findings of EMNLP 2023). 보상 모델이 "misleadingly assuming that humans prefer longer responses" 하는 지름길을 찾는다. Product-of-Experts 로 길이 효과를 분리한다. — [ACL Anthology](https://preview.aclanthology.org/new-sigs/2023.findings-emnlp.188/)

**사람 평가자와 전문가**
- "Style Over Substance: Evaluation Biases for Large Language Models". 저자: Minghao Wu, Alham Fikri Aji. arXiv:2307.03025, v3 2023-11-12 `[preprint, "Work in progress"]`. 검색 요약 인용: "both human and LLM judges often exhibits a bias towards longer responses, where GPT-4 demonstrates the most bias and the expert annotators demonstrate the least bias." 사실 오류가 있는 답이 너무 짧은 답이나 문법 오류 답보다 높게 평가됐다. 초록 페이지에 수치는 없다. — [arXiv](https://arxiv.org/abs/2307.03025)
- "Judging the Judges" 의 소규모 사람 연구: 같은 내용을 markdown 과 평문으로 보였을 때 사람은 markdown 을 약 57% 선호했다. LLM 판정자 5개 중 4개는 73–97% 선호했다. — [arXiv HTML](https://arxiv.org/html/2604.23178)
- "Not Too Short, Not Too Long: How LLM Response Length Shapes People's Critical Thinking in Error Detection". 저자: Natalie Friedman 외 6인. MIRAGE 2026 워크숍(ACM IUI 2026). arXiv:2603.06878. 24명 피험자, 15개 Watson-Glaser 문항. LLM 설명이 틀렸을 때 중간 길이 설명에서 피험자 정답률이 짧거나 긴 설명보다 높았다. 설명이 맞을 때는 길이와 무관하게 정답률이 높았다. 수치는 초록에 없다. — [arXiv](https://arxiv.org/abs/2603.06878)
- "Do Chatbot LLMs Talk Too Much? The YapBench Benchmark". 저자: Vadim Borisov, Michael Gröger, Mina Mikhael, Richard H. Schreiber. arXiv:2601.00624, 2026-01-02 `[preprint]`. 300개 이상 영어 프롬프트, 76개 모델. 짧은 답이 이상적인 질문에서 모델 간 초과 길이 중앙값이 "order-of-magnitude spread" 를 보인다. 실패 유형: 모호한 입력에서 "vacuum-filling", 한 줄 코딩 요청에서 설명·포맷 오버헤드. — [arXiv](https://arxiv.org/abs/2601.00624)

**Chatbot Arena 의 길이 계수**
- LMSYS "Does style matter? Disentangling style and substance in Chatbot Arena" (2024-08-29, Tianle Li·Anastasios Angelopoulos·Wei-Lin Chiang). Bradley-Terry 회귀에 스타일 공변량을 더했다. 계수: 길이 0.249(markdown 과 동시 통제), 0.267(길이만 통제). markdown 리스트 0.031, 헤더 0.024, 볼드 0.019. 원문: 길이가 지배 요인이고 "all other markdown effects are second order." — [LMSYS blog](https://www.lmsys.org/blog/2024-08-28-style-control)

### Inferences
- 길이 편향의 크기는 평가자 유형에 따라 다르다. 약한 LLM 판정자(GPT-3.5, Claude-v1 2023) > GPT-4 > 일반인 > 전문가 순으로 약해진다. 전문가 사용자에게 긴 답의 이점은 작다.
- 사람의 길이 선호는 "정보량" 과 혼재한다. 같은 정보량에서 길이만 늘린 경우 사람의 선호는 LLM 판정자보다 훨씬 약하다.
- 길이 편향은 RLHF 보상 모델을 통해 모델 자체의 장황함으로 전이된다. YapBench 가 이를 사용자 관점에서 측정한다.

### Gaps
- Anthropic·OpenAI 가 공개한, 자사 모델의 길이 편향 또는 응답 길이 변화에 관한 정량 보고서를 찾지 못했다.
- "Style Over Substance", "Verbosity Bias in Preference Labeling" 의 구체 수치(선호율, 편향 지표 값)는 초록에 없어 확인하지 못했다.
- 전문가 사용자를 대상으로 길이 선호를 직접 측정한 2025–2026 연구는 찾지 못했다.
- LMArena 가 2025 년에 style control 을 기본 보기로 전환했다는 정보는 커뮤니티 댓글(Manifold, 2025-05-19)만 있다. 공식 공지는 찾지 못했다. — [Manifold](https://manifold.markets/Bayesian/next-anthropic-model-tops-chatbot-l)

---

## 핵심 질문 3. Markdown·구조 과용("bullet-point disease", 헤더 남발)과 사용자가 실제로 선호하는 형식

### Takeaway
LLM 판정자의 markdown 선호(style bias)는 2026 년 연구에서 가장 큰 편향으로 측정됐다. 사람의 markdown 선호는 약하다(약 57%). Chatbot Arena 데이터에서는 markdown 요소가 승률을 올리지만 길이보다 효과가 작다. Anthropic 은 2026 년 claude.ai 시스템 프롬프트에서 대화·보고서·설명문에 불릿을 쓰지 말라고 명시했다. 챗봇 답변의 산문 대 불릿 이해도를 직접 비교한 통제 연구는 찾지 못했다.

### Cited Findings
- "Judging the Judges" (arXiv:2604.23178, 2026) `[preprint]`. 같은 내용을 markdown 과 평문으로 만든 STYLE 쌍에서 기대 판정은 "tie" 다. 기준선 style bias(+ 는 markdown 선호): Gemini 2.5 Pro +0.76, Gemini 2.5 Flash +0.72, Claude Sonnet 4 +0.68, Llama 3.3-70B +0.40, GPT-4o +0.10. 위치 편향은 전 모델 0.04 이하. 저자는 style bias 를 "the dominant bias" 라 부르고 연구가 거의 없다고 지적한다. — [arXiv HTML](https://arxiv.org/html/2604.23178)
  - 사람은 markdown 을 약 57% 선호했다. LLM 판정자 4개는 73–97% 선호했다. 저자는 격차의 대부분을 편향으로 본다.
  - Chain-of-Thought 판정 지시가 style bias 를 가장 많이 줄였다. Claude 0.68 → 0.49, Gemini Pro 0.76 → 0.60.
  - 주의: v1 요약에서는 style bias 범위를 0.76–0.92 로 적었고, 다른 색인은 0.10–0.76 으로 적는다. 버전 간 수치가 바뀌었을 수 있다. — [SOTAVerified](https://sotaverified.org/papers/260423178)
- NeurIPS 2026 게재 예정 "Label-free detection and mitigation of judge bias": LLM 판정자에 맞춰 학습한 모델이 "superficial judge preferences that reward answers with bullet points, hedged phrasing, or excessive length" 를 악용한다. 초록 외 수치 미확인. — [NeurIPS](https://neurips.cc/virtual/2026/178253)
- LMSYS style control (2024-08-29). markdown 만 통제했을 때 계수: 리스트 0.111, 헤더 0.044, 볼드 0.056. 길이와 동시 통제하면 리스트 0.031, 헤더 0.024, 볼드 0.019 로 줄어든다. markdown 통제 후 순위 변화: gpt-4o-mini 6→11, grok-2-mini 6→15, claude-3-opus 16→8, claude-3-5-sonnet 6→4. Hard Prompt 범주에서 claude-3-5-sonnet 은 2→1 로 chatgpt-4o-latest 와 공동 1위. — [LMSYS blog](https://www.lmsys.org/blog/2024-08-28-style-control)
  - 저자가 적은 한계: 관찰 연구이며 길이와 실질 품질의 상관 같은 혼란 변수를 배제하지 못했다.
- Anthropic 공개 시스템 프롬프트, Claude Opus 4.6 (2026-02-05), `<lists_and_bullets>` 절 원문 발췌. — [Claude docs](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-4-6.md)
  - "Claude avoids over-formatting responses with elements like bold emphasis, headers, lists, and bullet points. It uses the minimum formatting appropriate to make the response clear and readable."
  - "In typical conversations or when asked simple questions Claude keeps its tone natural and responds in sentences/paragraphs rather than lists or bullet points unless explicitly asked for these."
  - "Claude should not use bullet points or numbered lists for reports, documents, explanations, or unless the person explicitly asks for a list or ranking. For reports, documents, technical documentation, and explanations, Claude should instead write in prose and paragraphs without any lists, i.e. its prose should never include bullets, numbered lists, or excessive bolded text anywhere."
  - "Claude should generally only use lists, bullet points, and formatting in its response if (a) the person asks for it, or (b) the response is multifaceted and bullet points and lists are essential to clearly express the information. Bullet points should be at least 1-2 sentences long unless the person requests otherwise."
  - 같은 문서는 이 프롬프트가 API 에는 적용되지 않는다고 적는다. — [Anthropic release notes](https://docs.claude.com/en/release-notes/system-prompts)
- 사용자 선호 직접 연구. "AI Should Be More Human, Not More Complex" (Carlo Esposito, arXiv:2508.04713, 2025-07-27) `[preprint, 산업계 단독 저자]`. 참가자 "10.000 (est.)". 5개 AI 검색 시스템. 사용자가 "overwhelmingly prefer concise, source-attributed responses over elaborate explanations". 방법론·수치·한계가 초록에 없다. 신뢰도 낮음. — [arXiv](https://arxiv.org/abs/2508.04713)
- 교육 분야 소규모 실험(Clayes·Smith, TES 보도). 같은 Macbeth 자료를 평문과 불릿·밑줄 유인물로 제공했다. 평문 그룹이 더 높은 점수와 더 정교한 답을 썼다. 참가자 13명. 챗봇 답변이 아닌 유인물 연구다. — [TES](https://www.tes.com/news/plain-text-works-best)
- YapBench (2026) 는 한 줄 코딩 요청에서 "explanation/formatting overhead" 를 별도 실패 유형으로 분류한다. — [arXiv](https://arxiv.org/abs/2601.00624)

### Inferences
- "bullet-point disease" 의 기계적 원인은 두 겹이다. (1) LLM 판정자가 markdown 을 강하게 선호한다. (2) 그 판정자로 학습하면 모델이 불릿·볼드를 늘린다. 사람의 선호(57%)는 이를 정당화할 만큼 크지 않다.
- Anthropic 의 2026 시스템 프롬프트는 이 문제를 제품 수준에서 인정한 증거로 읽을 수 있다. 다만 프롬프트는 근거 자료를 인용하지 않는다.
- Arena 결과는 "markdown 이 승률을 올린다" 와 "길이가 더 큰 요인이다" 를 동시에 보여 준다. markdown 통제 시 Claude 모델이 오르고 gpt-4o-mini·grok-2-mini 가 내려간 것은 후자 모델들이 포맷 효과를 더 많이 받았음을 시사한다.

### Gaps
- 챗봇 답변을 산문과 불릿으로 동일 내용 제시하고 이해도·과업 성공률을 측정한 동료 심사 HCI 연구를 찾지 못했다.
- "Judging the Judges" 의 사람 연구 규모(n)는 확인하지 못했다.
- OpenAI·Google 의 포맷 과용에 관한 공식 평가 자료는 찾지 못했다.

---

## 핵심 질문 4. LLM 출력의 가독성 측정(Flesch-Kincaid, 문장 길이, 쉬운 말 지표)

### Takeaway
의료 도메인 연구가 가장 많다. 기본 설정의 ChatGPT 답변은 Flesch-Kincaid 9–10 학년 수준이며 권장 6–8 학년을 초과한다. 11개 연구 메타분석에서 ChatGPT(9.82)와 기존 자료(9.54)는 유의한 차이가 없었다. 학년 수준을 지시하면 가독성이 유의하게 개선되지만 목표에 항상 도달하지는 않는다.

### Cited Findings
- 메타분석(안과). Sachdeva K, Chaudry E, Butt FR 외. *Canadian Journal of Ophthalmology*, 2026-08-09 Epub. 1,660편 선별, 57편 포함, 11편 메타분석. 합동 FKGL: ChatGPT 9.82 vs 대조 9.54, 유의 차이 없음. 학년 지시 없을 때 ChatGPT 가 대조보다 유의하게 어려웠다. 학년 지시는 가독성을 유의하게 개선했다. 8학년 이하 LLM 출력은 57편 중 17편(29.82%). 기존 안과 환자 자료는 10.4–12.6 학년. — [Review of Optometry 보도](https://www.reviewofoptometry.com/article/ai-chatbot-responses-on-eye-care-dont-outperform-existing-materials-in-readability)
- PRISMA 기반 문헌 리뷰(Olszewski 외, *Applied Sciences* 2026, doi 10.3390/app16031423). 21개 챗봇, 14개 가독성 척도. FKGL 과 FRE 가 가장 흔한 지표. 대부분 텍스트가 중등~고등 초기 수준이며 권장 8학년을 초과. DeepSeek-V3·R1 이 가장 읽기 쉬웠고 ChatGPT-3.5·Perplexity 가 더 복잡했다. 저자는 정량 합성이 불가능해 체계적 문헌고찰이 아니라고 적었다. MDPI 페이지는 403 으로 직접 확인 실패. — [IPPT 색인](https://www.ippt.pan.pl/en/partners/KlaudiaWatros,9299)
- 피부과 단일 연구. Roster K, Kann RB, Farabi B, Gronbeck C, Brownstone N, Lipner SR. "Readability and Health Literacy Scores for ChatGPT-Generated Dermatology Public Education Materials". *JMIR Dermatology* 2024;7:e50163, 2024-03-06. — [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10955394/)
  - 자외선차단제: 기본 FKGL 9.1(FRE 60.5) → 1회 지시 5.6(69.4) → 2회 지시 3.8(80.2). 6학년 목표 달성.
  - 흑색종: 기본 FKGL 10.5(FRE 46.5) → 1회 지시 8.0(58.9) → 2회 지시 7.9(59.3). 목표 미달.
- 류마티스 (Frontiers in Digital Health 2025). ChatGPT 로 과학 논문을 단순화하면 평균 약 15학년 → 약 10학년. 6학년 목표에는 미달. — [Frontiers](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1623399/full)
- 70개 챗봇 응답을 분석한 2025 연구: 중앙값 가독성 10.4–16.0 학년. 2025 메타합성(Whittaker·Sun): 응답 품질(DISCERN)이 높을수록 가독성이 낮아졌다. 두 건 모두 검색 요약 수준이며 원문 미확인. — [Oxford ORA](https://ora.ox.ac.uk/objects/uuid:6b2b5272-03ff-449a-a903-3fc30bbab20a)
- 모델 간 비교는 연구마다 다르다. 한 2025 의학 연구에서 ChatGPT 4o 의 FRE 가 59.4 로 최고. 치과 연구에서 ChatGPT-5 가 Claude Sonnet 4 보다 FRE 가 높았다. 선천성 갑상선저하증 연구에서 Gemini 가 가장 복잡했다. 텍스트 단순화 연구(JMIR preprint)에서는 Claude 가 5.6 학년으로 가장 낮았다. — [turkmedline](https://turkmedline.net/detay/a-comparative-assessment-of-large-language-models-in-congenital-hypothyroidism-reliability-quality-and-readability/2b0053510264749d/tr/466); [JMIR preprint](https://preprints.jmir.org/preprint/69955/submitted)

### Inferences
- "LLM 답변이 권장 독해 수준을 넘는다" 는 결론은 의료 도메인에서 일관된다. 다만 기존 환자 자료도 같은 수준으로 어렵다. LLM 이 특별히 더 나쁜 것은 아니다.
- 학년 지시는 효과가 있다. 효과 크기는 주제에 따라 FKGL 1.5–5 포인트 사이로 달랐다. 한 번의 지시로 6학년 목표를 보장하지 못한다.
- 품질과 가독성이 음의 상관(Whittaker·Sun)이라는 결과는 "쉽게 쓰라" 는 지시가 정보 손실을 동반할 가능성을 시사한다.

### Gaps
- 법률·교육 도메인의 2023–2026 가독성 연구는 이번 검색에서 찾지 못했다.
- Claude·Gemini 를 포함한 다모델 메타분석은 찾지 못했다. 안과 메타분석은 ChatGPT 만 합동했다.
- 문장 길이나 쉬운 말(plain language) 체크리스트 같은 FKGL 이외 지표를 쓴 LLM 연구는 찾지 못했다.

---

## 핵심 질문 5. 시스템 프롬프트의 포맷 지시와 준수율 (IFEval, FollowBench, InfoBench, ComplexBench, IFBench)

### Takeaway
단일 포맷 제약(단어 수, 불릿 개수, 쉼표 금지, JSON)은 2023 년 GPT-4 가 프롬프트 단위 76.89% 로 따랐다. 제약을 3개 이상 겹치면 준수율이 급락한다. IFEval 점수는 과적합돼 있다. 같은 모델이 새 제약(IFBench)에서는 50 포인트 이상 낮게 나온다. 2025 년 기준 GPT-4.1·Claude 4 Sonnet 도 IFBench 50% 미만이다.

### Cited Findings
- "Instruction-Following Evaluation for Large Language Models" (IFEval). 저자: Jeffrey Zhou, Tianjian Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi Luan, Denny Zhou, Le Hou. arXiv:2311.07911, 2023-11-14 `[preprint, Google]`. 25개 검증 가능 지시 유형, 약 500개 프롬프트. — [arXiv](https://arxiv.org/abs/2311.07911)
  - GPT-4 (2023-11 수집): prompt-level strict 76.89%, inst-level strict 83.57%, prompt-level loose 79.30%, inst-level loose 85.37%.
  - PaLM 2 S (2023-08 수집): prompt-level strict 43.07%, inst-level strict 55.76%, prompt-level loose 46.95%, inst-level loose 59.11%.
  - 범주별 수치는 Figure 3 그래프로만 제공돼 숫자를 추출하지 못했다. — [arXiv PDF](https://arxiv.org/pdf/2311.07911)
- "Generalizing Verifiable Instruction Following" (IFBench). 저자: Valentina Pyatkin, Saumya Malik, Victoria Graf, Hamish Ivison, Shengyi Huang, Pradeep Dasigi, Nathan Lambert, Hannaneh Hajishirzi (Ai2). NeurIPS 2025 Datasets & Benchmarks. arXiv:2507.02833. 58개 새 제약. — [arXiv](https://arxiv.org/abs/2507.02833); [arXiv HTML](https://arxiv.org/html/2507.02833)
  - IFEval → IFBench (prompt-level loose): Tülu 82.4 → 28.9(격차 53.5pt). Tülu-DPO 81.1 → 25.5(55.6pt). Qwen2.5-7B-Instruct 74.7 → 31.3. OLMo2-Instruct 61.7 → 16.7.
  - 본문: GPT-4.1, Claude 3.7 Sonnet, Qwen3-32B, Claude 4 Sonnet 이 IFBench 에서 "below 50%".
  - RLVR 학습 효과: Qwen2.5-7B-Instruct IFEval 74.7 → 89.1, IFBench 31.3 → 45.9. OLMo2 IFBench 16.7 → 44.6(+27.9).
  - 초록 원문: "Even today's strongest models struggle with fulfilling such constraints."
- Artificial Analysis IFBench 리더보드(2026-10 열람): Grok 4.3 (Medium) 83.3%, Grok 4.20 0309 (Reasoning) 82.9%, MiniMax-M3 82.9%. 텍스트에 Claude·GPT-5·Gemini 3 수치가 없었다. — [Artificial Analysis](https://artificialanalysis.ai/evaluations/ifbench)
- "FollowBench: A Multi-level Fine-grained Constraints Following Benchmark for Large Language Models". 저자: Yuxin Jiang 외 9인(Huawei Noah's Ark). arXiv:2310.20410, v3 2024-06-05. 5개 제약 범주: Content, Situation, Style, Format, Example. 판정자 GPT-4-Preview-1106. — [arXiv HTML](https://arxiv.org/html/2310.20410)
  - 전체 평균(레벨 1–5): GPT-4 HSR 73.4%, SSR 77.2%. GPT-3.5 HSR 66.2%, SSR 72.5%.
  - Format 범주: GPT-4 HSR 86.0%, SSR 90.1%. GPT-3.5 HSR 73.3%, SSR 86.2%.
  - 레벨 1 → 5 하락: GPT-4 전체 HSR 84.7% → 61.9%. GPT-3.5 전체 HSR 80.3% → 53.2%. GPT-3.5 Format HSR 90.0% → 50.0%. GPT-4 Format HSR 90.0% → 80.0%.
  - GPT-4·GPT-3.5 는 제약 약 3개까지 연속 충족(CSL≈3). 오픈소스는 약 2개.
- "Benchmarking Complex Instruction-Following with Multiple Constraints Composition" (ComplexBench). arXiv:2407.03978 (THU-COAI, 2024). 4개 제약 유형, 19개 차원, 4개 조합 유형. 의존성 기반 집계. 모델별 수치는 확인하지 못했다. — [arXiv](https://arxiv.org/abs/2407.03978v1)
- 복수 벤치마크 공통 결론(2단계 검색 요약): 제약의 수·조합 깊이·이질성이 늘수록 성능이 급락한다. IFEval 은 표면 제약만 검사하므로 퇴화 전략으로도 점수를 얻는다. — [arXiv 2406.11301](https://arxiv.org/pdf/2406.11301)
- FOFO (ACL 2024): 포맷 요소 하나만 빠져도 실패로 채점한다. 포맷 준수와 콘텐츠 품질은 별개 능력이다. — [arXiv](https://arxiv.org/abs/2402.18667)

### Inferences
- "N 단어로 답하라", "불릿 금지" 같은 단일 제약은 2023 년 GPT-4 급 모델이 약 77–86% 따른다. 2025 년 RLVR 학습 모델은 IFEval 90% 안팎이다. 다만 새 제약 유형에는 45–55% 로 떨어진다.
- 시스템 프롬프트에 포맷 규칙을 여러 개 겹칠수록 전체 동시 준수율은 레벨 5 에서 50–62% 로 떨어진다. 규칙은 적을수록 지켜진다.
- Format 범주는 Situation·Example 보다 쉬운 범주다. 즉 포맷 지시 불이행은 모델 능력 부족보다 제약 누적 때문일 가능성이 크다.

### Gaps
- Claude 4.x·5.x 의 IFEval·IFBench 공식 수치를 1차 출처에서 찾지 못했다. IFBench 논문은 Claude 4 Sonnet 을 "below 50%" 로만 적었다.
- InfoBench, ComplexBench 의 모델별 수치는 확인하지 못했다.
- IFEval 의 제약 유형별(단어 수·불릿 수·쉼표 금지·JSON) 준수율은 그래프로만 제공돼 추출하지 못했다.

---

## 핵심 질문 6. 사고 과정과 최종 답 분리: 자유 추론 후 포맷하는 방식의 근거와 reasoning 모델에서의 유효성

### Takeaway
"먼저 자유롭게 추론하고 마지막에 포맷한다" 는 처방은 2024 년 Tam 외(NL-to-Format)에서 시작해 2026 년 세 연구(Thinking Before Constraining, Capacity Not Format, Structure Tax)가 정량적으로 확인했다. reasoning 모델에서도 유효하다. Anthropic·OpenAI API 는 thinking 블록을 grammar 제약에서 제외해 이 방식을 기본 구조로 채택했다. 다만 프론티어 모델에서는 손실 폭이 작다(Opus 4.7 AIME −5.3pp).

### Cited Findings
- Tam et al. (2024): NL-to-Format(자연어 답변 → 2단계 포맷 변환)이 비제약 성능에 거의 근접했다. JSON-mode 에서 answer 키가 reason 키보다 먼저 나온 비율이 GPT-3.5 Turbo 에서 100% 였다. — [arXiv HTML v3](https://arxiv.org/html/2408.02442v3)
- "Thinking Before Constraining" (2026, EMNLP 태그): 자유 추론 → 트리거 토큰 → constrained decoding. 자연 생성 대비 최대 27% 향상. 조기 트리거를 "virtually eradicate". — [arXiv](https://www.arxiv.org/abs/2601.07525)
- "Capacity, Not Format" (2026) `[preprint]`: delayed-structure 절제 실험이 손실 대부분을 회복(3회 평균 80–87%). 결론 "think first, format later". 프론티어 reasoning 모델 Opus 4.7 도 AIME 에서 96.2% → 91.0% 하락. — [arXiv](https://arxiv.org/abs/2606.09410)
- "Structure Tax" (AACL-IJCNLP 2026): reasoning-first 필드 순서가 자유 형식과 같거나 더 높다. answer-first 순서가 급락을 일으킨다. 추론 순서를 보존한 스키마는 중간 트랜스포머 층에서 정답·오답 표현의 분리도(CKA)가 더 높다. — [arXiv](https://arxiv.org/abs/2610.12056)
- Anthropic 문서: "Grammars apply only to Claude's direct output, not to tool use calls, tool results, or thinking tags (when using thinking). Grammar state resets between sections, allowing Claude to think freely while still producing structured output in the final response." 또한 스키마 안에 추론 필드를 넣으면 `reasoning_extraction` 거부가 날 수 있으니 "Ask for a short explanation instead." — [Claude docs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- Anthropic 문서는 structured outputs 가 message prefilling 과 호환되지 않는다고 적는다. — [Claude docs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- OpenAI 가이드는 `steps`(explanation, output) 배열 뒤에 `final_answer` 를 두는 "chain of thought" 스키마 예시를 제공한다. — [OpenAI docs](https://developers.openai.com/api/docs/guides/structured-outputs)
- "Judging the Judges" (2026): 판정자 측에서도 Chain-of-Thought 지시가 style bias 를 가장 많이 줄였다(Claude 0.68 → 0.49). 즉 "먼저 생각하고 판정" 이 포맷 편향 완화에도 쓰인다. — [arXiv HTML](https://arxiv.org/html/2604.23178)

### Inferences
- reasoning 모델에서는 thinking 이 이미 포맷 제약 밖에서 일어나므로, 최종 답 포맷 제약의 비용이 작다. 그러나 "Capacity, Not Format" 의 Opus 4.7 결과는 비용이 0 이 아님을 보여 준다.
- API 수준에서 thinking 을 grammar 밖에 두는 설계는 두 연구의 "think first, format later" 를 제품에 내장한 형태다. 사용자 쪽 처방은 "스키마에 추론 필드를 넣지 말고 thinking 을 켜라" 로 정리된다.
- 비 reasoning 모델이나 thinking 을 끈 호출에서는 reasoning-first 스키마가 가장 저렴한 대안이다.

### Gaps
- reasoning 모델(o-시리즈, GPT-5, Claude extended thinking)에서 thinking ON 과 OFF 를 나눠 포맷 제약 비용을 비교한 동료 심사 연구를 찾지 못했다.
- "Thinking Before Constraining" 의 벤치마크·모델명·토큰 오버헤드 수치는 전문 미확인이다.
- OpenAI 가이드의 후반부(reasoning 모델 관련 주의)는 읽지 못했다.

---

## 조사 한계 요약
- 2026 년 연구 중 "Capacity, Not Format", "Judging the Judges", "AI Should Be More Human" 은 단독 저자 preprint 다. 수치는 참고용이며 재현 여부가 확인되지 않았다.
- dottxt 반박은 constrained decoding 라이브러리 벤더의 블로그다.
- 사람의 포맷·길이 선호를 대규모로 통제 측정한 1차 연구는 LMSYS style control(관찰 데이터)과 "Judging the Judges" 의 소규모 사람 연구(57%)에 그친다.
- 가독성 연구는 의료 도메인에 편중돼 있다.
