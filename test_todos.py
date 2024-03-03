from todos import Task, TaskManager, parse


def test_can_instantiate_a_task():
    new_task = Task(number=1, description="new task", done=False)

    assert new_task.number == 1
    assert new_task.description == "new task"
    assert new_task.done is False


def test_can_parse_add_command():
    line = "+ other task"

    command = parse(line)

    assert command == {"action": "add", "description": "other task"}


def test_can_parse_set_done_command():
    line = "x 1"

    command = parse(line)

    assert command["action"] == "update"
    assert command["number"] == 1
    assert command["done"] is True


def test_can_parse_set_not_done_command():
    line = "o 2"

    command = parse(line)

    assert command["action"] == "update"
    assert command["number"] == 2
    assert command["done"] is False


def test_task_manager_has_no_tasks_by_default():
    task_manager = TaskManager()

    assert task_manager.tasks == []


def test_add():
    task_manager = TaskManager()

    task_manager.add("new task")

    (actual,) = task_manager.tasks
    assert actual.description == "new task"
    assert actual.number == 1


def test_update():
    """Scenario:

    * Create a TaskManager with one task('task one') that is not done
    * Excecute `update` with `done`: True
    * Check that task number 1 is done
    """
    task_manager = TaskManager()
    task_manager.tasks = [Task(number=1, description="task one", done=False)]

    task_manager.update(number=1, done=True)

    (actual,) = task_manager.tasks
    assert actual.done is True


def test_delete():
    """Scenario:

    * Create a TaskManager with one task('task one') that is not done
    * Delete the first task

    * Call task_manager.execute()

    * Check that tasks list is empty
    """
    task_manager = TaskManager()
    task_manager.tasks = [Task(number=1, description="task one", done=False)]

    task_manager.delete(1)

    assert not task_manager.tasks


def test_delete_non_existing_task():
    task_manager = TaskManager()
    task_manager.tasks = [Task(number=1, description="task one", done=False)]
    task_manager.delete(2)


def test_update_non_existing_task():
    task_manager = TaskManager()
    task_manager.tasks = [Task(number=1, description="task one", done=False)]
    task_manager.update(number=2, done=True)
