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
    """Class to represent an ordered HTML list."""
    def __init__(self, items: List[Union[str, HtmlList]], starting_number: int = 1) -> None:
        """Creates an ordered list using HTML syntax.

        :param items: The items in this list
        :param starting_number: The number of the first item in this list
        """
        pass

    def __str__(self) -> str:
        pass


class UnorderedList(HtmlList):
    """Class to represent an unordered HTML list."""
    def __init__(self, items: List[Union[str, HtmlList]]) -> None:
        pass

    def __str__(self) -> str:
        pass
