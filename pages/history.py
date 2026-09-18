import streamlit as st

from database.queries import get_tasks


st.set_page_config(
    page_title="History",
    page_icon="🕘",
    layout="wide"
)

st.title("🕘 Research History")

tasks = get_tasks()

if not tasks:

    st.info(
        "No research tasks have been completed yet."
    )

else:

    for task in tasks:

        title = (
            task["task"][:80]
            + (
                "..."
                if len(task["task"]) > 80
                else ""
            )
        )

        with st.expander(
            f"#{task['id']} — {title}"
        ):

            st.write(
                f"**Status:** {task['status']}"
            )

            st.write(
                f"**Created:** {task['created_at']}"
            )

            if task["plan"]:

                st.subheader(
                    "Research Plan"
                )

                st.markdown(
                    task["plan"]
                )

            if task["report"]:

                st.subheader(
                    "Final Report"
                )

                st.markdown(
                    task["report"]
                )