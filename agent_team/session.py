# @title Define Agent Session and Runner

from .weather_agent import get_agent as get_weather_agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

# --- Session Management ---
# Key Concept: SessionService stores conversation history & state.
# InMemorySessionService is simple, non-persistent storage for this tutorial.
session_service = InMemorySessionService()

# Define constants for identifying the interaction context
APP_NAME = "weather_tutorial_app"
USER_ID = "user_1"
SESSION_ID = "session_001"

# Session is created lazily to avoid asyncio.run() at import time
_session = None
_session_initialized = False

async def get_session():
    """Get or create the session (lazy initialization)."""
    global _session, _session_initialized
    if not _session_initialized:
        _session = await session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            session_id=SESSION_ID
        )
        _session_initialized = True
        print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")
    return _session

# --- Runner ---
# Key Concept: Runner orchestrates the agent execution loop.
runner = Runner(
    agent=get_weather_agent(),
    app_name=APP_NAME,
    session_service=session_service
)
print(f"Runner created for agent '{runner.agent.name}'.")


def get_runner() -> Runner:
    """Returns the configured Runner instance."""
    return runner


def get_user_id() -> str:
    """Returns USER_ID."""
    return USER_ID


def get_session_id() -> str:
    """Returns SESSION_ID."""
    return SESSION_ID
