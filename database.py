import sqlite3
import os


DATABASE_PATH = "data/chatbot.db"


def connect_database():
    """
    Connect to SQLite database.
    """

    os.makedirs("data", exist_ok=True)

    return sqlite3.connect(DATABASE_PATH)


def create_table():
    """
    Create users table.
    """

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL
        )
    """)

    connection.commit()

    connection.close()


def register(username):
    """
    Register a new user.
    """

    if username.strip() == "":
        return False

    try:
        connection = connect_database()

        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO users(username) VALUES (?)",
            (username.strip(),)
        )

        connection.commit()
        connection.close()

        return True


    except sqlite3.IntegrityError:
        return False



def login(username):
    """
    Check whether a user exists.
    """

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT username FROM users WHERE username = ?",
        (username.strip(),)
    )

    user = cursor.fetchone()

    connection.close()

    return user is not None