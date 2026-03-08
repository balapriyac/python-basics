def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))

def sum_iterative(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def sum_recursive(numbers):
    if not numbers:       # base case: empty list
        return 0
    return numbers[0] + sum_recursive(numbers[1:])

print(sum_recursive([10, 20, 30, 40]))

catalog = {
    "electronics": {
        "laptops": {
            "ThinkPad X1": 1299.99,
            "MacBook Air": 1099.99
        },
        "accessories": {
            "USB-C Hub": 49.99,
            "Laptop Stand": 34.99
        }
    },
    "stationery": {
        "Notebook A5": 8.99,
        "Gel Pen Set": 12.49
    }
}

def find_all_prices(data):
    prices = []
    for value in data.values():
        if isinstance(value, dict):
            # It's a nested dict — recurse into it
            prices.extend(find_all_prices(value))
        else:
            # It's a price — collect it
            prices.append(value)
    return prices

all_prices = find_all_prices(catalog)
print(f"All prices: {all_prices}")
print(f"Total inventory value: ${sum(all_prices):.2f}")

class FileNode:
    def __init__(self, name, size=0, children=None):
        self.name = name
        self.size = size  # 0 for folders
        self.children = children or []

def total_size(node):
    # Base case: it's a file (no children)
    if not node.children:
        return node.size
    # Recursive case: sum this node's size + all children's sizes
    return node.size + sum(total_size(child) for child in node.children)

# Build a small file tree
project = FileNode("project", children=[
    FileNode("src", children=[
        FileNode("main.py", size=12400),
        FileNode("utils.py", size=5800),
    ]),
    FileNode("data", children=[
        FileNode("sales_jan.parquet", size=302914),
        FileNode("sales_feb.parquet", size=289000),
    ]),
    FileNode("README.md", size=3200)
])

print(f"Total project size: {total_size(project):,} bytes")
print(f"Source files only: {total_size(project.children[0]):,} bytes")

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

from functools import lru_cache

@lru_cache(maxsize=None)
def fib_fast(n):
    if n <= 1:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)

print(fib_fast(10))
print(fib_fast(50))
print(fib_fast(100))

def countdown(n):
    if n == 0:
        return "Done"
    return countdown(n - 1)

print(countdown(5))     # works fine
# print(countdown(2000))  # raises RecursionError

