from google.adk.agents.llm_agent import Agent
from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm
import os
load_dotenv()

api_key=os.getenv("OPENROUTER_API_KEY")

root_agent = Agent(
    model=LiteLlm(model="openrouter/qwen/qwen3-vl-235b-a22b-thinking", api_key=api_key),
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)

