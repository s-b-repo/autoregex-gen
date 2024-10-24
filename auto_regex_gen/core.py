# auto_regex_gen/core.py

from .patterns import get_patterns

def auto_regex_gen(description: str) -> str:
    """
    Generates regex pattern based on the input description.
    """
    description = description.lower()
    patterns = get_patterns()

    # Check for matches in the description
    for key, pattern in patterns.items():
        if key in description:
            return pattern
    return "No matching regex found."
