
### Create Environment for depenedencies

```bash
mkdir mcp-sentiment
cd mcp-sentiment

conda create -n mcp-sentiment python=3.11
conda activate mcp-sentiment

pip install "gradio[mcp]" textblob
```

### Create a Basic MCP-Server and MCP Inspector:

[server](server.py)

* This code sets up a simple MCP server with a defined weather service tool, resource, and prompt. The `get_weather` function retrieves the current weather for a specified location, while the `weather_resource` function provides weather data as a resource. The `weather_report` prompt creates a weather report prompt for a given location. The server can be run to handle requests for weather information. The MCP server can be accessed via the defined tool, resource, and prompt.

```bash
mcp dev server.py
```
```http://localhost:6274``` -> open the MCP Inspector to see the server’s capabilities and interact with them.

### Now, let’s see how we can use the MCP Client in a code agent (Smolagents).

[client](client.py)

```bash
python3 client.py
```
- Note: Got the weather for Tokyo

### Create the MCP Server with Gradio

[app](app.py) --> this is a sentiment_analysis function tool, which automatically becomes a ```MCP Tool```. 

```bash
python3 app.py
```
***Note***: You should see output indicating that both the web interface and MCP server are running. The web interface will be available at ```http://localhost:7860```, the MCP server at ```http://localhost:7860/gradio_api/mcp/sse``` and MCP Schemaa at ```http://localhost:7860/gradio_api/mcp/schema```

### Basic Configuration of a UI MCP Client

***Note***: When working with Gradio MCP servers, you can configure your UI client to connect to the server using the MCP protocol. This configuration allows your UI client to communicate with the Gradio MCP server using the MCP protocol, enabling seamless integration between your frontend and the MCP service.

* Create a new file called ```config.json```  --> check codes in it.

[mcp_client](mcp_client.py)  --> running this script connects the Gradio UI client to a server via the configuration file.


## PROJECT

* Build an intelligent PR Agent that analyzes code changes and suggests helpful descriptions automatically.

* What You’ll Build: PR Agent Workflow Server - An MCP server that demonstrates how to make Claude Code team-aware and workflow-intelligent:

***Smart PR Management***: Automatic PR template selection based on code changes using MCP Tools
***CI/CD Monitoring***: Track GitHub Actions with Cloudflare Tunnel and standardized Prompts
***Team Communication***: Slack notifications demonstrating all MCP primitives working together

### Install Claude Code to test your MCP server integration. (WSL)

```bash
npm install -g @anthropic-ai/claude-code

cd your-project-directory

claude
```

```bash
mkdir PR_Agent

pip install uv

git clone https://github.com/huggingface/mcp-course.git

cd mcp-course/projects/unit3/build-mcp-server/starter

# Validate Your Code: run the validation script to check your implementation
uv run python validate_starter.py          

# Run Unit Tests: test your implementation with the provided test suite
uv run pytest test_server.py -v

# Test with Claude Code: add the MCP server to Claude Code
claude mcp add pr-agent -- uv --directory /absolute/path/to/starter run server.py

# Verify the server is configured
claude mcp list