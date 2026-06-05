"""
Fikra API - Basic Inference Quickstart
https://fikraapi.co.ke

Get your free API key at https://fikraapi.co.ke/account/signup
Docs: https://docs.fikraapi.co.ke
"""

import os
import openai

# ---------------------------------------------------------------------------
# Client setup
# Fikra API is fully OpenAI-compatible — just point base_url at our endpoint.
# Your existing OpenAI code works with this one change.
# ---------------------------------------------------------------------------

client = openai.OpenAI(
    base_url="https://api.fikraapi.co.ke/v1",
    api_key=os.environ.get("FIKRA_API_KEY", "your_fikra_api_key"),
)

# ---------------------------------------------------------------------------
# Available models:
#   fikra-pro-120b  — complex reasoning, long-form generation
#   fikra-pro-20b   — balanced, best for most use cases
#   fikra-fast-8b   — speed, multilingual, high-volume tasks
#   fikra-nano-1b   — edge model (coming soon)
# ---------------------------------------------------------------------------


def basic_completion(prompt: str, model: str = "fikra-pro-20b") -> str:
    """Send a single prompt and return the response text."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


def completion_with_options(
    prompt: str,
    system_prompt: str = "You are a helpful assistant.",
    model: str = "fikra-pro-20b",
    temperature: float = 0.7,
    max_tokens: int = 512,
) -> dict:
    """
    Full inference call with common options.
    Returns the full response object as a dict for inspection.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return {
        "content": response.choices[0].message.content,
        "model": response.model,
        "usage": {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
        },
    }


if __name__ == "__main__":
    print("Fikra API — Basic Inference")
    print("=" * 40)

    # Example 1: simple prompt
    print("\n[1] Simple prompt")
    result = basic_completion("Write a haiku about writing code.")
    print(result)

    # Example 2: full options with token usage
    print("\n[2] With options — shows token usage")
    result = completion_with_options(
        prompt="Explain what an API is in two sentences, for a non-technical founder.",
        system_prompt="You are a concise technical writer.",
        model="fikra-fast-8b",
        temperature=0.5,
        max_tokens=128,
    )
    print(f"Response: {result['content']}")
    print(f"Model:    {result['model']}")
    print(f"Tokens:   {result['usage']['total_tokens']} total "
          f"({result['usage']['prompt_tokens']} prompt + "
          f"{result['usage']['completion_tokens']} completion)")

    # Example 3: try the 120B model
    print("\n[3] Fikra Pro 120B — complex reasoning")
    result = basic_completion(
        "What are three practical ways a small Kenyan business could use AI today?",
        model="fikra-pro-120b",
    )
    print(result)
