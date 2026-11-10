from agent_framework import Agent
from agent_framework.anthropic import AnthropicClient

def anthropic_greeter(model: str) -> Agent:
    client = AnthropicClient(
        model=model,
        api_key="ollama",
        base_url="http://localhost:11434"
    )

    agent = Agent(
        client=client,
        instructions="""
            You are a customer service quality reviewer.

            You will receive a draft customer greeting.

            Your responsibility is to:
            - Preserve the customer's name.
            - Add a warm comliment to the greeting followed by a question about the customer's day.

            Do not generate an entirely new greeting.
                """
    )
    return agent