from lab.queue import Queue


def test_drain_empties_the_queue():
    queue = Queue()
    queue.add("first")
    assert queue.drain() == ["first"]
    assert queue.drain() == []
