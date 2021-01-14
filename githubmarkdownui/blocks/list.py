from __future__ import annotations
from abc import ABC
from dataclasses import dataclass
from typing import List, Union


@dataclass
class HtmlList(ABC):
    """Abstract class for a HTML list. Any HtmlLists inside this one will be displayed as a sublist of the element before it.
    """
    items: List[Union[str, HtmlList]]


@dataclass
class OrderedList(HtmlList):
    """Class to represent an ordered HTML list. An ordered list is a numbered list, for example:

    1. foo
    2. bar
    3. baz

    The starting number represents the number the list should start counting at.
    """
    starting_number: int = 1

    def __str__(self) -> str:
        pass


@dataclass
class UnorderedList(HtmlList):
    """Class to represent an unordered HTML list. An unordered list is a bullet point list, for example:

    - foo
    - bar
    - baz
    """
    def __str__(self) -> str:
        pass


def task_list(items: List[str], items_to_check: List[int]) -> str:
    """Creates a task list in Markdown where each item can be checked off. This task list cannot be used inside a table.

    :param items: The items in the task list
    :param items_to_check: The indices (starting from 0) of the items that should be checked off

    :raises: Exception if an index in items_to_check does not exist in the items list
    """
    pass
