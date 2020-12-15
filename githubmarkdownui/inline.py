def code_span(string: str, delimiter: int = 1) -> str:
    """Returns a string surrounded by backtick (`) characters. If your string
    contains one or more backtick characters, then the delimiter must be set
    to a value that is greater than the number of consecutive backticks.

    :raises: Exception if the delimiter is less than 1
    """
    if delimiter < 1:
        raise Exception('The delimiter must be 1 or more')

    return '`' * delimiter + string + '`' * delimiter
