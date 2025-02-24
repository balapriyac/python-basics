from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    elapsed = time.time() - start
    print(f"Elapsed time: {elapsed:.6f} seconds")

# Usage
with file_manager('test.txt', 'w') as f:
    f.write('Hello, context managers!')

with timer():
    # Code to time
    sum(i*i for i in range(1000000))
