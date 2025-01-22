import sqlite3
import os

DB_FILE = "New/Projects/To-Do list/Database/data.db"


def open_db():
    # Ensure the directory exists
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

    # Connect to the database (this will create the file if it doesn't exist)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create the Task table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS TASKS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            Title TEXT NOT NULL,
            Description TEXT NOT NULL,
            Date TEXT NOT NULL,
            State TEXT NOT NULL
        )
        """
    )
    conn.commit()
    return conn, cursor


def close_db(conn):
    conn.close()
