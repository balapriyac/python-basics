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

# before
def find_common_elements_list(list1, list2):
    common = []
    for item in list1:  # Go through each item in the first list
        if item in list2:  # Check if it exists in the second list
            common.append(item)  # If yes, add it to our common list
    return common

# Test with reasonably large lists
large_list1 = list(range(10000))
large_list2 = list(range(5000, 15000))

start_time = time.time()
common_list = find_common_elements_list(large_list1, large_list2)
list_time = time.time() - start_time
print(f"List approach time: {list_time:.4f} seconds")

# after
def find_common_elements_set(list1, list2):
    set2 = set(list2)  # Convert list to a set (one-time cost)
    return [item for item in list1 if item in set2]  # Check membership in set

start_time = time.time()
common_set = find_common_elements_set(large_list1, large_list2)
set_time = time.time() - start_time
print(f"Set approach time: {set_time:.4f} seconds")
print(f"Improvement: {list_time / set_time:.2f}x faster")
