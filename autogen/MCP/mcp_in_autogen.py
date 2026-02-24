from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import McpWorkbench, StdioServerParams
import asyncio
import os
import time
from dotenv import load_dotenv
load_dotenv()

async def main():
    params = StdioServerParams(
        command="uvx",
        args=["mcp-server-time", "--local-timezone=America/New_York"],
    )
    model = OpenAIChatCompletionClient(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
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
    
    async with McpWorkbench(server_params=params) as workbench:
        agent = AssistantAgent(
            name="Agent",
            model_client=model,
            workbench=workbench,
        )
        result = await agent.run(task="What is the the time in New delhi?")
        print(result.messages[-1].content)

if __name__ == "__main__":
    asyncio.run(main())