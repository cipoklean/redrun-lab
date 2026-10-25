"""A client built on httpx."""

import httpx


def make_client() -> httpx.Client:
    return httpx.Client(timeout=5.0)
