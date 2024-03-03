import pickle
from pathlib import Path

DB_PATH = Path("tasks.pickle")


class Task:
    def __init__(self, *, number, description, done):
        self.number = number
        self.description = description
        self.done = done

    def __repr__(self):
        box = "[x]" if self.done else "[ ]"
        return f"{self.number} {box} {self.description}"


class TaskManager:
    def __init__(self, db_path=Path("tasks.pickle"), clear=False):
        self.db_path = db_path
        self.load_tasks()
        if clear:
            self.tasks = []

    def load_tasks(self):
        if self.db_path.exists():
            with self.db_path.open("rb") as source:
                self.tasks = pickle.load(source)
        else:
            self.tasks = []

    def save_tasks(self):
        with self.db_path.open("wb") as destination:
            pickle.dump(self.tasks, destination)

    def add(self, description):
        number = len(self.tasks) + 1
        task = Task(number=number, description=description, done=False)
        self.tasks.append(task)

    def delete(self, number):
        task = self._find_task(number=number)
        if not task:
            return
        self.tasks = [t for t in self.tasks if t.number != number]

    def update(self, *, number, done):
        task = self._find_task(number=number)
        if task:
            task.done = done

    def _find_task(self, *, number):
        for i, task in enumerate(self.tasks, start=1):
            if i == number:
                return task
        print("No such task")

    def __repr__(self):
        if not self.tasks:
            return "Nothing to be done yet"
        return "\n".join(str(t) for t in self.tasks)
