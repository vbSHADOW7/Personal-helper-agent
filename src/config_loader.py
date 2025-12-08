from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any, Dict

import yaml
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_ROOT / ".env"
CONFIG_PATH = PROJECT_ROOT / "config.yaml"


# Load .env once
if ENV_PATH.exists():
    load_dotenv(ENV_PATH)
else:
    print("Warning: .env not found at project root")


@lru_cache(maxsize=1)
def get_config() -> Dict[str, Any]:
    """Load config.yaml exactly once."""
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"config.yaml not found at: {CONFIG_PATH}")

    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}

    return cfg


CONFIG: Dict[str, Any] = get_config()


def get_agent_config(agent_name: str) -> Dict[str, Any]:
    """
    Return the config dict for a specific agent, merged with app defaults.

    Priority:
      1. agents[agent_name] values
      2. app defaults (e.g. model)
    """
    cfg = get_config()

    # Use `or {}` so None won't break us
    app_cfg: Dict[str, Any] = cfg.get("app") or {}
    agents_cfg: Dict[str, Any] = cfg.get("agents") or {}

    # raw config for this agent (may be missing)
    raw_agent_cfg = agents_cfg.get(agent_name) or {}

    agent_cfg: Dict[str, Any] = dict(raw_agent_cfg)

    # Default model from app if not set
    agent_cfg.setdefault("model", app_cfg.get("model", "gemini-2.5-flash"))

    return agent_cfg
