from __future__ import annotations

"""
ADK ENTRYPOINT FILE

Run with:
    adk run src
or:
    adk web src

ADK imports this module as `src.agent`, so we must either:
- use a relative import:    from .agents.assistant import root_agent
  or
- use the full package:     from src.agents.assistant import root_agent

We'll use a relative import for clarity.
"""

from .agents.assistant import root_agent  # noqa: F401
