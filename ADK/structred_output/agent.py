from google.adk.agents.llm_agent import LlmAgent
from pydantic import BaseModel, Field

class CapitalOutput(BaseModel):
    capital: str = Field(description="The capital of the country.")

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction=f"Answer user questions to the best of your knowledge. Format :{"capital"':'"capital_name"}" ,
    output_schema=CapitalOutput,
    output_key="found_capital"
)
