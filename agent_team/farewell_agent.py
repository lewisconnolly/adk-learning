# @title Define Farewell Sub-Agent

from . import tools
from .models import MODEL_GEMINI_2_5_FLASH
from google.adk.agents import Agent

AGENT_MODEL = MODEL_GEMINI_2_5_FLASH

farewell_agent = None
try:
    farewell_agent = Agent(
        model = MODEL_GEMINI_2_5_FLASH,
        name="farewell_agent",
        instruction="You are the Farewell Agent. Your ONLY task is to provide a polite goodbye message. "
                    "Use the 'say_goodbye' tool when the user indicates they are leaving or ending the conversation "
                    "(e.g., using words like 'bye', 'goodbye', 'thanks bye', 'see you'). "
                    "Do not perform any other actions.",
        description="Handles simple farewells and goodbyes using the 'say_goodbye' tool.", # Crucial for delegation
        tools=[tools.say_goodbye],
    )
    print(f"✅ Agent '{farewell_agent.name}' created using model '{farewell_agent.model}'.")
except Exception as e:
    print(f"❌ Could not create Farewell agent. Check API Key ({AGENT_MODEL}). Error: {e}")