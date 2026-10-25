from lab.health import is_ready


def test_ready_state():
    assert is_ready("ready") is True


def test_other_states_are_not_ready():
    assert is_ready("starting") is False
