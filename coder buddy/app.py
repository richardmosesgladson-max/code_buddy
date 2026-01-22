import ollama
from prompts import SYSTEM_PROMPT

def run_coder(user_prompt):
    response = ollama.chat(
        model="tinyllama:latest",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response["message"]["content"]

print("🤖 Coder Buddy is ready! (type 'exit' to quit)")

while True:
    user_prompt = input("\nEnter your prompt: ")

    if user_prompt.lower() == "exit":
        print("👋 Exiting Coder Buddy. Happy coding!")
        break

    output = run_coder(user_prompt)
    print("\n--- Coder Buddy Response ---\n")
    print(output)
