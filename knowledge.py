# ==========================================
# BUILT-IN KNOWLEDGE DATABASE
# ==========================================


KNOWLEDGE = {

    "python":
        """
Python is a high-level programming language that is easy to learn.
It is widely used in web development, artificial intelligence,
machine learning, automation, and data science.
        """,


    "java":
        """
Java is an object-oriented programming language used to build
desktop applications, mobile apps, web applications, and enterprise software.
        """,


    "artificial intelligence":
        """
Artificial Intelligence is a branch of computer science that allows
machines to simulate human intelligence and solve problems.
        """,


    "machine learning":
        """
Machine Learning is a field of AI where systems learn from data
and improve without being explicitly programmed.
        """,


    "database":
        """
A database is an organized collection of information that can be
stored, managed, and retrieved efficiently.
        """,


    "computer":
        """
A computer is an electronic machine that receives input,
processes data, stores information, and produces output.
        """,


    "internet":
        """
The Internet is a worldwide network that connects millions of
computers and allows sharing of information.
        """,


    "algorithm":
        """
An algorithm is a step-by-step method used to solve a problem
or perform a task.
        """,


    "operating system":
        """
An operating system is software that manages computer hardware,
software resources, and provides services to applications.
        """
}


def search_knowledge(question):
    """
    Search a question in the knowledge base.
    """

    question = question.lower()


    for keyword, answer in KNOWLEDGE.items():

        if keyword in question:
            return answer.strip()


    return None