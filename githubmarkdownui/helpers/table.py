from enum import Enum, auto


class TableAlignmentError(Exception):
    """Raised when the alignment parameter is not the same length as the number of columns in the table."""


class TableDimensionError(Exception):
    """Raised when each row of the table does not have the same number of columns."""


class TableAlignment(Enum):
    CENTER = auto()
    LEFT = auto()
    RIGHT = auto()
