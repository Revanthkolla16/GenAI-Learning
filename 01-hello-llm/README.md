# 01 — Hello LLM

First contact with an LLM API. Call Groq, stream a response, print it token by token.

## What I built

A minimal Python script that connects to the Groq API, sends a message with a system prompt, and streams the response token by token. Loops so you can keep chatting in the terminal.

No frameworks. No abstractions. Just the raw API.

---

## Setup

**1. Get a free Groq API key**

Go to [console.groq.com](https://console.groq.com), sign up, and create an API key. No credit card needed.

**2. Install dependencies**

```bash
pip install groq python-dotenv
```

**3. Create your `.env` file**

```bash
cp .env.example .env
```

Open `.env` and paste your key:

```env
GROQ_API_KEY=your_key_here
```

**4. Run**

```bash
python main.py
```

---

## Code structure

```
01-hello-llm/
├── main.py          ← everything lives here
├── .env.example     ← copy to .env and add your key
├── requirements.txt
└── README.md
```

`main.py` has one function: `stream_response(user_message, system_prompt)`.

It calls `client.chat.completions.create()` with `stream=True`, then iterates over chunks. Each chunk has a `delta.content` field — that's the next token. Print it immediately with `flush=True` so it shows up in real time instead of buffering.

---

## What I learned

### The `messages` array is the model's entire memory

Every request includes the full conversation as a list:

```python
[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user",   "content": "What is RAG?"},
]
```

The model has no memory of its own — you send everything from scratch on every call. That single fact drives everything else in this roadmap: RAG, agent memory, context windows — all of it is just solving this one problem.

### Three roles: `system`, `user`, `assistant`

- `system` — sets how the model behaves. Most powerful lever you have.
- `user` — what you say.
- `assistant` — what the model previously said (needed for multi-turn conversations).

### Streaming vs non-streaming

Without `stream=True` the API waits for the full response before sending anything back. With streaming you get tokens as they're generated — feels instant in a terminal or UI.

### `temperature` controls randomness

- `0.0` — deterministic, same output every time
- `0.7` — balanced
- `1.0+` — starts getting unpredictable

### `max_tokens` is a hard ceiling

The model stops mid-sentence if it hits the limit. It doesn't affect quality, just length.

### Models I used

| Model | Good for |
|-------|----------|
| `llama-3.1-8b-instant` | Fast, good enough for most tasks |
| `llama-3.3-70b-versatile` | Better reasoning, slower |

---

## Experiments I tried

1. Changed the system prompt to `"Answer every question in exactly one word."` — the model obeyed instantly, shows how much control you have
2. Set `temperature=0`, asked the same question 5 times — identical outputs every time
3. Set `temperature=1.2` — same question, completely different answers each time
4. Swapped to `llama-3.3-70b-versatile` on a reasoning question — noticeably better
5. Removed the system prompt entirely — model still works but feels more generic

---

## Key terms

| Term | What it means |
|------|---------------|
| Token | Unit the model thinks in — roughly 0.75 words |
| Context window | Max tokens the model can see at once (input + output combined) |
| Streaming | Getting output token by token as it's generated |
| System prompt | Instructions that shape model behaviour for the whole conversation |
| Temperature | How random/creative the output is |

---

*Part of [genai-learning](../README.md) — AI engineering fundamentals through practice.*