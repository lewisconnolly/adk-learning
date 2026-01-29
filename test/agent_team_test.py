if __name__ == "__main__":
    import asyncio
    import sys
    from pathlib import Path

    # Add project root to path
    sys.path.insert(0, str(Path(__file__).parent.parent))
    import agent_team

    try:
        # Simple usage with default session:
        # print("Chatting with gemini-2.5-flash model:")
        # asyncio.run(agent_team.chat("What's the weather in London?"))

        # print("Chatting with claude-sonnet model:")
        # asyncio.run(agent_team.chat("What's the weather in London?", "claude-sonnet"))

        print("Running agent team conversation...")
        asyncio.run(agent_team.run_team_conversation())
    except Exception as e:
        print(f"An error occurred: {e}")