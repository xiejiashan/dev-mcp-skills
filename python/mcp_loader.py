import yaml
from pathlib import Path


def load_skill(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def skill_to_system_prompt(skill: dict) -> str:
    rules = "\n".join(f"- {r}" for r in skill.get("rules", []))
    return f"""
You are an AI agent using the skill: {skill['metadata']['name']}

Description:
{skill['metadata']['description']}

Rules:
{rules}

Output format:
{skill['outputs']}
""".strip()
