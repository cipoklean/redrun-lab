from lab.mode import app_mode


def test_app_mode_is_known():
    assert app_mode() in {"ci", "local"}
