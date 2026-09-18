from services.llm_service import ask_ai


def perform_research(
    task,
    plan,
    document_context=""
):

    # Keep input small to prevent 413 errors
    task = str(task)[:2000]

    plan = str(plan)[:2500]

    document_context = str(
        document_context or ""
    )[:2500]

    if not document_context:
        document_context = (
            "No uploaded documents were provided."
        )

    prompt = f"""
You are an autonomous AI research agent.

Research objective:
{task}

Research plan:
{plan}

Document context:
{document_context}

Perform focused web research.

Requirements:

1. Find relevant information.
2. Prefer reliable sources.
3. Focus on important facts.
4. Identify useful sources.
5. Do not invent facts.
6. Clearly identify uncertainty.
7. Keep the response concise.

Return:

## Research Summary

## Key Findings

## Evidence

## Important Sources

## Limitations
"""

    return ask_ai(
        prompt,
        system_prompt=(
            "You are a professional autonomous "
            "research agent. Perform focused "
            "research and provide concise findings."
        ),
        research_mode=True
    )