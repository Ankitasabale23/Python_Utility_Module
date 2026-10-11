import os
from datetime import datetime


def is_valid_email(email):
    """Check whether an email has a basic valid format."""
    email = email.strip()

    if " " in email or email.count("@") != 1:
        return False

    username, domain = email.split("@")

    return bool(username and "." in domain and not domain.startswith(".")
                and not domain.endswith("."))


def is_valid_number(value):
    """Check whether a value can be converted to a number."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def format_currency(amount):
    """Format a number as Indian rupees."""
    return f"Rs. {amount:,.2f}"


def calculate_percentage(value, total):
    """Calculate the percentage of a value out of a total."""
    if total == 0:
        raise ValueError("Total cannot be zero.")

    return (value / total) * 100


def get_current_date():
    """Return today's date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")


def write_text_file(filename, content):
    """Write text content to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def read_text_file(filename):
    """Read and return text content from a file."""
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    with open(filename, "r", encoding="utf-8") as file:
        return file.read()