# 1. bisect

from bisect import bisect_left, bisect_right, insort

# Let's create a grade tracking system
grades = [60, 70, 75, 85, 90, 95]

# Find where to insert a new grade while keeping the list sorted
new_grade = 82
position = bisect_left(grades, new_grade)
print(f"Insert 82 at position: {position}")

# Insert while maintaining sort order
insort(grades, new_grade)
print(f"Grades after insertion: {grades}")

# Find grade ranges
def grade_to_letter(score):
	breakpoints = [60, 70, 80, 90]  # F, D, C, B, A
	grades = 'FDCBA'
	position = bisect_right(breakpoints, score)
	return grades[position]

print(f"Score 82 gets grade: {grade_to_letter(82)}")
print(f"Score 75 gets grade: {grade_to_letter(75)}")

# 2. itertools.pairwise


from itertools import pairwise

# Let's analyze temperature changes
temperatures = [20, 23, 24, 25, 23, 22, 20]

# Calculate temperature changes between consecutive readings
changes = []
for prev, curr in pairwise(temperatures):
	change = curr - prev
	changes.append(change)

print("Temperature changes:", changes)


# Calculate moving averages
moving_averages = []
for t1, t2 in pairwise(temperatures):
	avg = (t1 + t2) / 2
	moving_averages.append(avg)

print("Moving averages:", moving_averages)

# Finding the largest temperature jump
max_jump = max(abs(b - a) for a, b in pairwise(temperatures))
print(f"Largest temperature change: {max_jump} degrees")


# 3. statistics.fmean

from statistics import mean, fmean
import time

# Let's compare fmean with traditional mean using a real-world example
# Imagine we're analyzing daily temperature readings
temperatures = [
	21.5, 22.1, 23.4, 22.8, 21.8,
	23.2, 22.7, 23.1, 22.6, 21.9
] * 100000  # Create a large dataset

# Let's compare speed and precision
start_time = time.perf_counter()
regular_mean = mean(temperatures)
regular_time = time.perf_counter() - start_time

start_time = time.perf_counter()
fast_mean = fmean(temperatures)
fast_time = time.perf_counter() - start_time

print(f"Regular mean: {regular_mean:.10f} (took {regular_time:.4f} seconds)")
print(f"fmean: {fast_mean:.10f} (took {fast_time:.4f} seconds)")

# 4. itertools.takewhile

from itertools import takewhile

# Processing log entries until an error
log_entries = [
	"INFO: System started",
	"INFO: Loading data",
	"INFO: Processing users",
	"ERROR: Database connection failed",
	"INFO: Retrying connection",
]

# Get all logs until first error
normal_operation = list(takewhile(
	lambda x: not x.startswith("ERROR"),
	log_entries
))
print("Logs before first error:")
for entry in normal_operation:
	print(entry)

# 5. operator.attrgettr  

from operator import attrgetter
from datetime import datetime

# Let's create a simple class to demonstrate
class Article:
    def __init__(self, title, author, views, date):
        self.title = title
        self.author = author
        self.stats = type('Stats', (), {'views': views})  # Nested attribute
        self.date = date

    def __repr__(self):
        return f"{self.title} by {self.author}"

# Create some sample articles
articles = [
	Article("Python Tips", "Alice", 1500, datetime(2025, 1, 15)),
	Article("Data Science", "Bob", 2500, datetime(2025, 1, 20)),
	Article("Web Dev", "Alice", 1800, datetime(2025, 1, 10))
]

# Sort articles by multiple criteria
get_author_views = attrgetter('author', 'stats.views')

# Sort by author and then by views
sorted_articles = sorted(articles, key=get_author_views)
for article in sorted_articles:
	print(f"{article.author}: {article.title} ({article.stats.views} views)")

# You can also use it to extract specific attributes
dates = list(map(attrgetter('date'), articles))
print("\nArticle dates:", dates)

# 6. itertools.chain


from itertools import chain

# Let's say we're processing data from multiple sources
sales_data = [
	[('Jan', 100), ('Feb', 150)],
	[('Mar', 200), ('Apr', 180)],
	[('May', 210), ('Jun', 190)]
]

# Flatten the data efficiently
flat_sales = list(chain.from_iterable(sales_data))
print("Flattened sales data:", flat_sales)

# List comprehension approach (creates intermediate list):
flat_list = [item for sublist in sales_data for item in sublist]

# chain.from_iterable approach (generates items one at a time):
flat_iterator = chain.from_iterable(sales_data)

     


     
   

