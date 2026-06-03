# 03 — Multi-turn CLI Chatbot

A terminal chatbot that actually remembers what you said. Conversation history, /clear, /history, and model switching

## What I built

A CLI chatbot that maintains a running conversation history across turns. Each message gets appended to a list that's sent with every API call — so the model always has full context of what was said before.

Commands:
- `/clear` — wipe the history and start fresh
- `/history` — print all messages so far, truncated for readability
- `/model` — switch between models mid-conversation
- `/help` — show the command menu
- `/exit` — quit

---

## Setup

Same `.env` and `requirements.txt` as projects 01 and 02.

```bash
pip install groq python-dotenv
python main.py
```

---

## Code structure

```
03-cli-chatbot/
├── main.py
├── .env.example
├── requirements.txt
└── README.md
```

Everything is in `main.py`. One core function — `chat(history, user_message)`:

1. Appends the user message to `history`
2. Sends `[system prompt] + history` to the API
3. Streams the response token by token
4. Appends the assistant's full response to `history`
5. Returns the response

The `history` list is the entire implementation of memory. That's it.

---

## What I learned

### Memory is just a list you manage yourself

This is the whole project in one sentence. The model has no memory — you maintain a list of `{"role": ..., "content": ...}` dicts and send the full list on every call. The model sees the whole conversation each time and responds in context.

```python
history = [
    {"role": "user",      "content": "My name is Revanth"},
    {"role": "assistant", "content": "Nice to meet you, Revanth!"},
    {"role": "user",      "content": "What's my name?"},
]
# Model correctly answers "Revanth" because it sees the full history
```

### Context window fills up

Every message you add makes the next API call more expensive (more tokens) and eventually hits the model's context limit. Real applications handle this by:
- **Summarising** old messages and replacing them with a summary
- **Sliding window** — keep only the last N messages
- **Selective memory** — store important facts separately, drop the rest

This project doesn't handle it — but understanding *why* it's a problem is the point.

### System prompt stays out of history

The system prompt is sent on every call but never stored in `history`. It's always prepended fresh:

```python
messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history
```

This means you can change the system prompt mid-conversation without it appearing in history — clean separation between instructions and conversation.

### Streaming + accumulation

Project 01 streamed and threw tokens away. Here I accumulate them into `full_response` while streaming, so I can append the complete assistant message to history after the stream ends. Both things at once — streaming output for UX, full string for state management.

```python
full_response = ""
for chunk in stream:
    token = chunk.choices[0].delta.content
    if token is not None:
        print(token, end="", flush=True)  # stream to terminal
        full_response += token            # accumulate for history
```

### Models I used

| Model | Notes |
|-------|-------|
| `llama-3.1-8b-instant` | Default — fast, good for casual conversation |
| `llama-3.3-70b-versatile` | Noticeably better at following long conversation context |
| `meta-llama/llama-4-scout-17b-16e-instruct` | Best context retention across long chats |

---

## Experiments I tried

1. Told the bot my name at turn 1, asked it 10 messages later — it remembered because the full history was in context
2. Hit `/clear` mid-conversation and asked the same question — model had no memory of earlier turns, confirmed history is just the list
3. Had a long back-and-forth (~20 turns) and watched the API calls get slower — more tokens in context = slower response
4. Switched from `llama-3.1-8b` to `llama-3.3-70b` mid-conversation — history carried over perfectly, model picked up the context immediately
5. Changed `SYSTEM_PROMPT` to `"You are a pirate. Stay in character always."` — model stayed in character across all turns because the system prompt persists

---

## Key terms

| Term | What it means |
|------|---------------|
| Conversation history | The list of past messages sent with every API call |
| Multi-turn | A conversation that spans more than one exchange |
| Context accumulation | History growing larger with every turn, consuming more tokens |
| Sliding window | Dropping old messages to keep context size manageable |
| Stateless API | The API remembers nothing — all state lives in your code |

---

*Part of [genai-learning](../README.md) — AI engineering fundamentals through practice.*