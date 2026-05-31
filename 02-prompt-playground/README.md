# 02 — Prompt Playground

A CLI tool to run the same question through different system prompts and temperatures side by side — so you can actually see what changes and what doesn't.

## What I built

A terminal tool with two modes:

- **compare-prompts** — sends the same question to 5 different system prompts at the same temperature, prints each response labelled
- **compare-temps** — sends the same question at temperatures 0.0, 0.5, 1.0, and 1.5 with the same system prompt

Both modes run back to back so you can read the diff without switching tabs or re-running anything.

---

## Setup

Same as project 1 — if you already have `.env` with your Groq key you're good.

```bash
pip install groq python-dotenv
```

**Run interactive mode:**
```bash
python main.py
```

**Run directly from CLI:**
```bash
# compare system prompts
python main.py --mode prompts --question "What is recursion?" --temperature 0.7

# compare temperatures
python main.py --mode temps --question "What is recursion?" --prompt expert
```

---

## Code structure

```
02-prompt-playground/
├── main.py          ← everything lives here
├── .env.example
├── requirements.txt
└── README.md
```

Two core functions:

- `compare_prompts(question, temperature)` — loops over the `SYSTEM_PROMPTS` dict, calls `get_response()` for each, prints with a labelled divider
- `compare_temperatures(question, system_prompt_name)` — loops over `[0.0, 0.5, 1.0, 1.5]`, same deal

`get_response()` is non-streaming here — streaming doesn't make sense when you're comparing multiple outputs at once.

The `SYSTEM_PROMPTS` dict at the top is where you add your own. Edit it freely.

---

## What I learned

### System prompts are the most powerful tool you have

Same model, same question, same temperature — completely different output just from changing the system prompt. This project makes that obvious in a way that just reading about it doesn't.

The `eli5` vs `expert` comparison on any technical question is the clearest demo of this. Same facts, totally different framing, vocabulary, and depth.

### Temperature is not magic — it has diminishing returns

The difference between `0.0` and `0.5` is significant. The difference between `1.0` and `1.5` is mostly just noise and degraded coherence. For most real tasks you want somewhere between `0.3` and `0.8`. Above `1.0` is rarely useful.

`temperature=0.0` is underrated — deterministic outputs are what you want when building anything production-facing.

### Non-streaming vs streaming

Project 1 used streaming because it felt good in a chatbot. Here I used non-streaming (`stream=False`) because I need the full response before printing the next one. Choosing between them depends on the use case, not a rule.

### Prompt sensitivity is a real problem

Run compare-prompts on a factual question like "what year was Python created?" — every prompt gives the same answer. Then run it on something ambiguous like "is Go better than Python?" — outputs diverge wildly. That gap between factual and opinionated questions is something you deal with constantly in agentic systems.

### Models I used

| Model | Notes |
|-------|-------|
| `llama-3.1-8b-instant` | Default — fast enough for back-to-back comparisons |
| `llama-3.3-70b-versatile` | Swap in for higher quality comparisons |

---

## Experiments I tried

1. Asked `"explain recursion"` across all 5 system prompts — the `eli5` and `expert` outputs were almost unrecognisable as answers to the same question
2. Asked a coding question at `temperature=0.0` three times — byte-for-byte identical output each time
3. Asked `"write a haiku about APIs"` at temp `0.0` vs `1.5` — at 0 it's clean, at 1.5 it gets weird fast
4. Ran compare-temps on a factual question (`"When did India gain Independence"`) — temperature barely changed the answer, just the phrasing

---

## Key terms

| Term | What it means |
|------|---------------|
| System prompt | Instructions sent before the conversation — shapes tone, format, depth |
| Temperature | Randomness dial — 0 is deterministic, higher is more creative/chaotic |
| Prompt sensitivity | How much the output changes based on how you phrase the input |
| Non-streaming | Wait for the full response before returning — simpler for batch comparisons |

---

*Part of [genai-learning](../README.md) — AI engineering fundamentals through practice.*