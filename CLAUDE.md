# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a learning project for Google's Agent Development Kit (ADK) - a framework for building AI agents with tool-calling capabilities.

## Environment Setup

```bash
conda env create -f environment.yml
conda activate adk-learning
```

## Running Agents

ADK agents are run using the `adk` CLI. From the project root:

```bash
# Run an agent interactively in the terminal
adk run <agent_folder>

# Run with web UI
adk web <agent_folder>

# Examples:
adk run my_agent
adk run multi_tool_agent
adk run agent_team
```

## Architecture

### Agent Structure

Each agent lives in its own folder with a standard structure:
- `__init__.py` - Imports the agent module (must expose `root_agent` or the main agent)
- `agent.py` - Defines the `root_agent` with model, instructions, and tools

### Key ADK Concepts

**Agent Definition** (`google.adk.agents.Agent`):
- `name`: Identifier for the agent
- `model`: LLM to use (e.g., `gemini-2.0-flash`, `gemini-2.5-flash`, or LiteLLM models like `anthropic/claude-sonnet-4-20250514`)
- `description`: What the agent does
- `instruction`: System prompt guiding agent behavior
- `tools`: List of Python functions the agent can call

**Tools**: Plain Python functions with type hints and docstrings. ADK uses the docstring to explain the tool to the LLM.

**Multi-model Support**: Use `google.adk.models.lite_llm.LiteLlm` for non-Google models (requires `litellm` package).

**Session Management**: `InMemorySessionService` for development, `Runner` orchestrates agent execution.

### Example Agents

- `my_agent/` - Minimal agent with single tool (time lookup)
- `multi_tool_agent/` - Agent with weather and time tools
- `agent_team/` - More complex setup with separate files for tools, agent definition, session management, and interaction helpers
