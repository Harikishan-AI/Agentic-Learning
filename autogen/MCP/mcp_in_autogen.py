from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import McpWorkbench, StdioServerParams
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

async def main():
    # Configure the MCP server parameters
    # mcp-server-time is a standard MCP server for time-related tools
    params = StdioServerParams(
        command="uvx",
        args=["mcp-server-time", "--local-timezone=America/New_York"],
    )

    # Configure the model client
    model = OpenAIChatCompletionClient(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPEN_ROUTER_API_KEY"),
        model="arcee-ai/trinity-large-preview:free",
        model_info={
            "family": "arcee",
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "structured_output": True,
            "multiple_system_messages": True
        },
    )

    # Use McpWorkbench to manage the MCP server lifecycle and tools
    async with McpWorkbench(server_params=params) as workbench:
        # tools = await workbench.list_tools()
        # print(tools)
        agent = AssistantAgent(
            name="TimeAgent",
            model_client=model,
            workbench=workbench,
            system_message="You are a helpful assistant that can provide time-related information using the available tools. Use the tools to get current time or timezone information.",
            reflect_on_tool_use=True,
        )

        # Run the agent on a specific task
        result = await agent.run(task="What is the time right now in london")
        
        # Output the final response
        print(f"\nResponse: {result.messages[-1].content}")

if __name__ == "__main__":
    asyncio.run(main())