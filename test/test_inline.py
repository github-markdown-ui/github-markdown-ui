import pytest

import githubmarkdownui.inline as inline


@pytest.mark.parametrize('string, delimiter', [
    ('hello world', 1),
    ('hello ` world', 2),
    ('hello world', 0),
])
def test_code_span(string, delimiter):
    if delimiter == 0:
        with pytest.raises(Exception):
            inline.code_span(string, delimiter=delimiter)
    else:
        assert inline.code_span(string, delimiter=delimiter) == '`' * delimiter + string + '`' * delimiter
