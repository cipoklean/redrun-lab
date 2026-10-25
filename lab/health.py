"""Liveness helpers. No credentials involved."""


def is_ready(state: str) -> bool:
    return state == "ready"
