import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL = MODEL = "openai/gpt-oss-120b"

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


def banner(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)
    print()