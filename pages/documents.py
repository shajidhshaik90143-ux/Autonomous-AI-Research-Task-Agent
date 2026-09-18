import streamlit as st

from database.queries import (
    save_document,
    get_documents
)

from tools.file_reader import (
    read_uploaded_pdf
)


st.set_page_config(
    page_title="Documents",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Research Documents")

st.write(
    "Upload PDF documents that the research agent can use "
    "as additional knowledge."
)


uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)


if uploaded_files:

    for uploaded_file in uploaded_files:

        if st.button(
            f"📥 Process {uploaded_file.name}",
            key=uploaded_file.name
        ):

            try:

                with st.spinner(
                    f"Reading {uploaded_file.name}..."
                ):

                    text = read_uploaded_pdf(
                        uploaded_file
                    )

                if not text.strip():

                    st.warning(
                        "No readable text was found."
                    )

                else:

                    save_document(
                        uploaded_file.name,
                        text
                    )

                    st.success(
                        f"{uploaded_file.name} saved successfully."
                    )

            except Exception as error:

                st.error(
                    f"Error: {error}"
                )


st.divider()

st.subheader("📖 Stored Documents")

documents = get_documents()

if not documents:

    st.info(
        "No documents uploaded yet."
    )

else:

    for document in documents:

        with st.expander(
            f"📄 {document['filename']}"
        ):

            content = document["content"]

            st.write(
                content[:5000]
            )

            st.caption(
                f"Characters: {len(content)}"
            )