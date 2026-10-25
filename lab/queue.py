"""A tiny in-memory queue."""


class Queue:
    def __init__(self) -> None:
        self._items: list[str] = []

    def add(self, item: str) -> None:
        self._items.append(item)

    def drain(self) -> list[str]:
        items, self._items = self._items, []
        return items
