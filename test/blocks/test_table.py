import pytest

from githubmarkdownui.blocks import table

from test.helpers import remove_whitespace


def test_table():
    assert table.table([['col1', 'col2'], ['hello', 'world'], ['foo', 'bar']]) == remove_whitespace(
        """
        <table>
            <thead>
                <tr>
                    <th>col1</th>
                    <th>col2</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>hello</td>
                    <td>world</td>
                </tr>
                <tr>
                    <td>foo</td>
                    <td>bar</td>
                </tr>
            </tbody>
        </table>
        """
    )


@pytest.mark.parametrize('alignment', [table.TableAlignment.CENTER, table.TableAlignment.LEFT, table.TableAlignment.RIGHT])
def test_table_with_alignment(alignment):
    assert table.table([['col1', 'col2'], ['hello', 'world']], [alignment, alignment]) == remove_whitespace(
        f"""
        <table>
            <thead>
                <tr>
                    <th align="{alignment.value}">col1</th>
                    <th align="{alignment.value}">col2</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="{alignment.value}">hello</td>
                    <td align="{alignment.value}">world</td>
                </tr>
            </tbody>
        </table>
        """
    )


def test_table_with_only_one_aligned_column():
    assert table.table([['col1', 'col2'], ['hello', 'world']], [table.TableAlignment.CENTER, None]) == remove_whitespace(
        """
        <table>
            <thead>
                <tr>
                    <th align="center">col1</th>
                    <th>col2</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td align="center">hello</td>
                    <td>world</td>
                </tr>
            </tbody>
        </table>
        """
    )


def test_table_alignment_error():
    with pytest.raises(table.TableAlignmentError):
        table.table([['col1', 'col2'], ['hello', 'world']], [table.TableAlignment.CENTER])


def test_table_dimension_error():
    with pytest.raises(table.TableDimensionError):
        table.table([['col1', 'col2'], ['hello']])
