from agent.planner import create_plan
from agent.researcher import perform_research
from agent.evaluator import evaluate_research
from agent.executor import generate_report

from rag.retriever import retrieve_documents


def create_research_plan(task: str) -> str:

    return create_plan(task)


def research_task(
    task: str,
    plan: str,
    use_documents: bool = True
) -> str:

    document_context = ""

    if use_documents:

        document_context = retrieve_documents(
            task,
            top_k=3
        )

    return perform_research(
        task,
        plan,
        document_context
    )


def evaluate_research_results(
    task: str,
    research: str
) -> str:

    return evaluate_research(
        task,
        research
    )


def create_final_report(
    task: str,
    plan: str,
    research: str,
    evaluation: str
) -> str:

    return generate_report(
        task,
        plan,
        research,
        evaluation
    )


def run_research_pipeline(
    task: str,
    use_documents: bool = True,
    progress_callback=None
):

    if progress_callback:
        progress_callback(
            "🧠 Creating research plan..."
        )

    plan = create_research_plan(
        task
    )

    if progress_callback:
        progress_callback(
            "🔎 Performing research..."
        )

    research = research_task(
        task,
        plan,
        use_documents
    )

    if progress_callback:
        progress_callback(
            "✅ Evaluating research..."
        )

    evaluation = evaluate_research_results(
        task,
        research
    )

    if progress_callback:
        progress_callback(
            "📝 Generating final report..."
        )

    report = create_final_report(
        task,
        plan,
        research,
        evaluation
    )

    if progress_callback:
        progress_callback(
            "🎉 Research completed!"
        )

    return {
        "plan": plan,
        "research": research,
        "evaluation": evaluation,
        "report": report
    }