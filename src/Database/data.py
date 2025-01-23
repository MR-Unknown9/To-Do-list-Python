import sqlite3
import os


class DATA:
    __db_file = "New/Projects/To-Do list/src/database/data.db"
    __conn = None
    __cursor = None

    @classmethod
    def open_db(cls):
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(cls.__db_file), exist_ok=True)

            # Connect to the database (this will create the file if it doesn't exist)
            cls.__conn = sqlite3.connect(cls.__db_file)
            cls.__cursor = cls.__conn.cursor()

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
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    @classmethod
    def close_db(cls):
        if cls.__conn:
            cls.__conn.close()

    @classmethod
    def add_db(cls, Title, Description, Date, State):
        try:
            cls.__cursor.execute(
                """INSERT INTO TASKS (Title, Description, Date, State)
                        VALUES (?, ?, ?, ?) """,
                (Title, Description, Date, State),
            )
            cls.__conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")


# Global database instance
db = DATA()
