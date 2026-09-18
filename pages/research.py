import streamlit as st

from agent.agent import run_agent
from rag.retriever import retrieve_documents
from tools.document_generator import create_pdf


st.set_page_config(
    page_title="Research",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 Autonomous Research")


default_task = st.session_state.get(
    "research_task",
    ""
)


task = st.text_area(
    "Research Objective",
    value=default_task,
    height=150,
    placeholder=(
        "Example: Research the future of "
        "artificial intelligence in education."
    )
)


use_documents = st.checkbox(
    "Use uploaded documents as additional research context",
    value=True
)


if st.button(
    "🚀 Run Autonomous Agent",
    type="primary",
    use_container_width=True
):

    if not task.strip():

        st.warning(
            "Enter a research objective."
        )

        st.stop()

    document_context = ""

    if use_documents:

        with st.spinner(
            "Searching uploaded documents..."
        ):

            document_context = retrieve_documents(
                task
            )

    progress_area = st.empty()

    status_messages = []

    def update_progress(message):

        status_messages.append(
            message
        )

        progress_area.info(
            "\n\n".join(
                status_messages
            )
        )

    try:

        with st.spinner(
            "Autonomous agent is working..."
        ):

            result = run_agent(
                task,
                document_context,
                update_progress
            )

        progress_area.success(
            "✅ Research completed!"
        )

        st.divider()

        st.subheader("🧠 Research Plan")

        st.markdown(
            result["plan"]
        )

        st.divider()

        st.subheader("🔎 Research Findings")

        st.markdown(
            result["research"]
        )

        st.divider()

        st.subheader("✅ Evaluation")

        st.markdown(
            result["evaluation"]
        )

        st.divider()

        st.subheader("📄 Final Report")

        st.markdown(
            result["report"]
        )

        pdf_path = create_pdf(
            result["report"],
            f"research_report_{result['task_id']}.pdf"
        )

        with open(
            pdf_path,
            "rb"
        ) as file:

            st.download_button(
                "📥 Download PDF Report",
                data=file,
                file_name=(
                    f"research_report_"
                    f"{result['task_id']}.pdf"
                ),
                mime="application/pdf",
                use_container_width=True
            )

    except Exception as error:

        st.error(
            f"❌ Agent error: {error}"
        )

        st.info(
            "Check your GROQ_API_KEY in the .env file "
            "and verify your internet connection."
        )