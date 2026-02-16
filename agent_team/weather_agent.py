# @title Define the Root Agent with Sub-Agents

from .models import MODEL_GEMINI_2_5_FLASH
from .tools import get_weather
from .farewell_agent import farewell_agent
from .greeting_agent import greeting_agent
from google.adk.agents import Agent

# Ensure sub-agents were created successfully before defining the root agent.
# Also ensure the original 'get_weather' tool is defined.
root_weather_agent = None

if greeting_agent and farewell_agent and 'get_weather' in globals():
    try:
        # Let's use a capable Gemini model for the root agent to handle orchestration
        root_agent_model = MODEL_GEMINI_2_5_FLASH

        root_weather_agent = Agent(
            name="weather_agent_v2", # Give it a new version name
            model=root_agent_model,
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
        print(f"✅ Root Agent '{root_weather_agent.name}' created using model '{root_agent_model}' with sub-agents: {[sa.name for sa in root_weather_agent.sub_agents]}")
    except Exception as e:
        print(f"❌ Could not create Gemini agent '{MODEL_GEMINI_2_5_FLASH}'. Check API Key and model name. Error: {e}")
else:
    print("❌ Cannot create root agent because one or more sub-agents failed to initialize or 'get_weather' tool is missing.")
    if not greeting_agent: print(" - Greeting Agent is missing.")
    if not farewell_agent: print(" - Farewell Agent is missing.")
    if 'get_weather' not in globals(): print(" - get_weather function is missing.")



def get_agent() -> Agent | None:
    """Returns the configured weather agent."""
    return root_weather_agent