import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client=Groq(api_key=os.environ.get("GROQ_API_KEY"))

MODEL="llama-3.1-8b-instant"
SYSTEM_PROMPT="You are a helpful assistant, Be concise and clear"

def chat(history: list,user_message: str):
    history.append({"role":"user","content":user_message})

    stream=client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system","content": SYSTEM_PROMPT}]+history,
        temperature=0.7,
        max_tokens=1024,
        stream=True,
    )

    print("\nAssistant: ",end="",flush=True)
    full_response=""
    for chunk in stream:
        token=chunk.choices[0].delta.content
        if token is not None:
            print(token,end="",flush=True)
            full_response+=token
    print("\n")

    history.append({"role": "assistant","content": full_response})

def print_history(history: list):
    if not history:
        print("\nNo History Yet\n")
        return
    print()
    for i,msg in enumerate(history):
        role="You" if msg["role"]=="user" else "Assistant"
        content=msg["content"]
        if len(content)>120:
            content=content[:120]+"..."
        print(f" [{i+1}] {role}: {content}")
    print()

def print_help():
    print("\nCommands:")
    print("  /clear    → wipe conversation history and start fresh")
    print("  /history  → show all messages so far")
    print("  /model    → switch model")
    print("  /help     → show this menu")
    print("  /exit     → quit\n")

def switch_model(current_model: str) -> str:
    models = [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile",
        "meta-llama/llama-4-scout-17b-16e-instruct",
    ]
    print("\nAvailable models:")
    for i, m in enumerate(models):
        marker = " ← current" if m == current_model else ""
        print(f"  [{i+1}] {m}{marker}")
    choice = input("\nPick a number: ").strip()
    try:
        selected = models[int(choice) - 1]
        print(f"Switched to {selected}\n")
        return selected
    except (ValueError, IndexError):
        print("Invalid choice, keeping current model\n")
        return current_model

if __name__=="__main__":
    history=[]
    model=MODEL

    print("=== Multi-turn CLI Chatbot ===")
    print(f"Model: {model}")
    print("Type /help for commands\n")

    while True:
        try:
            user_input=input("You: ").strip()

            if not user_input:
                continue
            elif user_input=="/exit":
                print("Bye!")
                break
            elif user_input=="/clear":
                history=[]
                print("\nHistory Cleared.\n")
            elif user_input=="/history":
                print_history(history)
            elif user_input=="/help":
                print_help()
            elif user_input=="/model":
                model=switch_model(model)
                MODEL=model
            else:
                chat(history,user_input)

        except KeyboardInterrupt:
            print("\nBye!")
            break