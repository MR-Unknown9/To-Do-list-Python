import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *


class ToDoApp:
    def __init__(
        self,
        root,
        add_task_callback,
        edit_task_callback,
        delete_task_callback,
        search_task_callback,
    ):
        self.root = root
        self.root.title("To-Do List App")
        self.style = ttkb.Style("cosmo")

        self.add_task_callback = add_task_callback
        self.edit_task_callback = edit_task_callback
        self.delete_task_callback = delete_task_callback
        self.search_task_callback = search_task_callback

        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = ttkb.Label(self.root, text="Title:")
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = ttkb.Entry(self.root)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        # Description
        self.desc_label = ttkb.Label(self.root, text="Description:")
        self.desc_label.grid(row=1, column=0, padx=10, pady=10)
        self.desc_entry = ttkb.Entry(self.root)
        self.desc_entry.grid(row=1, column=1, padx=10, pady=10)

        # Date
        self.date_label = ttkb.Label(self.root, text="Date (DD/MM/YYYY):")
        self.date_label.grid(row=2, column=0, padx=10, pady=10)
        self.date_entry = ttkb.Entry(self.root)
        self.date_entry.grid(row=2, column=1, padx=10, pady=10)

        # State
        self.state_label = ttkb.Label(self.root, text="State:")
        self.state_label.grid(row=3, column=0, padx=10, pady=10)
        self.state_entry = ttkb.Entry(self.root)
        self.state_entry.grid(row=3, column=1, padx=10, pady=10)

        # Buttons
        self.add_button = ttkb.Button(
            self.root, text="Add Task", command=self.add_task, bootstyle=SUCCESS
        )
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

        self.edit_button = ttkb.Button(
            self.root, text="Edit Task", command=self.edit_task, bootstyle=WARNING
        )
        self.edit_button.grid(row=4, column=1, padx=10, pady=10)

        self.delete_button = ttkb.Button(
            self.root, text="Delete Task", command=self.delete_task, bootstyle=DANGER
        )
        self.delete_button.grid(row=5, column=0, padx=10, pady=10)

        self.search_button = ttkb.Button(
            self.root, text="Search Task", command=self.search_task, bootstyle=INFO
        )
        self.search_button.grid(row=5, column=1, padx=10, pady=10)

        # Task List
        self.task_list = ttkb.Treeview(
            self.root,
            columns=("Title", "Description", "Date", "State"),
            show="headings",
        )
        self.task_list.heading("Title", text="Title")
        self.task_list.heading("Description", text="Description")
        self.task_list.heading("Date", text="Date")
        self.task_list.heading("State", text="State")
        self.task_list.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.refresh_task_list()

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()
        date = self.date_entry.get()
        state = self.state_entry.get()
        self.add_task_callback(title, description, date, state)
        self.refresh_task_list()

    def edit_task(self):
        selected_item = self.task_list.selection()[0]
        title = self.task_list.item(selected_item, "values")[0]
        new_title = self.title_entry.get()
        new_description = self.desc_entry.get()
        new_date = self.date_entry.get()
        new_state = self.state_entry.get()
        self.edit_task_callback(title, new_title, new_description, new_date, new_state)
        self.refresh_task_list()

    def delete_task(self):
        selected_item = self.task_list.selection()[0]
        title = self.task_list.item(selected_item, "values")[0]
        self.delete_task_callback(title)
        self.refresh_task_list()

    def search_task(self):
        title = self.title_entry.get()
        task = self.search_task_callback(title)
        if task:
            self.task_list.delete(*self.task_list.get_children())
            self.task_list.insert("", "end", values=task)
        else:
            self.refresh_task_list()

    def refresh_task_list(self):
        self.task_list.delete(*self.task_list.get_children())
        tasks = self.search_task_callback(None)
        for task in tasks:
            self.task_list.insert("", "end", values=task)
