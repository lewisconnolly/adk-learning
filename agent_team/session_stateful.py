# @title 1. Initialize New Session Service and State

# Import necessary session components
from .weather_agent_stateful import get_agent as get_weather_agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner


# Create a NEW session service instance for this state demonstration
session_service_stateful = InMemorySessionService()
print("✅ New InMemorySessionService created for state demonstration.")

# Define a NEW session ID for this part of the tutorial
APP_NAME_STATEFUL = "weather_tutorial_app_stateful"
SESSION_ID_STATEFUL = "session_state_demo_001"
USER_ID_STATEFUL = "user_state_demo"

# Session is created lazily to avoid asyncio.run() at import time
_session_stateful = None
_session_initialized = False

# Runner is also lazily initialized
_runner_stateful = None
_runner_initialized = False

# Define initial state data - user prefers Celsius initially
initial_state = {
    "user_preference_temperature_unit": "Celsius"
}

async def get_session():
    """Get or create the Claude session (lazy initialization)."""
    global _session_stateful, _session_initialized
    if not _session_initialized:
        _session_stateful = await session_service_stateful.create_session(
            app_name=APP_NAME_STATEFUL,
            user_id=USER_ID_STATEFUL,
            session_id=SESSION_ID_STATEFUL,
            state=initial_state
        )
        _session_initialized = True
        print(f"Session created: App='{APP_NAME_STATEFUL}', User='{USER_ID_STATEFUL}', Session='{SESSION_ID_STATEFUL}'")
    return _session_stateful

def get_runner() -> Runner | None:
    """Returns the configured Runner instance (lazy initialization)."""
    global _runner_stateful, _runner_initialized
    if not _runner_initialized:
        try:
            _runner_stateful = Runner(
                agent=get_weather_agent(),
                app_name=APP_NAME_STATEFUL,
                session_service=session_service_stateful
            )
            print(f"Runner created for agent '{_runner_stateful.agent.name}'.")
        except Exception as e:
            print(f"Could not create Claude runner. Check API Key and model name. Error: {e}")
            _runner_stateful = None
        _runner_initialized = True
    return _runner_stateful

def get_user_id() -> str:
    """Returns USER_ID."""
    return USER_ID_STATEFUL

def get_session_id() -> str:
    """Returns SESSION_ID."""
    return SESSION_ID_STATEFUL

def get_session_service() -> InMemorySessionService:
    """Returns the session service."""
    return session_service_stateful