import os
import sys

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Validate environment variables
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    sys.exit("Error: OPENAI_API_KEY is not set in the environment variables")

# Use the environment variable
from openai import OpenAI

client = OpenAI(api_key=api_key)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test in a funny way",
        }
    ],
    model="gpt-4o-mini",
)

# Print the response
print(chat_completion.choices[0].message.content)
