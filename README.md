# Microsoft Agent Framework Sandbox

Sandbox for testing building in [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/)

2 custom agents 1 build with ClaudeAgent (thin wrapper to Claude Code SDK) and the other via AnthropicClient.  There is a workflow that chains the 2 together.  ClaudeAgent runs fist and is a friendly greeter, AnthropicClient receives the output and adds a compliment and a question.

ClaudeAgent env variables to run via ollama.

```console
$env:CLAUDE_AGENT_MODEL="llama3.1:latest"
$env:ANTHROPIC_AUTH_TOKEN="ollama"
$env:ANTHROPIC_BASE_URL="http://localhost:11434"
$env:ANTHROPIC_API_KEY=""
```

Use pip to install requirements.

```console
pip install -r requirements.txt
```

Running the app.  Claude will run off CLAUDE_AGENT_MODEL while AnthropicClient will run off whatever model is passed in (could be the same).

```console
python .\main.py --name "Andy" --model "<ollama-model-running>"
```

Sample run and result:

```console
py .\main.py --name "David" --model "codellama:7b"
Checking environment variables...
http://localhost:11434
True
[claude-code:unrecognized_model] {"model":"llama3.1:latest","query_source":"generate_session_title"}

--- Customer Service Greeting ---


Hello David, it was great to hear that you're doing well. How was your day today?

---------------------------------