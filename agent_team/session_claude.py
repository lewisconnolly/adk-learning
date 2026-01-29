# @title Define Claude Agent Session and Runner

from .weather_agent_claude import get_agent as get_weather_agent_claude
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

# --- Session Management ---
session_service_claude = InMemorySessionService()

# Define constants for identifying the interaction context
APP_NAME_CLAUDE = "weather_tutorial_app_claude"
USER_ID_CLAUDE = "user_1_claude"
SESSION_ID_CLAUDE = "session_001_claude"

# Session is created lazily to avoid asyncio.run() at import time
_session_claude = None
_session_initialized = False

# Runner is also lazily initialized
_runner_claude = None
_runner_initialized = False


async def get_session():
    """Get or create the Claude session (lazy initialization)."""
    global _session_claude, _session_initialized
    if not _session_initialized:
        _session_claude = await session_service_claude.create_session(
            app_name=APP_NAME_CLAUDE,
            user_id=USER_ID_CLAUDE,
            session_id=SESSION_ID_CLAUDE
        )
        _session_initialized = True
        print(f"Session created: App='{APP_NAME_CLAUDE}', User='{USER_ID_CLAUDE}', Session='{SESSION_ID_CLAUDE}'")
    return _session_claude


def get_runner() -> Runner | None:
    """Returns the configured Runner instance (lazy initialization)."""
    global _runner_claude, _runner_initialized
    if not _runner_initialized:
        try:
            _runner_claude = Runner(
                agent=get_weather_agent_claude(),
                app_name=APP_NAME_CLAUDE,
                session_service=session_service_claude
            )
            print(f"Runner created for agent '{_runner_claude.agent.name}'.")
        except Exception as e:
            print(f"Could not create Claude runner. Check API Key and model name. Error: {e}")
            _runner_claude = None
        _runner_initialized = True
    return _runner_claude


def get_user_id() -> str:
    """Returns USER_ID."""
    return USER_ID_CLAUDE


def get_session_id() -> str:
    """Returns SESSION_ID."""
    return SESSION_ID_CLAUDE
