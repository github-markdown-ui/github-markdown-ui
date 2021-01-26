import pytest

from githubmarkdownui.blocks import leaf
from githubmarkdownui.constants import HEADING_MAX_LEVEL, HEADING_MIN_LEVEL


@pytest.mark.parametrize('level', [HEADING_MIN_LEVEL, HEADING_MAX_LEVEL, 0, 7])
def test_heading(level):
    if level < HEADING_MIN_LEVEL or level > HEADING_MAX_LEVEL:
        with pytest.raises(Exception):
            leaf.heading('hello world', level)
    else:
        assert leaf.heading('hello world', level) == f'<h{level}>hello world</h{level}>'
