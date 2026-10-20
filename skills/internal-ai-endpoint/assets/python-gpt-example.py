import base64
import os

import requests
from dotenv import load_dotenv


load_dotenv()

base_url = os.environ["INTERNAL_BASE_URL"].rstrip("/")
api_key = os.environ["INTERNAL_API_KEY"]
model = os.getenv("INTERNAL_MODEL", "gpt-5.4-mini")


def image_part(path: str) -> dict:
    mime = "image/png" if path.lower().endswith(".png") else "image/jpeg"
    with open(path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return {
        "type": "input_image",
        "image_url": f"data:{mime};base64,{encoded}",
    }


def extract_text(payload: dict) -> str:
    if isinstance(payload.get("output_text"), str):
        return payload["output_text"]

    texts = []
    for item in payload.get("output", []):
        if item.get("type") != "message":
            continue
        for part in item.get("content", []):
            if part.get("type") == "output_text":
                texts.append(part.get("text", ""))
    return "\n".join(text for text in texts if text)


def generate_text(prompt: str, image_paths: list[str] | None = None) -> str:
    content = [image_part(path) for path in image_paths or []]
    content.append({"type": "input_text", "text": prompt})

    body = {
        "model": model,
        "instructions": "You are a helpful assistant.",
        "input": [{"role": "user", "content": content}],
        "temperature": 0.2,
        "max_output_tokens": 8192,
    }

    response = requests.post(
        f"{base_url}/openai/responses",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=body,
        timeout=180,
        verify=False,
    )
    response.raise_for_status()
    return extract_text(response.json())


if __name__ == "__main__":
    print(generate_text("ping"))
