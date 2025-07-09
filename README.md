# 🤖 AI Coding Agent with Google Gemini API

This project implements an intelligent coding agent that uses the Google Gemini API to interpret natural language prompts, analyze Python code, and perform file operations. The agent is capable of listing files, reading content, writing code, executing scripts, and fixing bugs—all through a structured interaction loop with function calls.


## 📁 Project Structure
I-Agent/
│
├── main.py                        # Main execution script for the agent
├── .env                           # Stores your GEMINI_API_KEY (not tracked in version control)
├── calculator/                    # A simple calculator app used for testing
│   ├── main.py
│   ├── tests.py
│   └── pkg/
│       └── calculator.py
├── functions/                     # All helper functions used by the agent
│   ├── calling_function.py        # Handles execution of called functions
│   ├── get_files_info.py          # Lists files and directories
│   ├── new_function.py            # Reads file content safely
│   ├── second_function.py         # Writes content to files
│   └── run_python.py              # Executes Python files with optional arguments


## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/AI-Agent.git
   cd AI-Agent

2.	Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3.	Install dependencies:
pip install -r requirements.txt

4.	Configure your API key:
Create a .env file in the root directory and add your Google Gemini API key:
GEMINI_API_KEY="your_api_key_here"


🚀 How to Use the Agent

You can run the agent with a natural language prompt. For example:
    uv run main.py "fix the bug: 3 + 7 * 2 shouldn't be 20"
You can add --verbose to see debug output:
    uv run main.py "what files are in the calculator directory?" --verbose


🧠 Capabilities

	•	📁 Browse files and folders (with security boundaries)
	•	📝 Read file contents (limited to 10,000 characters)
	•	💾 Write or modify code files
	•	⚙️ Execute Python scripts with arguments
	•	🤖 Understand natural language instructions and map them to function calls


🔐 Security

All file operations are sandboxed to stay within the working_directory. Any attempt to access files outside this boundary is rejected for safety.


🗣️ Example Prompt

In the file pkg/calculator.py, the '+' operator has precedence 3,
which causes incorrect behavior. For example, '3 + 7 * 2' returns 20 instead of 17.
Update the code so that the '+' operator has lower precedence than '*',
and restore the correct order of operations.


📦 Dependencies
	•	google-generativeai
	•	python-dotenv
	•	subprocess, os, sys, typing (built-in)


📌 Notes
	•	The project was developed as part of the Boot.dev backend track.
	•	Do not commit your .env or API keys.
	•	You can extend the agent with new tool functions and schemas.
