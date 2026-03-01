# parallel_demo.py  – run with:  python parallel_demo.py "Translate: Hello, world!"
from google.adk.agents import LlmAgent, SequentialAgent

GEMINI = "gemini-3-flash-preview"

def make_translator_agent(lang_code, output_key):
    return LlmAgent(
        name=f"Translator_{lang_code}",
        model=GEMINI,
        instruction=f"Translate the user prompt into {lang_code}. "
                    "Return ONLY the translation text.",
        output_key=output_key,
    )

# 1️⃣ Three independent translators
spanish = make_translator_agent("Spanish", "es")
french  = make_translator_agent("French",  "fr")
german  = make_translator_agent("German",  "de")

sequential_translate = SequentialAgent(
    name="Sequential_Translate",
    sub_agents=[spanish, french, german],
    description="Runs three translation agents in Sequence."
)

root_agent = sequential_translate
 