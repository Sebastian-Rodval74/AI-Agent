
import os
from dotenv import load_dotenv
from google import genai  # Ensure this library is installed
import warnings
warnings.filterwarnings("ignore")


try:
# Load environment variables from .env file
    load_dotenv()

# Access the GEMINI_API_KEY variable
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Print the API key to verify it's loaded correctly
#print(f"API Key: {GEMINI_API_KEY}")

# Initialize the genai client
    client = genai.Client(api_key=GEMINI_API_KEY)

# Generate content using the API
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)

# Print the generated content
    print(response.text)

# Print token usage metadata
    usage = response.usage_metadata
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")


except Exception as e:
    pass
    # Optionally, you can log the error or handle it as needed