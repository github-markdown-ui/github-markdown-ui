from githubmarkdownui import inline


def test_bold():
    assert inline.bold('hello world') == '<strong>hello world</strong>'


def test_code_span():
    assert inline.code_span('print("hello world")') == '<code>print("hello world")</code>'


def test_emphasis():
    assert inline.emphasis('hello world') == '<em>hello world</em>'


def test_italics():
    assert inline.italics('hello world') == '<em>hello world</em>'


def test_link():
    assert inline.link('LinkedIn', 'https://www.linkedin.com/') == '<a href="https://www.linkedin.com/">LinkedIn</a>'


def test_strikethrough():
    assert inline.strikethrough('hello world') == '<del>hello world</del>'


def test_strong_emphasis():
    assert inline.strong_emphasis('hello world') == '<strong>hello world</strong>'
