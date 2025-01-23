import re
from src.database.data import db
from src.core.task import task
from src.gui import mainGUI

DATE_FORMAT = r"^(\d{,2})\/(\d{,2})\/(\d{4})$"


def add_task(new_title, new_description, new_date, new_state):
    # will change the format
    # if not re.match(DATE_FORMAT, new_date):
    #     return
    task.task = (new_title, new_description, new_date, new_state)
    db.add_db(
        Title=new_title, Description=new_description, Date=new_date, State=new_state
    )


def delete_task():
    pass


def edit_task():
    pass


def search():
    pass


def main():
    db.open_db()
    add_task("new sdfasfd", "none", "12-12-2024", "incomplete")
    db.close_db()

if __name__ == "__main__":
    main()
