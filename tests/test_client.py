from lab.client import make_client


def test_client_is_constructible():
    with make_client() as client:
        assert client is not None
