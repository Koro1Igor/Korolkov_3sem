import time
from contextlib import contextmanager

# Вариант 1 — класс
class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"time: {time.time() - self.start:.5f}")

# Вариант 2 — contextlib
@contextmanager
def cm_timer_2():
    start = time.time()
    yield
    print(f"time: {time.time() - start:.5f}")

if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(0.5)
    with cm_timer_2():
        time.sleep(0.5)
