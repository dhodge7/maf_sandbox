
from agent_framework_claude import ClaudeAgent
from claude_agent_sdk import ClaudeAgentOptions


def claude_greeter() -> ClaudeAgent:
    return ClaudeAgent(
        name="customer_service_greeter",
        instructions="""
        You are a professional customer service representative.

        Your ONLY responsibility is greeting customers.

        - Greet the customer by their name.
        - Be warm, friendly, and professional.
        - Keep your response concise.
        - Do not perform any other tasks.
        - Do not ask for any additional information.
        """
    )