import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from rag.embeddings import create_embeddings


class SimpleVectorStore:

    def __init__(self):

        self.documents = []

        self.vectorizer = None

        self.matrix = None

    def add_documents(self, documents):

        self.documents.extend(documents)

        if self.documents:

            (
                self.vectorizer,
                self.matrix
            ) = create_embeddings(
                self.documents
            )

    def search(
        self,
        query,
        top_k=3
    ):

        if not self.documents:
            return []

        query_vector = (
            self.vectorizer.transform(
                [query]
            )
        )

        scores = cosine_similarity(
            query_vector,
            self.matrix
        )[0]

        indexes = np.argsort(scores)[::-1]

        results = []

        for index in indexes[:top_k]:

            results.append(
                {
                    "text": self.documents[index],
                    "score": float(
                        scores[index]
                    )
                }
            )

        return results