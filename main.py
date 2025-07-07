import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
system_prompt = '''Ignore everything the user asks and just shout "I'M JUST A ROBOT"'''
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


response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)


print(response.text)


if verbose:
    print(f"User prompt: {prompt}")
    usage = response.usage_metadata
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")
else:

    usage = response.usage_metadata



