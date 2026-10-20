# Endpoint Calling Reference

## Environment

```env
INTERNAL_BASE_URL=
INTERNAL_API_KEY=
# Recommended default for lightweight analysis:
INTERNAL_MODEL=gemini-3-flash-preview
# Gemini thinking budget guidance:
# - Use 0 for fast extraction, classification, simple summarization, and boilerplate tasks.
# - Use 0〜1024 for ordinary work that needs some context reasoning.
# - Increase only for hard reasoning/validation because thinking tokens can contribute to token limits.
INTERNAL_THINKING_BUDGET=0
# Other available examples:
# INTERNAL_MODEL=gemini-3.5-flash
# INTERNAL_MODEL=gemini-3.1-flash-lite
# INTERNAL_MODEL=gemini-3.1-pro-preview
# INTERNAL_MODEL=gpt-5.4-mini
# INTERNAL_MODEL=gpt-5.5
```

Keep `INTERNAL_API_KEY` out of shared files. Put the real key only in a local `.env`.

Use the lightest model that produces reliable output for the task. Reserve pro or newest GPT models for harder reasoning, long synthesis, or validation passes.
For Gemini-family models, set `thinkingBudget` deliberately. A high thinking budget may consume output budget and can make max-token failures more likely.

## Common Headers

```python
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}
```

Some internal environments may need `verify=False` because of certificate handling. Prefer proper CA setup when available.

## Gemini Family

Use this path for model names beginning with `gemini`.

```text
POST {INTERNAL_BASE_URL}/v1beta/models/{INTERNAL_MODEL}:generateContent
```

Minimal body:

```python
body = {
    "systemInstruction": {"parts": [{"text": "You are a helpful assistant."}]},
    "contents": [
        {
            "role": "user",
            "parts": [{"text": "Summarize these product reviews."}],
        }
    ],
    "generationConfig": {
        "temperature": 0.2,
        "maxOutputTokens": 8192,
        "thinkingConfig": {
            "thinkingBudget": 0,
        },
    },
}
```

Image part:

```python
{
    "inlineData": {
        "mimeType": "image/jpeg",
        "data": image_base64,
    }
}
```

Text extraction:

```python
parts = response["candidates"][0]["content"]["parts"]
text = "\n".join(part.get("text", "") for part in parts if part.get("text"))
```

## GPT Family

Use this path for model names beginning with `gpt`.

```text
POST {INTERNAL_BASE_URL}/openai/responses
```

Minimal body:

```python
body = {
    "model": model,
    "instructions": "You are a helpful assistant.",
    "input": [
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Summarize these product reviews."}
            ],
        }
    ],
    "temperature": 0.2,
    "max_output_tokens": 8192,
}
```

Image part:

```python
{
    "type": "input_image",
    "image_url": f"data:image/jpeg;base64,{image_base64}",
}
```

Text extraction:

```python
if isinstance(response.get("output_text"), str):
    text = response["output_text"]
else:
    texts = []
    for item in response.get("output", []):
        if item.get("type") == "message":
            for part in item.get("content", []):
                if part.get("type") == "output_text":
                    texts.append(part.get("text", ""))
    text = "\n".join(t for t in texts if t)
```

## Model Routing

```python
if model.lower().startswith("gemini"):
    # use Gemini generateContent path/body
elif model.lower().startswith("gpt"):
    # use responses path/body
else:
    raise ValueError(f"Unsupported INTERNAL_MODEL: {model}")
```

## Curl Smoke Test

```bash
curl -k -X POST "$INTERNAL_BASE_URL/v1beta/models/$INTERNAL_MODEL:generateContent" \
  -H "Authorization: Bearer $INTERNAL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents":[{"role":"user","parts":[{"text":"ping"}]}]}'
```
