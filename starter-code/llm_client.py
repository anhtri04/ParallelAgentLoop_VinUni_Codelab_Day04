"""LLM client factory — OpenAI SDK with any OpenAI-compatible endpoint (DeepSeek default).

Env (.env in starter-code/):
    LLM_API_KEY=sk-...        # or OPENAI_API_KEY / DEEPSEEK_API_KEY
    LLM_BASE_URL=https://api.deepseek.com   # or OPENAI_BASE_URL
    LLM_MODEL=deepseek-chat   # or OPENAI_MODEL
"""

import os
from dotenv import load_dotenv

load_dotenv()  # loads starter-code/.env when CWD or module dir matches


def get_llm_config() -> dict:
    api_key = (
        os.getenv("LLM_API_KEY")
        or os.getenv("OPENAI_API_KEY")
        or os.getenv("DEEPSEEK_API_KEY")
        or ""
    ).strip()
    base_url = (
        os.getenv("LLM_BASE_URL")
        or os.getenv("OPENAI_BASE_URL")
        or "https://api.deepseek.com"
    ).strip()
    model = (
        os.getenv("LLM_MODEL")
        or os.getenv("OPENAI_MODEL")
        or "deepseek-chat"
    ).strip()
    return {"api_key": api_key, "base_url": base_url, "model": model}


def is_llm_configured() -> bool:
    return bool(get_llm_config()["api_key"])


def get_openai_client():
    """Build OpenAI client. Raises RuntimeError if no API key is set."""
    cfg = get_llm_config()
    if not cfg["api_key"]:
        raise RuntimeError(
            "No LLM API key found. Copy starter-code/.env.example to "
            "starter-code/.env and set LLM_API_KEY (DeepSeek key from "
            "https://platform.deepseek.com/api_keys)."
        )
    from openai import OpenAI
    return OpenAI(api_key=cfg["api_key"], base_url=cfg["base_url"]), cfg["model"]
