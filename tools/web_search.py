from services.llm_service import ask_ai


def web_research(
    query: str,
    instructions: str = ""
) -> str:

    prompt = f"""
Perform web research for the following query:

{query}

Additional instructions:

{instructions}

Research requirements:

1. Find relevant and recent information.
2. Prefer reliable sources.
3. Compare information when sources differ.
4. Identify important facts.
5. Include source names or URLs when available.
6. Do not invent facts.
7. Clearly identify uncertainty.
8. Return a structured research summary.
"""

    return ask_ai(
        prompt,
        system_prompt=(
            "You are a web research assistant. "
            "Use available web-search capabilities to "
            "find and synthesize relevant information."
        ),
        research_mode=True
    )


def search_web(query: str) -> str:

    return web_research(query)


def research_multiple_topics(
    topics: list[str]
) -> dict:

    results = {}

    for topic in topics:

        try:

            results[topic] = web_research(
                topic
            )

        except Exception as error:

            results[topic] = (
                f"Research failed: {error}"
            )

    return results