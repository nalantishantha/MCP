{
  "mcpServers": {
    "tavily-remote-mcp": {
      "type": "http",
      "url": "https://mcp.tavily.com/mcp/"
    }
  }
}

from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os 
from dotenv import load_dotenv

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")


# Path to the MCP server script
mcp_server_script = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "CH-1-CreateMCP", "1_first_mcp_server_stdio.py")

# Path to the virtual environment
venv_path = os.path.join(os.path.dirname(os.path.dirname((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))),".venv")


async def main():

    # Create an instance of the MultiServerMCPClient
    client = MultiServerMCPClient(

        # MCP Server Config (JSON)
        {

            "tavily_mcp_http":{
                "transport": "streamable-http",
                "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={tavily_api_key}",
            }
        }
    )

    # List the tools
    tools = await client.get_tools()
    print("Available tools:", len(tools))

    #call the tool
    tavily_tool = [tool for tool in tools if tool.name == "tavily_search"] [0]
    result = await tavily_tool.ainvoke({"query": "What is MCP?"})
    print(result)
    

if __name__ == "__main__":
    asyncio.run(main())