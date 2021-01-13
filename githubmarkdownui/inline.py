def bold(text: str) -> str:
    """Alternative name for strong_emphasis."""
    return strong_emphasis(text)


def code_span(text: str) -> str:
    """Returns the text surrounded by <code> tags."""
    pass


def emphasis(text: str) -> str:
    """Emphasizes (italicizes) the given text by placing <em> tags around it."""
    pass


def italics(text: str) -> str:
    """Alternative name for emphasis."""
    return emphasis(text)


def link(text: str, url: str) -> str:
    """Takes the given string and turns it into a link using <a> tags."""
    pass


def strong_emphasis(text: str) -> str:
    """Strongly emphasizes (bolds) the given text by placing <strong> tags around it."""
    pass
