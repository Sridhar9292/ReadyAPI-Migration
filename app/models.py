from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from app.config import OPENAI_API_KEY, ANTHROPIC_API_KEY


def get_gpt_model():
    return ChatOpenAI(
        model="gpt-4o-mini",
        api_key=OPENAI_API_KEY,
        temperature=0.3
    )


def get_claude_model():
    return ChatAnthropic(
        model="claude-3-haiku-20240307",
        api_key=ANTHROPIC_API_KEY,
        temperature=0.3
    )
