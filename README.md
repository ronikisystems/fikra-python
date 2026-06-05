# fikra-python

Python quickstart and examples for [Fikra API](https://fikraapi.co.ke) - the OpenAI-compatible AI inference API built for African developers.

[![Product Hunt](https://img.shields.io/badge/Product%20Hunt-Fikra%20API-FF4500?style=flat&logo=producthunt&logoColor=white)](https://www.producthunt.com/posts/fikra-api)
[![Fikra API](https://img.shields.io/badge/Fikra%20API-fikraapi.co.ke-FF4500?style=flat)](https://fikraapi.co.ke)
[![Built by Roniki Systems](https://img.shields.io/badge/Built%20by-Roniki%20Systems-1A1A1A?style=flat)](https://linkedin.com/company/roniki-systems-ltd)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat)](LICENSE)

---

Fikra API gives developers across East Africa and beyond access to powerful AI inference without the usual barriers - no Stripe account required, no $20 minimums, no VPN. Pay with M-Pesa and local payment apps. Start from KES 130. Get 2 million tokens per dollar.

This repo contains everything you need to get started in under 5 minutes.

---

## Models

| Model | Best for |
|---|---|
| `fikra-pro-120b` | Complex reasoning, long-form generation |
| `fikra-pro-20b` | Balanced, best for most use cases |
| `fikra-fast-8b` | Speed, multilingual, high-volume tasks |
| `fikra-nano-1b` | Edge deployment *(coming soon)* |

---

## Quickstart

### 1. Get your API key

Create a free account at [fikraapi.co.ke](https://fikraapi.co.ke/account/signup). You get **2 million free tokens** on signup during the launch period - no card required.

### 2. Install the OpenAI SDK

Fikra API is fully OpenAI-compatible. No new SDK to install.

```bash
pip install openai
```

### 3. Make your first call

```python
import openai

client = openai.OpenAI(
    base_url="https://api.fikraapi.co.ke/v1",
    api_key="your_fikra_api_key"
)

response = client.chat.completions.create(
    model="fikra-pro-20b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about writing code."}
    ]
)

print(response.choices[0].message.content)
```

That's it. If you were already using OpenAI, the only change is `base_url`.

---

## Examples in this repo

| File | Description |
|---|---|
| [`quickstart.py`](quickstart.py) | Basic inference — single request, single response |
| [`streaming.py`](streaming.py) | Streaming inference — chunks arrive in real time |
| [`curl_examples.sh`](curl_examples.sh) | curl reference for all three models |
| [`env_example.txt`](env_example.txt) | Environment variable setup |

---

## Migrating from OpenAI

If your existing code uses the OpenAI Python SDK, switching to Fikra API is a one-line change:

```python
# Before
client = openai.OpenAI(api_key="sk-...")

# After — everything else stays the same
client = openai.OpenAI(
    base_url="https://api.fikraapi.co.ke/v1",
    api_key="your_fikra_api_key"
)
```

All OpenAI SDK features work as expected: streaming, system prompts, temperature, max_tokens, and any language with an HTTP client.

---

## Rate limits

| Tier | Limit |
|---|---|
| Free (unverified) | 30 requests/minute |
| Trusted (after first top-up) | 100 requests/minute |

---

## Links

- **Website:** [fikraapi.co.ke](https://fikraapi.co.ke)
- **Documentation:** [docs.fikraapi.co.ke](https://docs.fikraapi.co.ke)
- **Product Hunt:** [producthunt.com/posts/fikra-api](https://www.producthunt.com/posts/fikra-api)
- **Builder:** [James Miano on LinkedIn](https://linkedin.com/in/jamesmiano)
- **Built by:** [Roniki Systems](https://linkedin.com/company/roniki-systems-ltd) · Nairobi, Kenya
- **Indie Hackers:** [indieHackers.com/r/fikra-api](https://www.indiehackers.com)

---

## Contributing

Issues and PRs welcome. If you build something with Fikra API, open a PR to add it to the examples.

---

*Built in Nairobi. Designed for developers in markets that mainstream AI platforms ignore.*
