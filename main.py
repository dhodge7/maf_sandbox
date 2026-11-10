import argparse
import asyncio
import os

from dotenv import load_dotenv
from workflow import run_greeting_workflow


async def main():
    load_dotenv()
    print("Checking environment variables...")
    print(os.getenv("ANTHROPIC_BASE_URL"))
    print(bool(os.getenv("ANTHROPIC_AUTH_TOKEN")))

    parser = argparse.ArgumentParser(
        description="Customer Service Greeting Agent"
    )

    parser.add_argument(
        "--name",
        required=True,
        help="Name of the customer to greet"
    )

    parser.add_argument(
        "--model",
        default="llama3.1:latest",
        help="Claude model to use (default: llama3.1:latest)"
    )

    args = parser.parse_args()

    if args.name is None:
        print("Error: --name argument is required.")
        return

    # Execute workflow
    response = await run_greeting_workflow(
        name=args.name,
        model=args.model
    )

    print("\n--- Customer Service Greeting ---\n")
    print(response)
    print("\n---------------------------------\n")


if __name__ == "__main__":
    asyncio.run(main())
