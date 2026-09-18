from services.llm_service import ask_ai


def create_plan(task):

    task = str(task)[:3000]

    prompt = f"""
Create a concise research plan for:

{task}

Return:

1. Research objective
2. Key questions
3. Topics to investigate
4. Required evidence
5. Suggested report structure

Keep the plan concise.
"""

    return ask_ai(
        prompt,
        system_prompt=(
            "You are an expert research planner."
        ),
        research_mode=False
    )