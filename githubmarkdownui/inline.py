def bold(text: str) -> str:
    """Alternative name for strong_emphasis.

    :param text: The text to be bolded
    """
    return strong_emphasis(text)


def code_span(text: str) -> str:
    """Returns the text surrounded by <code> tags.

    :param text: The text that should appear as a code span
    """
    return f'<code>{text}</code>'


def emphasis(text: str) -> str:
    """Emphasizes (italicizes) the given text by placing <em> tags around it.

    :param text: The text to be emphasized
    """
    return f'<em>{text}</em>'


def italics(text: str) -> str:
    """Alternative name for emphasis.

    :param text: The text to be italicized
    """
    return emphasis(text)


def link(text: str, url: str) -> str:
    """Turns the given text into a link using <a> tags.

    :param text: The text for the link
    :param url: The url for the link
    """
    return f'<a href="{url}">{text}</a>'


def strikethrough(text: str) -> str:
    """Formats the text with a strikethrough by placing <del> tags around it.

    :param text: The text to appear with a strikethrough
    """
    return f'<del>{text}</del>'


def strong_emphasis(text: str) -> str:
    """Strongly emphasizes (bolds) the given text by placing <strong> tags around it.

    :param text: The text to be strongly emphasized
    """
    return f'<strong>{text}</strong>'
