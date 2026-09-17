import os
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters, client
import asyncio

#path to the MCP server script
mcp_server_script = os.path.join(os.path.dirname(__file__), '1_first_mcp_server_stdio.py')
print(mcp_server_script)

#create server parameters
server_params = StdioServerParameters(
    command="python",
    args=[str(mcp_server_script)],
    env={}
)

#create client session
async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            #initialize the MCP session
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:", tools)

            result = await session.call_tool("process", {"data": "Hello World"})
            print("Result:", result)

#run the client
if __name__ == "__main__":
    asyncio.run(main())