from __future__ import annotations
from abc import ABC
from typing import List, Union


class HtmlList(ABC):
    """Abstract class for a HTML list."""
    def __init__(self, items: List[Union[str, HtmlList]]) -> None:
        """Creates a list using HTML syntax.

        :param items: The items in this list. An HtmlList will be displayed as a sublist of the element before it
        """
        pass


class OrderedList(HtmlList):
    """Class to represent an ordered HTML list. An ordered list is a numbered list, for example:

    1. foo
    2. bar
    3. baz
    """
    def __init__(self, items: List[Union[str, HtmlList]], starting_number: int = 1) -> None:
        """Creates an ordered list using HTML syntax.

        :param items: The items in this list
        :param starting_number: The number of the first item in this list
        """
        pass

    def __str__(self) -> str:
        pass


class UnorderedList(HtmlList):
    """Class to represent an unordered HTML list. An unordered list is a bullet point list, for example:

    - foo
    - bar
    - baz
    """
    def __init__(self, items: List[Union[str, HtmlList]]) -> None:
        pass

    def __str__(self) -> str:
        pass


def task_list(items: List[str], items_to_check: List[int]) -> str:
    """Creates a task list in Markdown where each item can be checked off. This task list cannot be used inside a table.

    :param items: The items in the task list
    :param items_to_check: The indices (starting from 0) of the items that should be checked off

    :raises: Exception if an index in items_to_check does not exist in the items list
    """
    pass
