import json
import os


FILE_PATH = "data/knowledge.json"


def initialize_learning():
    """
    Create the learning file if it does not exist.
    """

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as file:
            json.dump({}, file, indent=4)


def load_knowledge():
    """
    Load learned knowledge.
    """

    initialize_learning()

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return {}


def get_learned_answer(question):
    """
    Search for a learned answer.
    """

    data = load_knowledge()

    question = question.lower().strip()

    return data.get(question)


def learn_new_answer(question, answer):
    """
    Save new information learned from the user.
    """

    data = load_knowledge()

    data[question.lower().strip()] = answer.strip()

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


    return (
        "Thank you for teaching me. "
        "I have saved this information and "
        "I will remember it during our future conversations."
    )