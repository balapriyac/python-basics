from functools import cache, lru_cache
import timeit

# without caching
def fibonacci_no_cache(n):
	if n <= 1:
    		return n
	return fibonacci_no_cache(n-1) + fibonacci_no_cache(n-2)

# with cache
@cache
def fibonacci_cache(n):
	if n <= 1:
    		return n
	return fibonacci_cache(n-1) + fibonacci_cache(n-2)

# with LRU cache
@lru_cache(maxsize=None)
def fibonacci_lru_cache(n):
	if n <= 1:
    		return n
	return fibonacci_lru_cache(n-1) + fibonacci_lru_cache(n-2)


n = 35  

no_cache_time = timeit.timeit(lambda: fibonacci_no_cache(n), number=1)
cache_time = timeit.timeit(lambda: fibonacci_cache(n), number=1)
lru_cache_time = timeit.timeit(lambda: fibonacci_lru_cache(n), number=1)

print(f"Time without cache: {no_cache_time:.6f} seconds")
print(f"Time with cache: {cache_time:.6f} seconds")
print(f"Time with LRU cache: {lru_cache_time:.6f} seconds")
