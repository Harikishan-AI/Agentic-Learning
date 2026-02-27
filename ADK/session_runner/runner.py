from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent import root_agent

import dotenv
import asyncio

dotenv.load_dotenv()

sessions_service_in_memory = InMemorySessionService()

initial_state = {
    "name": "Mayank",
    "data": """
    I am Mayank, a software developer with 5 years of experience 
    in full-stack development.
    I love NBA, and my favourite player is Kobe Bryant.
    """
}

APP_NAME = "Answer Agent"
USER_ID = "mayank"
SESSION_ID = "mayank_session"


async def main():

    # Create session
    await sessions_service_in_memory.create_session(
        session_id=SESSION_ID,
        user_id=USER_ID,
        app_name=APP_NAME,
        state=initial_state
    )

    print(f"Session created with ID: {SESSION_ID}")

    runner = Runner(
        agent=root_agent,
        session_service=sessions_service_in_memory,
        app_name=APP_NAME
    )

    # Get session
    session = await sessions_service_in_memory.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    context_text = f"""
    User Info:
    Name: {session.state.get("name")}
    Data: {session.state.get("data")}

    Question: Which is the Favourite Player of User?
    """

    new_message = types.Content(
        role="user",
        parts=[types.Part(text=context_text)]
    )

    # Run agent normally 
    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        if event.is_final_response():
            print("Final response:", event.content.parts[0].text)

asyncio.run(main())