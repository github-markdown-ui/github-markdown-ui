from enum import Enum, auto
from typing import List, Optional


class TableAlignmentError(Exception):
    """Raised when the alignment parameter is not the same length as the number of columns in the table."""


class TableDimensionError(Exception):
    """Raised when each row of the table does not have the same number of columns."""


class TableAlignment(Enum):
    CENTER = auto()
    LEFT = auto()
    RIGHT = auto()


def table(content: List[List[str]], alignment: List[Optional[TableAlignment]] = None) -> str:
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
