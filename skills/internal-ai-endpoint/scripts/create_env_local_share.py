#!/usr/bin/env python
import argparse
from pathlib import Path


DEFAULT_BASE_URL = ""
DEFAULT_MODEL = "gemini-3-flash-preview"
DEFAULT_THINKING_BUDGET = "0"


def read_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        values[key.strip()] = value.strip().strip("'\"")
    return values


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create .env.local.share for the internal AI endpoint without copying secrets."
    )
    parser.add_argument("--source", default=".env", help="source env file")
    parser.add_argument("--output", default=".env.local.share", help="output share env file")
    args = parser.parse_args()

    source = Path(args.source)
    output = Path(args.output)
    values = read_env(source)

    base_url = values.get("INTERNAL_BASE_URL") or DEFAULT_BASE_URL
    model = values.get("INTERNAL_MODEL") or DEFAULT_MODEL
    thinking_budget = values.get("INTERNAL_THINKING_BUDGET") or DEFAULT_THINKING_BUDGET

    output.write_text(
        "\n".join(
            [
                "# Shared internal AI endpoint configuration.",
                "# Do not commit or share a real INTERNAL_API_KEY.",
                f"INTERNAL_BASE_URL={base_url}",
                "INTERNAL_API_KEY=",
                "# Recommended default for lightweight analysis:",
                f"INTERNAL_MODEL={model}",
                "# Gemini thinking budget guidance:",
                "# - Use 0 for fast extraction, classification, simple summarization, and boilerplate tasks.",
                "# - Use 0〜1024 for ordinary work that needs some context reasoning.",
                "# - Increase only for hard reasoning/validation because thinking tokens can contribute to token limits.",
                f"INTERNAL_THINKING_BUDGET={thinking_budget}",
                "# Other available examples:",
                "# INTERNAL_MODEL=gemini-3.5-flash",
                "# INTERNAL_MODEL=gemini-3.1-flash-lite",
                "# INTERNAL_MODEL=gemini-3.1-pro-preview",
                "# INTERNAL_MODEL=gpt-5.4-mini",
                "# INTERNAL_MODEL=gpt-5.5",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"Created {output}")
    print("Included: INTERNAL_BASE_URL, INTERNAL_API_KEY placeholder, INTERNAL_MODEL")
    print("Excluded: real INTERNAL_API_KEY")


if __name__ == "__main__":
    main()
