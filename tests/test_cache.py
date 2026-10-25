import time

from lab.cache import warm


def test_warm_is_quick():
    started = time.perf_counter()
    assert warm(50) == 50
    elapsed = time.perf_counter() - started
    assert elapsed < 0.05, f"cache warm took {elapsed:.3f}s"
