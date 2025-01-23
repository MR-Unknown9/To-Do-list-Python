class TASKS:

    def __init__(self):
        self.__title = None
        self.__description = None
        self.__date = None
        self.__state = None

    @property
    def task(self):
        return self.__title, self.__description, self.__date, self.__state

    @task.setter
    def task(self, task_details):
        self.__title, self.__description, self.__date, self.__state = task_details

    @task.deleter
    def task(self):
        del self.__title
        del self.__description
        del self.__date
        del self.__state


task = TASKS()
