import os
import time

from dotenv import load_dotenv
from groq import Groq


load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY is missing from .env"
    )


client = Groq(
    api_key=API_KEY
)


NORMAL_MODEL = os.getenv(
    "GROQ_NORMAL_MODEL",
    "openai/gpt-oss-20b"
)

RESEARCH_MODEL = os.getenv(
    "GROQ_RESEARCH_MODEL",
    "groq/compound-mini"
)


def ask_ai(
    prompt: str,
    system_prompt: str | None = None,
    research_mode: bool = False
) -> str:

    # Hard safety limit on input size.
    # This prevents 413 Request Entity Too Large.
    prompt = str(prompt)[:14000]

    if system_prompt:
        system_prompt = str(system_prompt)[:3000]

    messages = []

    if system_prompt:
        messages.append(
            {
                "role": "system",
                "content": system_prompt
            }
        )

    messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    if research_mode:
        model = RESEARCH_MODEL
        max_tokens = 2200
    else:
        model = NORMAL_MODEL
        max_tokens = 1800

    for attempt in range(3):

        try:

            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.2,
                max_completion_tokens=max_tokens
            )

            return response.choices[0].message.content

        except Exception as error:

            error_text = str(error).lower()

            # Rate limit
            if (
                "429" in error_text
                or "rate limit" in error_text
            ):

                if attempt < 2:
                    time.sleep(20)
                    continue

            # Request too large
            if (
                "413" in error_text
                or "request_too_large" in error_text
                or "request entity too large" in error_text
            ):

                raise RuntimeError(
                    "Groq rejected the request because "
                    "it was too large. The project now "
                    "limits research/document context. "
                    "Please try again."
                )

            raise

    raise RuntimeError(
        "Groq request failed after multiple attempts."
    )