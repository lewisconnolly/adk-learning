# Agent Team - ADK multi-model weather agent
#
# Usage:
#   import asyncio
#   import agent_team
#
#   # Simple usage with default session:
#   asyncio.run(agent_team.chat("What's the weather in London?"))
#

import os
import warnings
import logging
from pathlib import Path

from dotenv import load_dotenv

# --- Initialization ---
warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.ERROR)

# Load environment variables from .env file
load_dotenv(Path(__file__).parent.parent / ".env")

# Configure ADK to use API keys directly (not Vertex AI for this multi-model setup)
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"

print("Environment configured.")
print(f"Google API Key set: {'Yes' if os.environ.get('GOOGLE_API_KEY') else 'No'}")
print(f"Anthropic API Key set: {'Yes' if os.environ.get('ANTHROPIC_API_KEY') else 'No'}")

# --- Imports ---
from .interact import call_agent_async, chat, run_team_conversation, run_stateful_conversation
from .session_stateful import get_session_service as get_session_service_stateful


__all__ = [
    # Interaction functions
    "call_agent_async",
    "chat",
    "run_team_conversation",
    "run_stateful_conversation",
    "get_session_service_stateful",
]
