import os
import sqlite3

from dotenv import load_dotenv


load_dotenv()

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "data/agent.db"
)


def get_connection():

    os.makedirs(
        os.path.dirname(DATABASE_PATH),
        exist_ok=True
    )

    connection = sqlite3.connect(
        DATABASE_PATH,
        check_same_thread=False
    )

    connection.row_factory = sqlite3.Row

    return connection


def init_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS research_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            plan TEXT,
            research TEXT,
            evaluation TEXT,
            report TEXT,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()

    connection.close()