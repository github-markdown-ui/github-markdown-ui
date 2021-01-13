from typing import List, Optional

from githubmarkdownui.helpers.table import TableAlignment


def heading(text: str, level: int) -> str:
    """Returns a heading with the given text, by wrapping the text with a corresponding <h1> to <h6> tag. 1 is the biggest
    heading while 6 is the smallest heading. The level must be between 1 to 6 inclusive.

    :raise: Exception if the level is not between 1 to 6 inclusive
    """
    pass


def table(content: List[List[str]], alignment: List[Optional[TableAlignment]] = None) -> None:
    """Creates a table using HTML syntax.

    The content parameter is a list containing lists of equal length, which correspond to the contents of the table.
    The first sublist is the table headers, and each remaining sublist is one row of the table.

    For example, the content parameter [['column 1', 'column 2'], ['hello', 'world'], ['foo', 'bar']] would create a
    table like this:

    column 1 | column 2
    ---------|---------
    hello    | world
    foo      | bar

    :param content: A list of lists containing the contents of the table
    :param alignment: An optional list specifying how each column of the table should be aligned. This list must be the
    same length as the sublists of the content parameter

    :raises: TableAlignmentError when the alignment parameter is not the same length as the sublists of content
    :raises: TableDimensionError when the sublists of content do not contain the same number of elements
    """
    pass
