from google.adk.agents import Agent
from book_concierge.prompt import PURCHASE_AGENT_INSTR
from book_concierge.service import BookConciergeService

service = BookConciergeService()

root_agent = Agent(
    name="book_concierge_agent",
    description="書籍提案エージェント",
    model="gemini-2.0-flash",
    instruction=service.build_root_prompt(),
    sub_agents=[
        Agent(
            name="re_read_agent",
            description="過去の書籍から再読を希望する場合のエージェント",
            model="gemini-2.0-flash",
            instruction=service.build_re_read_prompt(),
        ),
        Agent(
            name="purchase_agent",
            description="書籍の購入をサポートするエージェント",
            model="gemini-2.0-flash",
            instruction=PURCHASE_AGENT_INSTR,
        ),
    ]
)