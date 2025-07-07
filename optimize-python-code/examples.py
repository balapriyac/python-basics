# before
import time

def square_numbers_loop(numbers):
    result = []
    for num in numbers:
        result.append(num ** 2)
    return result

# Let's test this with 100,000 numbers to see the performance
test_numbers = list(range(1000000))

start_time = time.time()
squared_loop = square_numbers_loop(test_numbers)
loop_time = time.time() - start_time
print(f"Loop time: {loop_time:.4f} seconds")

# after
def square_numbers_comprehension(numbers):
    return [num ** 2 for num in numbers]  # Create the entire list in one line

start_time = time.time()
squared_comprehension = square_numbers_comprehension(test_numbers)
comprehension_time = time.time() - start_time
print(f"Comprehension time: {comprehension_time:.4f} seconds")
print(f"Improvement: {loop_time / comprehension_time:.2f}x faster")

