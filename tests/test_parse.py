from lab.parse import parse_row


def test_parse_row_reads_every_pair():
    assert parse_row("a=1, b=2") == {"a": "1", "b": "2"}


def test_parse_row_with_padding():
    assert parse_row("  key = value  ") == {"key": "value"}
