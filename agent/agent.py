from agent.planner import create_plan
from agent.researcher import perform_research
from agent.evaluator import evaluate_research
from agent.executor import generate_report

from database.queries import (
    create_task,
    update_task
)


def run_agent(
    task,
    document_context="",
    progress_callback=None
):

    task_id = create_task(task)

    try:

        if progress_callback:
            progress_callback(
                "🧠 Creating research plan..."
            )

        plan = create_plan(task)

        update_task(
            task_id,
            plan=plan
        )

        if progress_callback:
            progress_callback(
                "🔎 Performing autonomous research..."
            )

        research = perform_research(
            task,
            plan,
            document_context
        )

        update_task(
            task_id,
            research=research
        )

        if progress_callback:
            progress_callback(
                "✅ Evaluating research quality..."
            )

        evaluation = evaluate_research(
            task,
            research
        )

        update_task(
            task_id,
            evaluation=evaluation
        )

        if progress_callback:
            progress_callback(
                "📝 Generating final report..."
            )

        report = generate_report(
            task,
            plan,
            research,
            evaluation
        )

        update_task(
            task_id,
            report=report,
            status="completed"
        )

        return {
            "task_id": task_id,
            "plan": plan,
            "research": research,
            "evaluation": evaluation,
            "report": report
        }

    except Exception as error:

        update_task(
            task_id,
            status="failed"
        )

        raise error