from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os 


# Path to the MCP server script
mcp_server_script = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "CH-1-CreateMCP", "1_first_mcp_server_stdio.py")

# Path to the virtual environment
venv_path = os.path.join(os.path.dirname(os.path.dirname((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))),".venv")


async def main():

    # Create an instance of the MultiServerMCPClient
    client = MultiServerMCPClient(

        # MCP Server Config (JSON)
        {
            "ddg-search":{
                "transport": "stdio",
                "command": "uvx",
                "args": ["duckduckgo-mcp-server"]
            }
        }
    )

    # List the tools
    tools = await client.get_tools()
    print("Available tools:", len(tools))

    # for tool in tools:
    #     print(f"tool {tool.name}\n")

    # Call a tool with the correct format
    ddg_tool = tools[0]
    result = await ddg_tool.ainvoke({"query": "What is MCP?"})
    print(result)

if __name__ == "__main__":
    asyncio.run(main())