from database.connection import get_connection


def create_task(task):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO research_tasks (task, status)
        VALUES (?, ?)
        """,
        (task, "running")
    )

    task_id = cursor.lastrowid

    connection.commit()

    connection.close()

    return task_id


def update_task(
    task_id,
    plan=None,
    research=None,
    evaluation=None,
    report=None,
    status=None
):

    connection = get_connection()

    cursor = connection.cursor()

    fields = []
    values = []

    if plan is not None:
        fields.append("plan = ?")
        values.append(plan)

    if research is not None:
        fields.append("research = ?")
        values.append(research)

    if evaluation is not None:
        fields.append("evaluation = ?")
        values.append(evaluation)

    if report is not None:
        fields.append("report = ?")
        values.append(report)

    if status is not None:
        fields.append("status = ?")
        values.append(status)

    if fields:

        values.append(task_id)

        query = f"""
        UPDATE research_tasks
        SET {", ".join(fields)}
        WHERE id = ?
        """

        cursor.execute(query, values)

        connection.commit()

    connection.close()


def get_tasks():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM research_tasks
        ORDER BY created_at DESC
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return rows


def get_task(task_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM research_tasks
        WHERE id = ?
        """,
        (task_id,)
    )

    row = cursor.fetchone()

    connection.close()

    return row


def save_document(filename, content):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO documents
        (filename, content)
        VALUES (?, ?)
        """,
        (filename, content)
    )

    connection.commit()

    connection.close()


def get_documents():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM documents
        ORDER BY created_at DESC
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return rows


def get_dashboard_stats():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM research_tasks"
    )

    tasks = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM research_tasks
        WHERE status = 'completed'
        """
    )

    completed = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM documents"
    )

    documents = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM research_tasks
        WHERE report IS NOT NULL
        """
    )

    reports = cursor.fetchone()[0]

    connection.close()

    return {
        "tasks": tasks,
        "completed": completed,
        "documents": documents,
        "reports": reports
    }