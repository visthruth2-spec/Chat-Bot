from file_manager import write_file, read_file


def add_reminder(reminder):
    """
    Add a reminder.
    """

    if reminder.strip() == "":
        return "Reminder cannot be empty."

    write_file("reminders.txt", reminder)

    return "Reminder saved successfully."


def show_reminders():
    """
    Display all reminders.
    """

    reminders = read_file("reminders.txt")

    return (
        "======= YOUR REMINDERS =======\n"
        + reminders
    )