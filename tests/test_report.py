from lab.report import render


def test_render_one_row():
    assert render([("widgets", 12.5)]) == "widgets: 12.50"


def test_render_joins_rows_with_newlines():
    assert render([("widgets", 1.0), ("bolts", 2.0)]) == "widgets: 1.00\nbolts: 2.00"
