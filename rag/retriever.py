from database.queries import get_documents

from rag.vector_store import SimpleVectorStore


MAX_DOCUMENT_CHARS = 3500


def retrieve_documents(
    query,
    top_k=2
):

    documents = get_documents()

    if not documents:
        return ""


    texts = []

    for document in documents:

        content = document["content"]

        if content:

            # Limit every document before vectorization.
            content = content[:MAX_DOCUMENT_CHARS]

            texts.append(content)


    if not texts:
        return ""


    store = SimpleVectorStore()

    store.add_documents(texts)


    results = store.search(
        query,
        top_k=top_k
    )


    context = []


    for result in results:

        text = result["text"]

        text = text[:MAX_DOCUMENT_CHARS]

        if result["score"] > 0:

            context.append(text)


    # Final global limit
    final_context = "\n\n--- DOCUMENT ---\n\n".join(
        context
    )

    return final_context[:5000]