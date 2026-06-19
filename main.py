# ==========================================
# SMART AI PERSONAL ASSISTANT - MAIN PROGRAM
# ==========================================

from settings import (
    BOT_NAME,
    WELCOME_MESSAGE,
    GOODBYE_MESSAGE,
    HELP_MESSAGE
)

from database import (
    create_table,
    register,
    login
)

from file_manager import (
    initialize_files,
    write_file
)

from learning import initialize_learning
from memory import initialize_memory

from chatbot import ChatBot


# ==========================================
# Initial Setup
# ==========================================

def setup():
    """
    Create all required files and databases.
    """

    create_table()
    initialize_files()
    initialize_learning()
    initialize_memory()


# ==========================================
# User Authentication
# ==========================================

def user_menu():
    """
    Register or login user.
    """

    while True:

        print("\n========== USER MENU ==========")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()


        # Register
        if choice == "1":

            username = input(
                "Enter a new username: "
            ).strip()


            if username == "":
                print("Username cannot be empty.")
                continue


            if register(username):

                print(
                    "Account created successfully!"
                )

            else:

                print(
                    "Username already exists."
                )


        # Login
        elif choice == "2":

            username = input(
                "Enter your username: "
            ).strip()


            if login(username):

                print(
                    f"\nWelcome back, {username}!"
                )

                return username


            else:

                print(
                    "User not found. Please register first."
                )


        # Exit
        elif choice == "3":

            return None


        else:

            print(
                "Invalid option. Please try again."
            )


# ==========================================
# Chat Interface
# ==========================================

def start_chat(username):
    """
    Start chatbot conversation.
    """

    bot = ChatBot(username)


    print("\n========================================")
    print(f"Hello {username}!")
    print(f"I am {BOT_NAME}, your AI assistant.")
    print("Type 'help' to see available commands.")
    print("Type 'exit' or 'logout' to close.")
    print("========================================")


    while True:

        message = input("\nYou: ").strip()


        # Empty message
        if message == "":

            print(
                f"{BOT_NAME}: Please enter a message."
            )

            continue


        # Exit commands
        if message.lower() in [
            "exit",
            "logout",
            "bye"
        ]:

            print(
                f"\n{BOT_NAME}: Goodbye {username}!"
            )

            break


        # Help command
        if message.lower() == "help":

            print(HELP_MESSAGE)

            continue


        # Save user's message
        write_file(
            "history.txt",
            f"{username}: {message}"
        )


        # Get chatbot reply
        response = bot.reply(message)


        print(
            f"{BOT_NAME}: {response}"
        )


        # Save bot reply
        write_file(
            "history.txt",
            f"{BOT_NAME}: {response}"
        )


# ==========================================
# Main Function
# ==========================================

def main():

    setup()


    print(WELCOME_MESSAGE)


    username = user_menu()


    if username is None:

        print(GOODBYE_MESSAGE)

        return


    start_chat(username)


    print(GOODBYE_MESSAGE)


# ==========================================
# Run Program
# ==========================================

if __name__ == "__main__":

    main()