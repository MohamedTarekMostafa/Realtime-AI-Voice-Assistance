import os
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession
from livekit.plugins import google
load_dotenv(".env")
class EgyptAirRealtimeAssistant(Agent):
    def __init__(self):
        super().__init__(
            instructions="""You are a professional EGYPTAIR voice concierge.
            - Speak directly to the user with a welcoming tone.
            - You can hear the user's voice and emotions directly.
            - Keep your responses natural and concise."""
        )

async def entrypoint(ctx: agents.JobContext):
    llm = google.realtime.RealtimeModel(
        model="gemini-2.5-flash-native-audio-preview-12-2025", 
        voice="Puck", 
        instructions="You are an EGYPTAIR assistant. Talk to the user naturally."
    )

    assistant = EgyptAirRealtimeAssistant()
    session = AgentSession(
        llm=llm,
    )

    await session.start(room=ctx.room, agent=assistant)

    await session.generate_reply(
        instructions="Greet the user warmly in English and ask how you can assist with their EGYPTAIR travel today."
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))