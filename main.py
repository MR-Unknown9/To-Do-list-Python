import re
from src.database.data import db
from src.core.task import task
from src.gui.mainGUI import ToDoApp
import ttkbootstrap as ttkb

DATE_FORMAT = r"\d{2}/\d{2}/\d{4}"


def add_task(new_title, new_description, new_date, new_state):
    if not re.match(DATE_FORMAT, new_date):
        print("Invalid date format. Please use DD/MM/YYYY.")
        return
    task.task = (new_title, new_description, new_date, new_state)
    db.add_db(
        Title=new_title, Description=new_description, Date=new_date, State=new_state
    )


def delete_task(identifier):
    db.del_db(identifier)


def edit_task(
    identifier, new_title=None, new_description=None, new_date=None, new_state=None
):
    db.edit_db(identifier, new_title, new_description, new_date, new_state)


def search_task(identifier=None):
    if identifier:
        task = db.search_db(identifier)
        if task:
            return task
        else:
            return []
    else:
        return db.fetch_all_tasks()


def main():
    db.open_db()
    root = ttkb.Window(themename="cosmo")
    app = ToDoApp(root, add_task, edit_task, delete_task, search_task)
    root.mainloop()
    db.close_db()


if __name__ == "__main__":
    main()
