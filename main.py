import re
from src.database import data
from src.core.task import TASKS
from src.gui import mainGUI

NEW_TASK = TASKS()
DATE_FORMAT = r"^(\d{,2})\/(\d{,2})\/(\d{4})$"


def add_task(new_title, new_description, new_date, new_state):
    if not re.match(DATE_FORMAT, new_date):
        print("Invalid date format. Please use DD/MM/YYYY.")
        return
    NEW_TASK.task = (new_title, new_description, new_date, new_state)
    data.add_db(
        Title=new_title, Description=new_description, Date=new_date, State=new_state
    )


def delete_task():
    pass


def edit_task():
    pass


def search():
    pass


def main():
    conn, cursor = data.open_db()
    add_task("new task", "none", "12/12/2024", "incomplete")
    data.close_db(conn)


if __name__ == "__main__":
    main()
