from lab.dashboard import headline


def test_headline_joins_totals():
    assert headline([1.0, 2.5]) == "1.00 | 2.50"


def test_headline_of_nothing_is_empty():
    assert headline([]) == ""
