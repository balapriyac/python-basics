from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Watch how fast this runs compared to non-cached version
import time
start = time.time()
result = fibonacci(35)
end = time.time()
print(f"Fibonacci(35) = {result}, calculated in {end-start:.6f} seconds")

# Check cache statistics
print(f"Cache info: {fibonacci.cache_info()}")
