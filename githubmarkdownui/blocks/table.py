from enum import Enum
from typing import List, Optional


class TableAlignmentError(Exception):
    """Raised when the alignment parameter is not the same length as the number of columns in the table."""


class TableDimensionError(Exception):
    """Raised when each row of the table does not have the same number of columns."""


class TableAlignment(Enum):
    CENTER = 'center'
    LEFT = 'left'
    RIGHT = 'right'


def table(content: List[List[str]], alignment: List[Optional[TableAlignment]] = None) -> str:
    """Creates a table using HTML syntax.

    The content parameter is a list containing lists of equal length, which correspond to the contents of the table.
    The first sublist is the table headers, and each remaining sublist is one row of the table.

    For example, the content parameter [['column 1', 'column 2'], ['this is a long string', 'hello'], ['foo', 'bar']]
    and alignment parameter [TableAlignment.RIGHT, None] would create a table like this:

                 column 1 | column 2
    ----------------------|---------
    this is a long string | hello
                      foo | bar

    :param content: A list of lists containing the contents of the table
    :param alignment: An optional list specifying how each column of the table should be aligned. This list must be the
    same length as the sublists of the content parameter

    :raises: TableAlignmentError when the alignment parameter is not the same length as the sublists of content
    :raises: TableDimensionError when the sublists of content do not contain the same number of elements
    """
    # Check if the inputs are valid. The content parameter must be a m x n matrix and alignment must be the same length as
    # one element in content.
    if not all(isinstance(row, list) and len(row) == len(content[0]) for row in content):
        raise TableDimensionError('Each row in the table must have the same number of columns')

    if alignment and len(alignment) != len(content[0]):
        raise TableAlignmentError('The alignment parameter is not the same length as a row in the table')

    table_syntax = '<table><thead><tr>'

    # Build the table header.
    for index, item in enumerate(content[0]):
        if alignment and alignment[index]:
            table_syntax += f'<th align="{alignment[index].value}">'
        else:
            table_syntax += '<th>'

        table_syntax += f'{item}</th>'

    table_syntax += '</tr></thead><tbody>'

    # Build the table body. Skip the first list in content because that is the table headers.
    for row in content[1:]:
        table_syntax += '<tr>'

        for index, item in enumerate(row):
            if alignment and alignment[index]:
                table_syntax += f'<td align="{alignment[index].value}">'
            else:
                table_syntax += '<td>'

            table_syntax += f'{item}</td>'

        table_syntax += '</tr>'

    table_syntax += '</tbody></table>'

    return table_syntax
