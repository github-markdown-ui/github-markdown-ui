from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List, Union


@dataclass
class HtmlList(ABC):
    """Abstract class for a HTML list. Any HtmlLists inside this one will be displayed as a sublist of the element before it.

    Any child classes must override __str__ to output the list in HTML syntax.
    """
    items: List[Union[str, HtmlList]]

    def build_list_contents(self) -> str:
        """Constructs the contents of the list by building the <li> tags or any nested lists."""
        list_body = ''

        for item in self.items:
            if isinstance(item, HtmlList):
                list_body += str(item)
            else:
                list_body += f'<li>{item}</li>'

        return list_body

    @abstractmethod
    def __str__(self) -> str:
        """Outputs this HtmlList in HTML list syntax."""
        pass


@dataclass
class OrderedList(HtmlList):
    """Class to represent an ordered HTML list. An ordered list is a numbered list, for example:

    1. foo
    2. bar
    3. baz

    The starting number represents the number the list should start counting at.

    To turn this OrderedList into an HTML string, simply cast this object to a str.
    """
    starting_number: int = 1

    def __str__(self) -> str:
        if self.starting_number != 1:
            opening_tag = f'<ol start="{self.starting_number}">'
        else:
            opening_tag = '<ol>'

        return f'{opening_tag}{self.build_list_contents()}</ol>'


@dataclass
class UnorderedList(HtmlList):
    """Class to represent an unordered HTML list. An unordered list is a bullet point list, for example:

    - foo
    - bar
    - baz

    To turn this UnorderedList into an HTML string, simply cast this object to a str.
    """
    def __str__(self) -> str:
        return f'<ul>{self.build_list_contents()}</ul>'


def task_list(items: List[str], items_to_check: Optional[List[int]] = None) -> str:
    """Creates a task list in GitHub Flavored Markdown where each item can be checked off. This task list cannot be used
    inside a table.

    :param items: The items in the task list
    :param items_to_check: The indices (starting from 0) of the items that should be checked off

    :raises: Exception if an index in items_to_check does not exist in the items list
    """
    if not items_to_check:
        items_to_check = []

    for index in items_to_check:
        if index < 0 or index > len(items) - 1:
            raise Exception(f'Cannot check off non-existent index {index} in task list')

    task_list_syntax = ''

    for index, item in enumerate(items):
        task_list_syntax += f'- [{"x" if index in items_to_check else " "}] {item}\n'

    return task_list_syntax.rstrip('\n')
