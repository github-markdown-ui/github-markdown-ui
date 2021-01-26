from githubmarkdownui import utils


def test_check_description():
    assert utils.check_description('hello world') == '<details><summary>What is this check?</summary>\nhello world</details>'


def test_collapsible_section():
    assert (utils.collapsible_section('my title', 'hello world') ==
            '<details><summary>my title</summary>\nhello world</details>')
