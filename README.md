# Microsoft Agent Framework Sandbox

Sandbox for testing building in [Microsoft Agent Framework]https://learn.microsoft.com/en-us/agent-framework/

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