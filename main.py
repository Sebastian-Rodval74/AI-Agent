import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import (
    schema_get_files_info, 
    schema_get_file_content, 
    schema_run_python_file, 
    schema_write_file,
)
from functions.run_python import run_python_file
from functions.calling_function import call_function


load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) < 2 or not sys.argv[1].strip():
    print("Error: A prompt must be provided as a command-line argument.")
    exit(1)

prompt = sys.argv[1]
verbose = "--verbose" in sys.argv

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]

# Add these missing definitions:
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
    ),
)




if response.function_calls:
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose=verbose)
        # Safety check
        part = function_call_result.parts[0]
        if (not hasattr(part, "function_response") or
            not hasattr(part.function_response, "response")):
            raise Exception("Fatal: No function_response.response present!")
        print(part.function_response.response)
        if verbose:
            print(f"-> {part.function_response.response}")
else:
    print(response.text)
