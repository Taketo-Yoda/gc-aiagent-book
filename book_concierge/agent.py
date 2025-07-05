from google.adk.agents import Agent
import book_concierge.prompt as prompt

root_agent = Agent(
    name="book_concierge_agent",
    description="書籍提案エージェント",
    model="gemini-2.0-flash",
    instruction=prompt.ROOT_AGENT_INSTR,
)