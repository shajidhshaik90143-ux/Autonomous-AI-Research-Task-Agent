from database.queries import (
    get_tasks,
    get_documents
)


def get_research_history():

    return get_tasks()


def get_uploaded_documents():

    return get_documents()