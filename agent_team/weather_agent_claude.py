# @title Define the Claude Root Agent with Sub-Agents

from .models import MODEL_CLAUDE_SONNET
from .tools import get_weather
from .farewell_agent import farewell_agent
from .greeting_agent import greeting_agent
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_weather_agent_claude = None

if greeting_agent and farewell_agent and 'get_weather' in globals():
    try:
        AGENT_MODEL = MODEL_CLAUDE_SONNET
        
        root_weather_agent_claude = Agent(
            name="weather_agent_claude_v2",
            # Key change: Wrap the LiteLLM model identifier
            model=LiteLlm(model=MODEL_CLAUDE_SONNET),
            description="The main coordinator agent. Handles weather requests and delegates greetings/farewells to specialists.",
            instruction="You are the main Weather Agent coordinating a team. Your primary responsibility is to provide weather information. "
                        "Use the 'get_weather' tool ONLY for specific weather requests (e.g., 'weather in London'). "
                        "You have specialized sub-agents: "
                        "1. 'greeting_agent': Handles simple greetings like 'Hi', 'Hello'. Delegate to it for these. "
                        "2. 'farewell_agent': Handles simple farewells like 'Bye', 'See you'. Delegate to it for these. "
                        "Analyze the user's query. If it's a greeting, delegate to 'greeting_agent'. If it's a farewell, delegate to 'farewell_agent'. "
                        "If it's a weather request, handle it yourself using 'get_weather'. "
                        "For anything else, respond appropriately or state you cannot handle it.",
            tools=[get_weather], # Root agent still needs the weather tool for its core task
            # Key change: Link the sub-agents here!
            sub_agents=[greeting_agent, farewell_agent]
        )
        print(f"Agent '{root_weather_agent_claude.name}' created using model '{MODEL_CLAUDE_SONNET}'.")

    except Exception as e:
        print(f"❌ Could not create Claude agent '{MODEL_CLAUDE_SONNET}'. Check API Key and model name. Error: {e}")

def get_agent() -> Agent | None:
    """Returns the configured weather agent."""
    return root_weather_agent_claude