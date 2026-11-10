
from agent_framework import WorkflowBuilder

from agents.claude import claude_greeter
from agents.anthropic import anthropic_greeter


async def run_greeting_workflow(name: str, model: str):

    # Initialize agents
    claude_agent = claude_greeter()
    anthropic_agent = anthropic_greeter(model=model)

    # Build sequential workflow
    workflow = (
        WorkflowBuilder(start_executor=claude_agent)
        .add_edge(claude_agent, anthropic_agent)
        .build()
    )

    # Execute workflow
    async with claude_agent, anthropic_agent:
        result = await workflow.run(
            f"Greet the customer named {name}."
        )

    # Return final agent response
    outputs = result.get_outputs()

    return outputs[-1].text if outputs else ""
