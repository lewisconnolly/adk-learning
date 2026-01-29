# @title Define Greeting Sub-Agent

from . import tools
from .models import MODEL_GEMINI_2_5_FLASH
from google.adk.agents import Agent

AGENT_MODEL = MODEL_GEMINI_2_5_FLASH

greeting_agent = None
try:
    greeting_agent = Agent(
        model = AGENT_MODEL,
        name="greeting_agent",
        instruction="You are the Greeting Agent. Your ONLY task is to provide a friendly greeting to the user. "
                    "Use the 'say_hello' tool to generate the greeting. "
                    "If the user provides their name, make sure to pass it to the tool. "
                    "Do not engage in any other conversation or tasks.",
        description="Handles simple greetings and hellos using the 'say_hello' tool.", # Crucial for delegation
        tools=[tools.say_hello],
    )
    print(f"✅ Agent '{greeting_agent.name}' created using model '{greeting_agent.model}'.")
except Exception as e:
    print(f"❌ Could not create Greeting agent. Check API Key ({AGENT_MODEL}). Error: {e}")