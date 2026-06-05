#!/bin/bash
# Fikra API — curl Reference
# https://fikraapi.co.ke
#
# Set your API key as an environment variable:
#   export FIKRA_API_KEY=your_fikra_api_key
#
# Or replace $FIKRA_API_KEY below with your key directly.
# Get your free key at https://fikraapi.co.ke/account/signup

BASE_URL="https://api.fikraapi.co.ke/v1"

echo "================================================"
echo " Fikra API — curl Examples"
echo " https://fikraapi.co.ke"
echo "================================================"

# ---------------------------------------------------------------------------
# 1. Basic inference — fikra-fast-8b
# ---------------------------------------------------------------------------
echo ""
echo "[1] Basic inference — fikra-fast-8b"
echo "------------------------------------"

curl "$BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIKRA_API_KEY" \
  -d '{
    "model": "fikra-fast-8b",
    "messages": [
      {
        "role": "user",
        "content": "What is the capital of Kenya?"
      }
    ]
  }'

echo ""

# ---------------------------------------------------------------------------
# 2. With system prompt — fikra-pro-20b
# ---------------------------------------------------------------------------
echo ""
echo "[2] With system prompt — fikra-pro-20b"
echo "---------------------------------------"

curl "$BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIKRA_API_KEY" \
  -d '{
    "model": "fikra-pro-20b",
    "messages": [
      {
        "role": "system",
        "content": "You are a concise technical assistant. Keep answers under 3 sentences."
      },
      {
        "role": "user",
        "content": "Explain what an API key is."
      }
    ],
    "temperature": 0.5,
    "max_tokens": 256
  }'

echo ""

# ---------------------------------------------------------------------------
# 3. Streaming — fikra-pro-120b
# ---------------------------------------------------------------------------
echo ""
echo "[3] Streaming — fikra-pro-120b"
echo "--------------------------------"
echo "(chunks arrive in real time)"
echo ""

curl "$BASE_URL/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FIKRA_API_KEY" \
  -d '{
    "model": "fikra-pro-120b",
    "messages": [
      {
        "role": "user",
        "content": "Write a short story about a developer in Nairobi who builds an AI product."
      }
    ],
    "stream": true
  }'

echo ""

# ---------------------------------------------------------------------------
# 4. Check available models
# ---------------------------------------------------------------------------
echo ""
echo "[4] List available models"
echo "--------------------------"

curl "$BASE_URL/models" \
  -H "Authorization: Bearer $FIKRA_API_KEY"

echo ""
echo "================================================"
echo " Docs: https://docs.fikraapi.co.ke"
echo " Sign up: https://fikraapi.co.ke/account/signup"
echo "================================================"
