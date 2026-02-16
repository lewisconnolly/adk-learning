if __name__ == "__main__":
    import asyncio
    import sys
    from pathlib import Path

    # Add project root to path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    import agent_team

    try:
        # Ensure the stateful runner (runner_root_stateful) is available from the previous cell
        # Ensure call_agent_async, USER_ID_STATEFUL, SESSION_ID_STATEFUL, APP_NAME are defined
        
        asyncio.run(agent_team.run_stateful_conversation())        
    except Exception as e:
        print(f"An error occurred: {e}")

