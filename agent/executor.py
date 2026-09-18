from services.llm_service import ask_ai


def generate_report(
    task,
    plan,
    research,
    evaluation
):

    task = str(task)[:3000]

    plan = str(plan)[:4000]

    research = str(research)[:7000]

    evaluation = str(evaluation)[:4000]


    prompt = f"""
Create a professional research report.

TASK:

{task}

PLAN:

{plan}

RESEARCH:

{research}

EVALUATION:

{evaluation}

Use this structure:

# Research Report

## Executive Summary

## Introduction

## Research Objectives

## Methodology

## Key Findings

## Detailed Analysis

## Evidence

## Limitations

## Future Trends

## Conclusion

## Sources

Rules:

- Use only the provided research.
- Do not invent statistics.
- Do not invent sources.
- Clearly identify uncertainty.
- Keep the report concise and professional.
"""


    return ask_ai(
        prompt,
        system_prompt=(
            "You are a professional research "
            "report generator."
        ),
        research_mode=False
    )