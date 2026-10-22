"""Grid knowledge assistant package."""

__version__ = "0.1.0"


def normalize_question(question: str) -> str:
    """Remove leading and trailing whitespace from a question."""
    return question.strip()
