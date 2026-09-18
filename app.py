import streamlit as st

from database.connection import init_database
from database.queries import get_dashboard_stats


st.set_page_config(
    page_title="Autonomous AI Research Agent",
    page_icon="🤖",
    layout="wide"
)

init_database()


def main():

    st.title("🤖 Autonomous AI Research & Task Agent")

    st.markdown(
        """
        ### Your AI-powered autonomous research assistant

        Give the agent a research objective and it can:

        - 🧠 Analyze your task
        - 📋 Create a research plan
        - 🔎 Perform web research
        - 📚 Search uploaded documents
        - 🤖 Analyze findings
        - ✅ Evaluate the research
        - 📝 Generate a final report
        - 💾 Save research history
        """
    )

    st.divider()

    stats = get_dashboard_stats()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Research Tasks",
        stats["tasks"]
    )

    col2.metric(
        "Completed",
        stats["completed"]
    )

    col3.metric(
        "Documents",
        stats["documents"]
    )

    col4.metric(
        "Reports",
        stats["reports"]
    )

    st.divider()

    st.subheader("🚀 Start New Research")

    task = st.text_area(
        "Research objective",
        placeholder=(
            "Example: Research the impact of artificial intelligence "
            "on software engineering and prepare a detailed report."
        ),
        height=150
    )

    if st.button(
        "🚀 Start Autonomous Research",
        type="primary",
        use_container_width=True
    ):

        if not task.strip():
            st.warning("Please enter a research objective.")
            return

        st.session_state["research_task"] = task

        st.switch_page("pages/research.py")

    st.info(
        "Use the sidebar to upload PDFs, view research history, "
        "and manage application settings."
    )


if __name__ == "__main__":
    main()