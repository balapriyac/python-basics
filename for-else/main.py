# Example 1: Finding a Prime Number
import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n))+ 1):
        if n % i == 0:
            print(f"{n} is divisible by {i}. Not a prime number.")
            break
    else:
        # This block executes if the loop did not encounter a break statement
        print(f"{n} is a prime number.")
        return True

# Example 2: Searching for an Item in a List

def search_item(lst, item):
    for i in lst:
        if i == item:
            print(f"Found {item} in the list.")
            break
    else:
        print(f"{item} is not in the list.")
