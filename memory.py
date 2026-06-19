import json
import os


FILE_PATH = "data/memory.json"


def initialize_memory():
    """
    Create memory file if it does not exist.
    """

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as file:
            json.dump({}, file, indent=4)


def load_memory():
    """
    Load stored memory.
    """

    initialize_memory()

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return {}


def save_memory(key, value):
    """
    Save user information.
    """

    data = load_memory()

    data[key.lower().strip()] = value.strip()

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def get_memory(key):
    """
    Retrieve remembered information.
    """

    data = load_memory()

    return data.get(key.lower().strip())