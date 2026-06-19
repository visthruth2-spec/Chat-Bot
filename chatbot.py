import re
import datetime

from settings import BOT_NAME
from responses import get_response
from knowledge import search_knowledge
from learning import (
    get_learned_answer,
    learn_new_answer
)

from memory import (
    save_memory,
    get_memory
)

from calculator import calculate

from todo import (
    add_task,
    show_tasks
)

from reminder import (
    add_reminder,
    show_reminders
)

from file_manager import (
    write_file,
    read_file
)


class ChatBot:

    def __init__(self, username):
        self.username = username


    def reply(self, message):

        text = message.lower().strip()


        # =============================
        # Greetings
        # =============================
        if text in ["hello", "hi", "hey"]:
            return (
                f"Hello {self.username}! "
                f"I am {BOT_NAME}. How can I help you today?"
            )


        # Good Morning
        if "good morning" in text:
            return get_response("morning")


        # Good Evening
        if "good evening" in text:
            return get_response("evening")


        # How are you
        if "how are you" in text:
            return get_response("how_are_you")


        # Bot name
        if "your name" in text:
            return (
                f"My name is {BOT_NAME}. "
                "I am your personal AI assistant."
            )


        # Abilities
        if (
            "what can you do" in text
            or "your abilities" in text
            or "help me" in text
        ):
            return get_response("abilities")


        # Thank you
        if (
            "thank you" in text
            or "thanks" in text
        ):
            return get_response("thanks")


        # Jokes
        if "joke" in text:
            return get_response("jokes")


        # =============================
        # Date and Time
        # =============================
        if "date" in text:
            today = datetime.datetime.now()

            return (
                "Today's date is: "
                + today.strftime("%d-%m-%Y")
            )


        if "time" in text:
            current = datetime.datetime.now()

            return (
                "Current time is: "
                + current.strftime("%I:%M:%S %p")
            )


        # =============================
        # Calculator
        # =============================
        if text == "calculate":

            expression = input(
                "Enter calculation: "
            )

            return calculate(expression)


        # =============================
        # Notes
        # =============================
        if text == "add note":

            note = input(
                "Enter your note: "
            )

            write_file(
                "notes.txt",
                note
            )

            return "Your note has been saved."


        if text == "show notes":

            return read_file(
                "notes.txt"
            )


        # =============================
        # Task Manager
        # =============================
        if text == "add task":

            task = input(
                "Enter your task: "
            )

            return add_task(task)


        if text == "show tasks":

            return show_tasks()


        # =============================
        # Reminder Manager
        # =============================
        if text == "add reminder":

            reminder = input(
                "Enter your reminder: "
            )

            return add_reminder(reminder)


        if text == "show reminders":

            return show_reminders()


        # =============================
        # Memory System
        # Example:
        # My favorite color is black
        # =============================
        remember = re.search(
            r"my (.+) is (.+)",
            text
        )

        if remember:

            key = remember.group(1)
            value = remember.group(2)

            save_memory(
                key,
                value
            )

            return (
                f"Okay {self.username}, "
                f"I will remember that your "
                f"{key} is {value}."
            )


        # Recall memory
        # Example:
        # What is my favorite color
        # =============================
        recall = re.search(
            r"what is my (.+)",
            text
        )


        if recall:

            key = recall.group(1)

            answer = get_memory(key)

            if answer:

                return (
                    f"Your {key} is {answer}."
                )

            return (
                "I don't have that information yet."
            )


        # =============================
        # Built-in knowledge
        # =============================
        answer = search_knowledge(text)

        if answer:
            return answer


        # =============================
        # Learned knowledge
        # =============================
        answer = get_learned_answer(text)

        if answer:
            return answer


        # =============================
        # Unknown Question Handling
        # =============================
        print(
            f"{BOT_NAME}: Hmm, I don't know "
            "this information yet."
        )

        choice = input(
            f"{BOT_NAME}: Would you like "
            "to teach me this? (yes/no): "
        ).lower()


        if choice == "yes":

            new_answer = input(
                "Enter the answer: "
            )

            return learn_new_answer(
                text,
                new_answer
            )


        return get_response("unknown")