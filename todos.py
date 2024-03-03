class Task:
    def __init__(self, *, number, description, done):
        self.number = number
        self.description = description
        self.done = done

    def __str__(self):
        box = "[x]" if self.done else "[ ]"
        return f"{self.number} {box} {self.description}"

    def __repr__(self):
        return f"Task<#{self.number} -{self.description} - done: {self.done}>"


class TaskManager:
    def __init__(self):
        self.tasks = []

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

    def __str__(self):
        if not self.tasks:
            return "Nothing to be done yet"
        return "\n".join(str(t) for t in self.tasks)
