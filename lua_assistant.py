import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "codellama"

SYSTEM_PROMPT = """You are an expert Lua programming assistant. You help users write, debug, and understand Lua code.

Guidelines:
- Always provide clean, idiomatic Lua code
- Explain your code with clear comments when helpful
- Point out common Lua pitfalls (1-based indexing, nil handling, metatables, etc.)
- When debugging, explain what the bug is and why the fix works
- Format all code in proper markdown code blocks with lua syntax highlighting
"""

history = [{"role": "system", "content": SYSTEM_PROMPT}]


def chat(user_message):
    history.append({"role": "user", "content": user_message})

    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "messages": history,
        "stream": True
    }, stream=True)

    response.raise_for_status()

    full_reply = ""
    print("\nAssistant: ", end="", flush=True)

    for line in response.iter_lines():
        if line:
            data = json.loads(line)
            chunk = data.get("message", {}).get("content", "")
            print(chunk, end="", flush=True)
            full_reply += chunk
            if data.get("done"):
                break

    print("\n")
    history.append({"role": "assistant", "content": full_reply})


def main():
    print("Lua Coding Assistant (powered by CodeLlama)")
    print("Type 'exit' to quit, 'clear' to reset conversation\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        if user_input.lower() == "clear":
            history.clear()
            history.append({"role": "system", "content": SYSTEM_PROMPT})
            print("Conversation cleared.\n")
            continue

        chat(user_input)


if __name__ == "__main__":
    main()
