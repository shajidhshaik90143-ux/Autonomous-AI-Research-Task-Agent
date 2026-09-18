import streamlit as st

from database.connection import init_database
from database.queries import get_dashboard_stats, get_tasks


st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

init_database()


def main():

    st.title("📊 AI Research Dashboard")

    st.markdown(
        """
        Monitor your autonomous AI research activity,
        documents, reports, and completed tasks.
        """
    )

    st.divider()

    stats = get_dashboard_stats()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🔬 Research Tasks",
            stats["tasks"]
        )

    with col2:
        st.metric(
            "✅ Completed",
            stats["completed"]
        )

    with col3:
        st.metric(
            "📚 Documents",
            stats["documents"]
        )

    with col4:
        st.metric(
            "📄 Reports",
            stats["reports"]
        )

    st.divider()

    st.subheader("🕘 Recent Research")

    tasks = get_tasks()

    if not tasks:

        st.info(
            "No research tasks have been created yet."
        )

        return

    for task in tasks[:10]:

        with st.expander(
            f"#{task['id']} — {task['task'][:100]}"
        ):

            col1, col2 = st.columns(2)

            with col1:
                st.write(
                    f"**Status:** {task['status']}"
                )

            with col2:
                st.write(
                    f"**Created:** {task['created_at']}"
                )

            if task["report"]:

                st.markdown(
                    task["report"][:3000]
                )


if __name__ == "__main__":
    main()