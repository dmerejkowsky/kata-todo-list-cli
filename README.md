# Todo List Command Line Kata

*Goal: practice converting notebooks to command line interfaces*

# Specification

Each task is made of

* A description
* A number that identifies it
* A status "done" or "to do"

The TasksManager implements a few methods to add, update and remove tasks from the list.

# Instructions

Write a CLI so that you can use the task manager from the command line, like this:

## Step 1

Add a cli using
[argparse](https://docs.python.org/3/howto/argparse.html#argparse-tutorial)
that only shows the list of tasks:

```
$ task-manager
```

## Step 2

Add sub-parsers so that you can use `task-manager` with a sub-command, like this
[argparse](https://docs.python.org/3/howto/argparse.html#argparse-tutorial)

```
$ task-manager list                          # List all tasks
$ task-manager add "Learn how to make CLIS"  # Add a new task
$ task-manager complete-task --number=1      # Mark task number 1 as done
$ task-manager undo-task --number=1          # Mark task number 2 as not done
$ taks-manger delete-task --number=1         # Delete task number 1
```

Make sure to call `TaskManager.save_tasks()` at the end of each command

## Step 3

By default, tasks are load and saved from a file named `tasks.pickle` - and the possibility
to set the file path from the command line
