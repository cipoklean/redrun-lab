from lab.index import build_index


def test_index_covers_every_row():
    """One call, so the coin flip in the module decides the run exactly once."""
    index = build_index(["alpha", "beta", "gamma"])
    assert len(index) == 3
    assert index == {"alpha": 0, "beta": 1, "gamma": 2}
