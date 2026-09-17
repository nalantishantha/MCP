from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def fetch():
    '''Use this tool to fetch data from the source.'''
    #Simulate fetching data from a source
    
    return {"data": "Sample data fetched from the source."}

@mcp.tool()
def process(data):
    '''Use this tool to process the fetched data.'''
    #Simulate processing the data
    
    processed_data = data.upper()  # Example processing: converting to uppercase
    return {"processed_data": processed_data}

if __name__ == "__main__":
    mcp.run(transport="stdio") 