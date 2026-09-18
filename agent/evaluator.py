from services.llm_service import ask_ai


def evaluate_research(
    task,
    research
):

    task = str(task)[:3000]

    research = str(research)[:7000]


    prompt = f"""
Evaluate this research.

ORIGINAL TASK:

{task}

RESEARCH:

{research}

Check:

- Relevance
- Completeness
- Evidence quality
- Unsupported claims
- Missing information
- Source quality

Return:

QUALITY SCORE: X/10

Then provide a concise evaluation.
"""


    return ask_ai(
        prompt,
        system_prompt=(
            "You are a research quality evaluator."
        ),
        research_mode=False
    )