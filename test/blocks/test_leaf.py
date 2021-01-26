import pytest

from githubmarkdownui.blocks import leaf
from githubmarkdownui.constants import HEADING_MAX_LEVEL, HEADING_MIN_LEVEL


def test_thematic_break():
    assert leaf.thematic_break() == '<hr>'


@pytest.mark.parametrize('language', ['python', None])
def test_code_block(language):
    test_code = 'x = 5\nprint("hello world")'

    result = leaf.code_block(test_code, language)

    if language:
        assert result == '```python\nx = 5\nprint("hello world")\n```'
    else:
        assert result == '<pre><code>x = 5\nprint("hello world")</code></pre>'


@pytest.mark.parametrize('level', [HEADING_MIN_LEVEL, HEADING_MAX_LEVEL, 0, 7])
def test_heading(level):
    if level < HEADING_MIN_LEVEL or level > HEADING_MAX_LEVEL:
        with pytest.raises(Exception):
            leaf.heading('hello world', level)
    else:
        assert leaf.heading('hello world', level) == f'<h{level}>hello world</h{level}>'
