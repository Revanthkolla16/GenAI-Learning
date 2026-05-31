import os
import argparse
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client=Groq(api_key=os.environ.get("GROQ_API_KEY"))

MODEL="llama-3.3-70b-versatile"

SYSTEM_PROMPTS={
    "default"   : "You are a helpful assistant.",
    "concise"   : "Answer in only one sentence.",
    "expert"    : "You are a senior software engineer with 15 years of experience, Be technical and precise.",
    "eli5"      : "Explain everything like I am 5 years old, Use simple words and analogies.",
    "sarcastic" : "You are a sarcastic assistant, Answer correctly but with dry humor.",
    "scholar"   : "You are a professor who only answers in bullet points"
}

def get_response(user_message: str, system_prompt: str, temperature: float)->str:
    response=client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role":"system", "content":system_prompt},
            {"role":"user","content":user_message}
        ],
        temperature=temperature,
        max_tokens=1024,
        stream=False,
    )
    return response.choices[0].message.content.strip()

def print_divider(label: str="",width: int=60):
    if label:
        pad=(width-len(label)-2)//2
        print(f"\n{'-'*pad}{label}{'-'*pad}")
    else:
        print("-"*width)

def compare_prompts(question:str,temperature:float):
    print(f"\nQuestion: {question}")
    print(f"Temperature: {temperature}")
    print(f"Model: {MODEL}")

    for name,prompt in SYSTEM_PROMPTS.items():
        print_divider(name.upper())
        print(f"System: \"{prompt}\"")
        print()
        response = get_response(question, prompt, temperature)
        print(response)
    
    print_divider()

def compare_temperatures(question: str, system_prompt_name: str):
    temperatures = [0.0, 0.5, 1.0, 1.5]
    prompt = SYSTEM_PROMPTS.get(system_prompt_name, SYSTEM_PROMPTS["default"])
 
    print(f"\nQuestion: {question}")
    print(f"System prompt: {system_prompt_name}")
    print(f"Model: {MODEL}")
 
    for temp in temperatures:
        print_divider(f"TEMPERATURE {temp}")
        response = get_response(question, prompt, temp)
        print(response)
 
    print_divider()

def interactive_mode():
    print("\n=== Prompt Playground ===")
    print("Commands:")
    print("  compare-prompts  → same question across all system prompts")
    print("  compare-temps    → same question across temperatures 0, 0.5, 1.0, 1.5")
    print("  list-prompts     → show available system prompts")
    print("  exit             → quit\n")

    while True:
        cmd = input("Command: ").strip().lower()

        if cmd=="exit":
            break

        elif cmd=="list-prompts":
            print()
            for name,prompt in SYSTEM_PROMPTS.items():
                print(f"{name:<12} -> {prompt}")
            print()
        
        elif cmd=="compare-prompts":
            question=input("Question: ").strip()
            temp = float(input("Temperature (default 0.7): ").strip() or "0.7")
            compare_prompts(question, temp)

        elif cmd=="compare-temps":
            question = input("Question: ").strip()
            print(f"Available prompts: {', '.join(SYSTEM_PROMPTS.keys())}")
            prompt_name = input("System prompt (default: default): ").strip() or "default"
            compare_temperatures(question, prompt_name)

        else:
            print("Unknown command. Try: compare-prompts, compare-temps, list-prompts, exit")

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="Prompt Playground - compare LLM outputs")
    parser.add_argument("--mode",choices=["prompts", "temperatures", "interactive"],default="interactive")
    parser.add_argument("--question",type=str,help="Question to ask")
    parser.add_argument("--temperature",type=float,default=0.7)
    parser.add_argument("--prompt",type=str,default="default")
    args=parser.parse_args()

    if args.mode == "interactive":
        interactive_mode()
    elif args.mode == "prompts":
        if not args.question:
            print("Pass --question when using --mode prompts")
        else:
            compare_prompts(args.question,args.temperature)
    elif args.mode == "temperatures":
        if not args.question:
            print("Pass --question when using --mode temperatures")
        else:
            compare_temperatures(args.question,args.prompt)