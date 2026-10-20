import base64
import os

import requests
from dotenv import load_dotenv


load_dotenv()

base_url = os.environ["INTERNAL_BASE_URL"].rstrip("/")
api_key = os.environ["INTERNAL_API_KEY"]
model = os.getenv("INTERNAL_MODEL", "gemini-3-flash-preview")
thinking_budget = int(os.getenv("INTERNAL_THINKING_BUDGET", "0"))


def image_part(path: str) -> dict:
    mime = "image/png" if path.lower().endswith(".png") else "image/jpeg"
    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return {"inlineData": {"mimeType": mime, "data": encoded}}


def generate_text(prompt: str, image_paths: list[str] | None = None) -> str:
    parts = [image_part(path) for path in image_paths or []]
    parts.append({"text": prompt})

    body = {
        "systemInstruction": {
            "parts": [{"text": "You are a helpful assistant."}]
        },
        "contents": [{"role": "user", "parts": parts}],
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 8192,
            "thinkingConfig": {
                "thinkingBudget": thinking_budget,
            },
        },
    }

    response = requests.post(
        f"{base_url}/v1beta/models/{model}:generateContent",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=body,
        timeout=180,
        verify=False,
    )
    response.raise_for_status()
    payload = response.json()
    response_parts = payload["candidates"][0]["content"]["parts"]
    return "\n".join(part.get("text", "") for part in response_parts if part.get("text"))


if __name__ == "__main__":
    print(generate_text("ping"))
