from smolagents import InferenceClientModel, CodeAgent, ToolCollection
from mcp.client.stdio import StdioServerParameters
from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())
hf_token = os.getenv('hf_token')

model = InferenceClientModel(token=hf_token)
                             
server_parameters = StdioServerParameters(command="uv", args=["run", "server.py"])

with ToolCollection.from_mcp(
    server_parameters, trust_remote_code=True
) as tool_collection:
    agent = CodeAgent(tools=[*tool_collection.tools], model=model)
    agent.run("What's the weather in Tokyo?")
