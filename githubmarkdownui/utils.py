def check_description(text: str) -> str:
    """Creates a collapsible section with the title 'What is this check?'

    :param text: The text to be displayed inside this check description
    """
    return collapsible_section('What is this check?', text)


def collapsible_section(title: str, text: str) -> str:
    """Creates a collapsible section with the given title, and when expanded will show the given text.

    :param title: The title for this collapsible section
    :param text: The text to be displayed inside this collapsible section
    """
    return f'<details><summary>{title}</summary>\n{text}</details>'
