"""
Fikra API — Streaming Inference
https://fikraapi.co.ke

Streaming returns chunks as they are generated rather than waiting for
the full response. Use this for chat interfaces, long-form generation,
or anywhere you want to show output in real time.

Get your free API key at https://fikraapi.co.ke/account/signup
Docs: https://docs.fikraapi.co.ke
"""

import os
import sys
import openai

client = openai.OpenAI(
    base_url="https://api.fikraapi.co.ke/v1",
    api_key=os.environ.get("FIKRA_API_KEY", "your_fikra_api_key"),
)


def stream_completion(
    prompt: str,
    model: str = "fikra-pro-20b",
    system_prompt: str = "You are a helpful assistant.",
) -> str:
    """
    Stream a completion and print chunks as they arrive.
    Returns the full assembled response string when done.
    """
    print(f"[Streaming · {model}]\n")
    print("-" * 40)

    full_response = []
    final_chunk = None

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=True,
    )

    for chunk in response:
        content = chunk.choices[0].delta.content if chunk.choices else ""
        if content:
            sys.stdout.write(content)
            sys.stdout.flush()
            full_response.append(content)
        final_chunk = chunk

    print("\n" + "-" * 40)

    if final_chunk:
        print(f"Model: {final_chunk.model}")

    return "".join(full_response)


def stream_with_callback(
    prompt: str,
    on_chunk,
    model: str = "fikra-pro-20b",
) -> str:
    """
    Stream a completion and call on_chunk(text) for each chunk.
    Useful when integrating into a web framework or WebSocket handler.

    Example:
        def handle_chunk(text):
            websocket.send(text)

        stream_with_callback("Your prompt", on_chunk=handle_chunk)
    """
    full_response = []

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )

    for chunk in response:
        content = chunk.choices[0].delta.content if chunk.choices else ""
        if content:
            on_chunk(content)
            full_response.append(content)

    return "".join(full_response)


if __name__ == "__main__":
    print("Fikra API — Streaming Inference")
    print("=" * 40)

    # Example 1: basic stream to stdout
    print("\n[1] Basic streaming — Pro 20B")
    stream_completion(
        prompt="Explain how M-Pesa changed mobile payments in East Africa.",
        model="fikra-pro-20b",
    )

    # Example 2: stream a longer response with the 120B model
    print("\n\n[2] Long-form streaming — Pro 120B")
    stream_completion(
        prompt=(
            "Write a detailed technical overview of how OpenAI-compatible APIs work, "
            "covering endpoints, authentication, request structure, and streaming."
        ),
        model="fikra-pro-120b",
        system_prompt="You are a senior software engineer writing for a developer audience.",
    )

    # Example 3: stream with callback (simulated WebSocket handler)
    print("\n\n[3] Stream with callback — Fast 8B")
    print("[Fast 8B · callback mode]\n")
    print("-" * 40)

    chunks_received = []

    def collect_chunk(text: str):
        sys.stdout.write(text)
        sys.stdout.flush()
        chunks_received.append(text)

    stream_with_callback(
        prompt="What are the three most important things a developer should know about rate limiting?",
        on_chunk=collect_chunk,
        model="fikra-fast-8b",
    )

    print("\n" + "-" * 40)
    print(f"Received {len(chunks_received)} chunks")
