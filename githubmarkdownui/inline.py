def code_span(text: str, delimiter: int = 1) -> str:
    """Returns the text surrounded by backtick (`) characters. If the text
    contains one or more backtick characters, then the delimiter must be set
    to a value that is greater than the number of consecutive backticks.

    :raises: Exception if the delimiter is less than 1
    """
    if delimiter < 1:
        raise Exception('The delimiter must be 1 or more')

    return '`' * delimiter + text + '`' * delimiter
