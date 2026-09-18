import os

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT


def create_pdf(
    content,
    filename
):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    filepath = os.path.join(
        "reports",
        filename
    )

    document = SimpleDocTemplate(
        filepath,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    story = []

    for line in content.split("\n"):

        line = line.strip()

        if not line:
            story.append(
                Spacer(1, 8)
            )

            continue

        if line.startswith("# "):

            style = styles["Title"]

            text = line[2:]

        elif line.startswith("## "):

            style = styles["Heading1"]

            text = line[3:]

        elif line.startswith("### "):

            style = styles["Heading2"]

            text = line[4:]

        else:

            style = styles["BodyText"]

            text = line

        story.append(
            Paragraph(
                text,
                style
            )
        )

        story.append(
            Spacer(1, 6)
        )

    document.build(story)

    return filepath