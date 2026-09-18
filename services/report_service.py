from tools.document_generator import create_pdf


def generate_pdf_report(
    report_content: str,
    task_id: int
) -> str:

    filename = (
        f"research_report_{task_id}.pdf"
    )

    return create_pdf(
        report_content,
        filename
    )


def prepare_report_for_download(
    report_content: str
) -> bytes:

    return report_content.encode(
        "utf-8"
    )