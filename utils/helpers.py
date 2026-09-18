from datetime import datetime


def current_timestamp():

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def truncate_text(
    text,
    max_length=5000
):

    if not text:
        return ""

    if len(text) <= max_length:

        return text

    return (
        text[:max_length]
        + "\n\n[Content truncated]"
    )