import sqlite3
import os


class Database:
    __db_file = "New/Projects/To-Do list/src/database/data.db"
    __conn = None
    __cursor = None

    @classmethod
    def open_db(cls):
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(cls.__db_file), exist_ok=True)
            print(
                f"Directory created or already exists: {os.path.dirname(cls.__db_file)}"
            )

            # Connect to the database (this will create the file if it doesn't exist)
            cls.__conn = sqlite3.connect(cls.__db_file)
            cls.__cursor = cls.__conn.cursor()
            print(f"Connected to the database: {cls.__db_file}")

            # Create the Task table if it doesn't exist
            cls.__cursor.execute(
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
            cls.__conn.commit()
            print("Table created or already exists.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    @classmethod
    def close_db(cls):
        if cls.__conn:
            cls.__conn.close()
            print("Database connection closed.")

    @classmethod
    def add_db(cls, Title, Description, Date, State):
        try:
            cls.__cursor.execute(
                """INSERT INTO TASKS (Title, Description, Date, State)
                        VALUES (?, ?, ?, ?) """,
                (Title, Description, Date, State),
            )
            cls.__conn.commit()
            print("Task added to the database.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    @classmethod
    def del_db(cls, identifier):
        try:
            cls.__cursor.execute(
                """DELETE FROM TASKS WHERE ID = ? OR Title = ?""",
                (identifier, identifier),
            )
            cls.__conn.commit()
            print("Task deleted from the database.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    @classmethod
    def edit_db(
        cls,
        identifier,
        new_title=None,
        new_description=None,
        new_date=None,
        new_state=None,
    ):
        try:
            # Fetch the existing task details
            cls.__cursor.execute(
                """SELECT Title, Description, Date, State FROM TASKS WHERE ID = ? OR Title = ?""",
                (identifier, identifier),
            )
            task = cls.__cursor.fetchone()

            if task is None:
                print("Task not found.")
                return

            # Use existing values if new values are not provided
            current_title, current_description, current_date, current_state = task
            updated_title = new_title if new_title is not None else current_title
            updated_description = (
                new_description if new_description is not None else current_description
            )
            updated_date = new_date if new_date is not None else current_date
            updated_state = new_state if new_state is not None else current_state

            # Update the task with the new values
            cls.__cursor.execute(
                """UPDATE TASKS
                   SET Title = ?, Description = ?, Date = ?, State = ?
                   WHERE ID = ? OR Title = ?""",
                (
                    updated_title,
                    updated_description,
                    updated_date,
                    updated_state,
                    identifier,
                    identifier,
                ),
            )
            cls.__conn.commit()
            print("Task updated in the database.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")


# Global database instance
db = Database()
