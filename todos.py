class TaskManager:
    def __init__(self):
        self.tasks = []

    def execute(self, command):
        action = command["action"]
        if action == "add":
            self.execute_add(command)
        elif action == "update":
            self.execute_update(command)
        elif action == "delete":
            self.execute_delete(command)

    def execute_add(self, command):
        description = command["description"]
        number = len(self.tasks) + 1
        task = Task(number=number, description=description, done=False)
        self.tasks.append(task)

    def execute_delete(self, command):
        number = command["number"]
        task = self.find_task(number=number)
        if not task:
            return
        self.tasks = [t for t in self.tasks if t.number != number]

    def execute_update(self, command):
        number = command["number"]
        done = command["done"]
        task = self.find_task(number=number)
        if task:
            task.done = done

    def find_task(self, *, number):
        for i, task in enumerate(self.tasks, start=1):
            if i == number:
                return task
        print("No such task")

    def __str__(self):
        if not self.tasks:
            return "Nothing to be done yet"
        return "\n".join(str(t) for t in self.tasks)


def parse(line):
    first_letter = line[0]
    argument = extract_argument(line)
    if first_letter == "+":
        return {"action": "add", "description": argument}
    elif first_letter == "o":
        number = int(argument)
        return {"action": "update", "number": number, "done": False}
    elif first_letter == "x":
        number = int(argument)
        return {"action": "update", "number": number, "done": True}
    return None


class Task:
    def __init__(self, *, number, description, done):
        self.number = number
        self.description = description
        self.done = done

    def __str__(self):
        box = "[x]" if self.done else "[ ]"
        return f"{self.number} {box} {self.description}"


def extract_argument(line):
    return line[2:]


def main():
    task_manager = TaskManager()
    print(task_manager)
    while True:
        line = input(">>> ")
        if line == "quit":
            break
        command = parse(line)
        if not command:
            print("invalid command")
            continue
        task_manager.execute(command)
        print(task_manager)


if __name__ == "__main__":
    main()
