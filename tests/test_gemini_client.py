from dotenv import load_dotenv

load_dotenv()

from src.gemini_client import GeminiClient


gemini = GeminiClient()

response = gemini.generate(
    "Say hello"
)

print(response)