import pytest

import githubmarkdownui.blocks.leaf as leaf


@pytest.mark.parametrize('level', [1, 6, 0, 7])
def test_heading(level):
    if level < 1 or level > 6:
        with pytest.raises(Exception):
            leaf.heading('hello world', level)
    else:
        assert leaf.heading('hello world', level) == f'<h{level}>hello world</h{level}>'
