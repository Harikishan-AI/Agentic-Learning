from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv
import os
load_dotenv()

api_key=os.getenv("OPENROUTER_API_KEY")

def make_translator_agent(lang_code, output_key):
    return LlmAgent(
        name=f'Transalor_Agent_{lang_code}',
        model=LiteLlm(model="openrouter/qwen/qwen3-vl-235b-a22b-thinking", api_key=api_key),
        instruction=f'Create a localized marketing tagline in {lang_code} for the user’s product/idea. Return only the tagline text.',
        output_key=output_key,
    )

# Market-focused (not translation): generate localized taglines per audience
spanish = make_translator_agent('Spanish', 'spanish_key')
french = make_translator_agent('French', 'French_key')
german = make_translator_agent('German', 'German_key')

parallel_translate = ParallelAgent(
    name='Parallel_Translator',
    description='Generate localized marketing taglines for Spanish, French, and German audiences.',
    sub_agents=[spanish, french, german],
)

merger_agent = LlmAgent(
    name='Merger_Agent',
    model=LiteLlm(model="openrouter/qwen/qwen3-vl-235b-a22b-thinking", api_key=api_key),
    instruction='''Package the taglines neatly:
     **Spanish** {spanish_key}
     **French** {French_key}
     **German** {German_key}

     Return the response in the following JSON format:
     ```
     {
       "es": "tagline_text",
       "fr": "tagline_text",
       "de": "tagline_text"
     }
     ```
    ''',
    output_key='merged_translation',
)

pipeline = SequentialAgent(
    name='Translation_Pipeline',
    sub_agents=[parallel_translate, merger_agent]
)

root_agent = pipeline