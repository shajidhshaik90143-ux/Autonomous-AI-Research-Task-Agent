import streamlit as st

from database.queries import get_tasks


st.set_page_config(
    page_title="Tasks",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Research Tasks")

tasks = get_tasks()

if not tasks:

    st.info(
        "No tasks available."
    )

else:

    for task in tasks:

        col1, col2, col3 = st.columns(
            [5, 2, 2]
        )

        with col1:

            st.write(
                f"**#{task['id']}** "
                f"{task['task']}"
            )

        with col2:

            status = task["status"]

            if status == "completed":

                st.success(
                    status
                )

            elif status == "failed":

                st.error(
                    status
                )

            else:

                st.warning(
                    status
                )

        with col3:

            st.write(
                task["created_at"]
            )