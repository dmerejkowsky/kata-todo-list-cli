# Todo List Command Line Kata

*Goal: practice converting notebooks to command line interfaces*

# Specification

Each task is made of

* A description
* A number that identifies it
* A status "done" or "to do"

The TasksManager can interpret some commands, like this:

* `+ description>` Add a task
* `- <id>` Remove the task matching the given id
* `x <id>` Set the status of the task matching the id to "done"
* `o <id>` Set the status of the task matching the id to "to do"
* `q` Exit the interaction loop
