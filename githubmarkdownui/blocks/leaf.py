from typing import Optional


def thematic_break() -> str:
    """Returns a <hr> tag, used to create a thematic break. Equivalent to --- in Markdown."""
    pass


def code_block(text: str, language: Optional[str] = None) -> str:
    """Creates a code block using HTML syntax. If language is given, then the code block will be
    created using Markdown syntax, but it cannot be used inside a table.

    :param text: The text inside the code block
    :param language: The language to use for syntax highlighting
    """
    pass


def heading(text: str, level: int) -> str:
    """Returns a heading with the given text, by wrapping the text with a corresponding <h1> to <h6> tag. 1 is the biggest
    heading while 6 is the smallest heading. The level must be between 1 and 6 inclusive.

    :param text: The text for the heading
    :param level: The level of the heading between 1 and 6 inclusive

    :raises: Exception if the level is not between 1 and 6 inclusive
    """
    if not 1 <= level <= 6:
        raise Exception('Level must be between 1 and 6 inclusive')

    return f'<h{level}>{text}</h{level}>'
