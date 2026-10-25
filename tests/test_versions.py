from lab.versions import is_legacy_version, normalise


def test_plain_version_normalises():
    assert normalise("1.2.3") == "1.2.3"


def test_non_pep440_version_is_legacy():
    assert is_legacy_version("1.2.3-not.a.version") is True


def test_pep440_version_is_not_legacy():
    assert is_legacy_version("1.2.3") is False
