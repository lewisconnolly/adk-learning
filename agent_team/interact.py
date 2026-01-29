# @title Define Agent Interaction Function
from google.genai import types # For creating message Content/Parts

async def call_agent_async(query: str, runner, user_id, session_id):
    """Sends a query to the agent and prints the final response.

    Args:
        query: The user's question or request.
        runner: The ADK Runner instance.
        user_id: The user identifier for the session.
        session_id: The session identifier.

    Returns:
        The agent's response text.
    """
    print(f"\n>>> User Query: {query}")

    # Prepare the user's message in ADK format
    content = types.Content(role='user', parts=[types.Part(text=query)])

    final_response_text = "Agent did not produce a final response." # Default

    # Key Concept: run_async executes the agent logic and yields Events.
    # We iterate through events to find the final answer.
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        # You can uncomment the line below to see *all* events during execution
        # print(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")

        # Key Concept: is_final_response() marks the concluding message for the turn.
        if event.is_final_response():
            if event.content and event.content.parts:
                # Assuming text response in the first part
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate: # Handle potential errors/escalations
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            # Add more checks here if needed (e.g., specific error codes)
            break # Stop processing events once the final response is found

    print(f"<<< Agent Response: {final_response_text}")
    return final_response_text


async def chat(query: str, model: str = "gemini-2.5-flash"):
    """Convenience function to chat with the weather agent using default session.

    Args:
        query: The user's question or request.
        model: Model to use - "gemini-2.5-flash" (default) or "claude-sonnet".

    Returns:
        The agent's response text.

    Example:
        >>> import asyncio
        >>> import agent_team
        >>> asyncio.run(agent_team.chat("What's the weather in London?"))
    """
    if model == "gemini-2.5-flash":
        from .session import get_runner, get_user_id, get_session_id, get_session
        # Ensure session is initialized
        await get_session()
        return await call_agent_async(
            query=query,
            runner=get_runner(),
            user_id=get_user_id(),
            session_id=get_session_id()
        )
    elif model == "claude-sonnet":
        from .session_claude import get_runner, get_user_id, get_session_id, get_session
        # Ensure session is initialized
        await get_session()
        return await call_agent_async(
            query=query,
            runner=get_runner(),
            user_id=get_user_id(),
            session_id=get_session_id()
        )
    else:
        raise ValueError(f"Unknown model: {model}. Use 'gemini-2.5-flash' or 'claude-sonnet'.")
    
    
async def run_team_conversation(model: str = "gemini-2.5-flash"):    
    print("\n--- Testing Agent Team Delegation ---")

    session_agent_team = None
    runner_agent_team = None
    user_id_agent_team = None
    session_id_agent_team = None

    if model == "gemini-2.5-flash":        
        from .session import get_runner, get_user_id, get_session_id, get_session        
        session_agent_team = await get_session()
        runner_agent_team = get_runner()
        user_id_agent_team = get_user_id()
        session_id_agent_team = get_session_id()

    elif model == "claude-sonnet":
        from .session_claude import get_runner, get_user_id, get_session_id, get_session
        session_agent_team = await get_session()
        runner_agent_team = get_runner()
        user_id_agent_team = get_user_id()
        session_id_agent_team = get_session_id()

    if session_agent_team is None:
        print("❌ Session for Claude agent is not available. Cannot proceed with conversation.")
        return

    if runner_agent_team is None:
        print("❌ Runner for Claude agent is not available. Cannot proceed with conversation.")
        return        

    print(f"Session created: App='{runner_agent_team.app_name}', User='{user_id_agent_team}', Session='{session_id_agent_team}'")          

    # --- Interactions using await (correct within async def) ---
    await call_agent_async(query = "Hello there!",
                            runner=runner_agent_team,
                            user_id=user_id_agent_team,
                            session_id=session_id_agent_team)
    await call_agent_async(query = "What is the weather in New York?",
                            runner=runner_agent_team,
                            user_id=user_id_agent_team,
                            session_id=session_id_agent_team)
    await call_agent_async(query = "Thanks, bye!",
                            runner=runner_agent_team,
                            user_id=user_id_agent_team,
                            session_id=session_id_agent_team)