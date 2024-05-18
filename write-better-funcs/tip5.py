# returns a list of Fibonacci numbers
def generate_fibonacci_numbers_list(limit):
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-1] + fibonacci_numbers[-2] <= limit:
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers


# use generators instead
from typing import Generator

def generate_fibonacci_numbers(limit: int) -> Generator[int, None, None]:
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Usage
limit = 100
fibonacci_numbers_generator = generate_fibonacci_numbers(limit)
for num in fibonacci_numbers_generator:
    print(num)
