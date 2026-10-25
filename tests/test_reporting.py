from lab.reporting import Row, describe


def test_describe_formats_an_amount():
    assert describe(Row("widgets", 12.5)) == "widgets: 12.50"


def test_describe_handles_a_missing_amount():
    assert describe(Row("bolts")) == "bolts: n/a"
