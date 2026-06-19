import re


def calculate(expression):
    """
    Calculate a mathematical expression.
    """

    expression = expression.strip()

    # Allow only numbers and mathematical symbols
    allowed_pattern = r"^[0-9+\-*/(). ]+$"

    if not re.match(allowed_pattern, expression):
        return (
            "Invalid expression. "
            "Please use only numbers and +, -, *, / symbols."
        )

    try:
        result = eval(expression)

        return f"The answer is {result}"

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    except Exception:
        return "Invalid mathematical expression."