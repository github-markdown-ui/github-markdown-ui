import pytest

from githubmarkdownui.blocks import lists
from test.helpers import remove_whitespace


def test_unordered_list():
    assert str(lists.UnorderedList(['foo', 'bar', 'baz'])) == remove_whitespace(
        """
        <ul>
            <li>foo</li>
            <li>bar</li>
            <li>baz</li>
        </ul>
        """
    )


@pytest.mark.parametrize('starting_number', [1, 2])
def test_ordered_list(starting_number):
    assert str(lists.OrderedList(['foo', 'bar', 'baz'], starting_number=starting_number)) == remove_whitespace(
        f"""
        {'<ol>' if starting_number == 1 else '<ol start="' + str(starting_number) + '">'}
            <li>foo</li>
            <li>bar</li>
            <li>baz</li>
        </ol>
        """
    )


@pytest.mark.parametrize('outer_list_tags', [
    ['<ul>', '</ul>'],
    ['<ol>', '</ol>'],
])
@pytest.mark.parametrize('inner_list_tags', [
    ['<ul>', '</ul>'],
    ['<ol>', '</ol>'],
])
def test_nested_lists(outer_list_tags, inner_list_tags):
    if inner_list_tags[0] == '<ul>':
        inner_list = lists.UnorderedList(['hello', 'world'])
    else:
        inner_list = lists.OrderedList(['hello', 'world'])

    if outer_list_tags[0] == '<ul>':
        html_list = lists.UnorderedList(['foo', 'bar', inner_list, 'baz'])
    else:
        html_list = lists.OrderedList(['foo', 'bar', inner_list, 'baz'])

    assert str(html_list) == remove_whitespace(
        f"""
        {outer_list_tags[0]}
            <li>foo</li>
            <li>bar</li>
            {inner_list_tags[0]}
                <li>hello</li>
                <li>world</li>
            {inner_list_tags[1]}
            <li>baz</li>
        {outer_list_tags[1]}
        """
    )


def test_task_list():
    assert lists.task_list(['foo', 'bar', 'baz']) == '- [ ] foo\n- [ ] bar\n- [ ] baz'


def test_task_list_check_items():
    assert lists.task_list(['foo', 'bar', 'baz'], [0, 1]) == '- [x] foo\n- [x] bar\n- [ ] baz'


@pytest.mark.parametrize('index', [-1, 3, 8])
def test_task_list_check_invalid_index(index):
    with pytest.raises(Exception):
        lists.task_list(['foo', 'bar', 'baz'], [index])
