import requests
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[2] / "python"))

from mcp_loader import load_skill, skill_to_system_prompt


def fetch_url(url: str) -> str:
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.text[:8000]


skill = load_skill("../../mcp/skills/pr_review_assistant.yaml")
system_prompt = skill_to_system_prompt(skill)

llm = ChatOpenAI(model="gpt-4.1-mini")

pr_url = "https://github.com/langchain-ai/langchain/pull/123"  # example

content = fetch_url(pr_url)

messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content=f"PR URL: {pr_url}\n\nContent:\n{content}")
]

resp = llm(messages)
print(resp.content)
