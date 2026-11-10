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
                You are a professional customer service representative.
        
                Your ONLY responsibility is greeting customers.
        
                - Greet the customer by their name.
                - Be warm, friendly, and professional.
                - Keep your response concise.
                - Do not perform any other tasks.
                """
    )
    return agent