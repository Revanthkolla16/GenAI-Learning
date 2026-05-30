import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client=Groq(api_key=os.environ.get("GROQ_API_KEY"))

def stream_response(user_message:str,system_prompt:str="You are a helpful assistant"):
    stream=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"system","content":system_prompt},
            {"role":"user","content":user_message}
        ],
        temperature=1.2,
        max_tokens=1024,
        stream=True
    )

    print("\nAssistant: ",end="",flush=True)
    for chunk in stream:
        token=chunk.choices[0].delta.content
        if token is not None:
            print(token,end="",flush=True)
    print("\n")

if __name__ == "__main__":
    print("===Hello LLM===")
    print("Type your message, Ctrl+C to exit")

    while True:
        try:
            user_input=input("You: ").strip()
            if not user_input:
                continue
            stream_response(user_input)
        except KeyboardInterrupt:
            print("\nThank You!")
            break