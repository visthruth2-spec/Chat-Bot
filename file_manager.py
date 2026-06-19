import os


DATA_FOLDER = "data"


FILES = [
    "history.txt",
    "notes.txt",
    "tasks.txt",
    "reminders.txt"
]


def initialize_files():
    """
    Create data folder and all required files.
    """

    os.makedirs(DATA_FOLDER, exist_ok=True)


    for filename in FILES:

        path = os.path.join(DATA_FOLDER, filename)

        if not os.path.exists(path):

            with open(path, "w"):
                pass


def write_file(filename, text):
    """
    Add new text to a file.
    """

    initialize_files()

    path = os.path.join(DATA_FOLDER, filename)


    with open(path, "a", encoding="utf-8") as file:

        file.write(text + "\n")


def read_file(filename):
    """
    Read a file and return its contents.
    """

    initialize_files()

    path = os.path.join(DATA_FOLDER, filename)


    with open(path, "r", encoding="utf-8") as file:

        data = file.read()


    if data.strip() == "":
        return "No information found."


    return data


def clear_file(filename):
    """
    Remove all contents from a file.
    """

    path = os.path.join(DATA_FOLDER, filename)


    with open(path, "w", encoding="utf-8") as file:

        file.write("")