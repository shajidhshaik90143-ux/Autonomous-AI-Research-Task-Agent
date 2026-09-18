from sklearn.feature_extraction.text import TfidfVectorizer


def create_embeddings(documents):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000
    )

    matrix = vectorizer.fit_transform(
        documents
    )

    return vectorizer, matrix