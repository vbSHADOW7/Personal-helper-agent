from __future__ import annotations

from typing import Any, Dict

from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

from ...config_loader import get_agent_config  # 👈 use per-agent config
from ...tools import get_utc_time, calculate_expression




def create_agent() -> LlmAgent:
    cfg: Dict[str, Any] = get_agent_config("assistant")
    app_cfg: Dict[str, Any] = cfg.get("app", {})

    model_name: str = app_cfg.get("model", "gemini-2.5-flash")
    app_timezone: str = app_cfg.get("timezone", "UTC")

    # --- Web search specialist agent ---
#     search_agent = LlmAgent(
#         model=model_name,
#         name="assistant_search_agent",
#         description="Specialist agent that performs Google web searches.",
#         instruction="""
# You are a web research specialist.
#
# - Use the google_search tool to fetch up-to-date factual information.
# - Summarize findings clearly and objectively.
# - If information is uncertain or conflicting, say so explicitly.
# """,
#         tools=[google_search],
#     )
#
#     search_tool = AgentTool(search_agent)

    # --- Main assistant agent (root) ---
    assistant_agent = LlmAgent(
        model=model_name,
        name="assistant_agent",
        description=(
            "General-purpose personal helper that can tell UTC time, "
            "solve math expressions, ."
        ),
        instruction=f"""
You are a helpful personal assistant. you can answer any question. address the user as master.

Capabilities:
- Tell the current time and date in UTC.
- Evaluate expressions using the calculate_expression tool.


Rules:
- Prefer tools over guessing.
- Be concise unless the user asks for more detail.
- Always state that the time is in UTC.
""",
        tools=[
            get_utc_time,
            calculate_expression,
            #search_tool,
        ],
    )

    return assistant_agent


# ADK entrypoint
root_agent = create_agent()
