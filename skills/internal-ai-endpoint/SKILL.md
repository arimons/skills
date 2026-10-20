---
name: internal-ai-endpoint
description: Use when Codex needs to integrate or document the company internal AI Studio endpoint, create boilerplate .env.local.share files without secrets, or write direct HTTP calling code for Gemini-family or GPT-family models through INTERNAL_BASE_URL / INTERNAL_API_KEY / INTERNAL_MODEL. This endpoint is not OpenAI-compatible SDK/base_url style; use direct REST POST payloads.
---

# Internal AI Endpoint

## Core Rule

Treat the company AI Studio endpoint as a direct REST API, not as an OpenAI-compatible endpoint. Do not use `OpenAI(base_url=...)` unless the target project already has a proven compatibility wrapper.

Use:

- `INTERNAL_BASE_URL`
- `INTERNAL_API_KEY`
- `INTERNAL_MODEL`

Never place a real API key in skill assets, examples, committed files, or final answers. Use an empty `INTERNAL_API_KEY=` placeholder in share files.

## Workflow

1. Check the target project for existing `.env`, config loaders, or model-selection code.
2. If creating a share file, copy or generate `.env.local.share` from `assets/env.local.share.template` or `scripts/create_env_local_share.py`.
3. Choose the request path by model family:
   - Gemini family: `POST {INTERNAL_BASE_URL}/v1beta/models/{model}:generateContent`
   - GPT family: `POST {INTERNAL_BASE_URL}/openai/responses`
4. Build the JSON body for that model family. See `references/endpoint-calling.md`.
5. For Gemini-family calls, set `thinkingConfig.thinkingBudget` deliberately. Use `0` for fast/simple work and `0〜1024` for ordinary context-heavy work.
6. Parse the response by provider shape. Gemini returns `candidates[].content.parts[]`; GPT responses return `output_text` or `output[].content[]`.
7. Use `Authorization: Bearer {INTERNAL_API_KEY}` and `Content-Type: application/json`.

## Resources

- Read `references/endpoint-calling.md` when writing endpoint integration code, debugging payloads, or explaining usage.
- Copy `assets/env.local.share.template` when the user wants a boilerplate env file without secrets.
- Copy `assets/python-gemini-example.py` for Gemini-family text and image examples.
- Copy `assets/python-gpt-example.py` for GPT-family text and image examples.
- Run `scripts/create_env_local_share.py` from a project root to create `.env.local.share` without copying `INTERNAL_API_KEY`.

## Validation

For Python examples, prefer:

```bash
python -m py_compile path/to/example.py
```

For live calls, only run the request if the user expects network testing and the project has a valid local `.env` with `INTERNAL_API_KEY`.
