# Lua Coding Assistant

A local AI chatbot specialized in Lua programming, powered by [Ollama](https://ollama.com) and [CodeLlama](https://ollama.com/library/codellama). Runs entirely on your machine — no API keys, no internet required.

## Features

- Lua-focused AI assistant (debugging, writing, explaining code)
- Real-time streaming responses
- Conversation memory within a session
- Runs 100% locally and for free

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed and running
- CodeLlama model pulled

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/Azzam-alanazi/Azzam-lua-AI.git
cd Azzam-lua-AI
```

**2. Install Python dependencies**
```bash
pip install -r requirements.txt
```

**3. Install Ollama**

Download from [https://ollama.com](https://ollama.com) and follow the installer for your OS.

**4. Pull the CodeLlama model**
```bash
ollama pull codellama
```

## Usage

**1. Start Ollama**
```bash
ollama serve
```

**2. Run the assistant**
```bash
python lua_assistant.py
```

**Commands:**

| Command | Description |
|---------|-------------|
| `exit`  | Quit the program |
| `clear` | Reset the conversation history |

## Example

```
Lua Coding Assistant (powered by CodeLlama)
Type 'exit' to quit, 'clear' to reset conversation

You: write a function that reverses a string in Lua