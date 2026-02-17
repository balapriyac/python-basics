from fastmcp import Client
import asyncio

async def test_server():
    async with Client("task_server.py") as client:
        # List available tools
        tools = await client.list_tools()
        print("Available tools:", [t.name for t in tools.tools])
        
        # Add a task
        result = await client.call_tool("add_task", {
            "title": "Learn MCP",
            "description": "Build a task tracker with FastMCP"
        })
        print("\nAdded task:", result.content[0].text)
        
        # View all tasks
        resources = await client.list_resources()
        print("\nAvailable resources:", [r.uri for r in resources.resources])
        
        task_list = await client.read_resource("tasks://all")
        print("\nAll tasks:\n", task_list.contents[0].text)

asyncio.run(test_server())
