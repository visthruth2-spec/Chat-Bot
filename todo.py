from file_manager import write_file, read_file


def add_task(task):
    """
    Add a new task.
    """

    if task.strip() == "":
        return "Task cannot be empty."

    write_file("tasks.txt", task)

    return "Task added successfully."


def show_tasks():
    """
    Display all tasks.
    """

    tasks = read_file("tasks.txt")

    return (
        "========== YOUR TASKS ==========\n"
        + tasks
    )