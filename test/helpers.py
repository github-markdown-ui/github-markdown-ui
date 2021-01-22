from re import sub


def remove_whitespace(text: str) -> str:
    """Removes all whitespace from a string (including newline characters) after a > or before a <.

    This function allows us to write the expected HTML syntax outputs of the test cases in a more readable form, as long as
    we don't put whitespace around < or > characters within HTML tags.
    """
    return sub(r'(?<=>)\s+|\s+(?=<)', '', text)
