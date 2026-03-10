# install pandas and NumPy to run the last two examples


# 1. Measuring Before Optimizing

import time

def load_records():
    # Simulate loading 100,000 records
    return list(range(100_000))

def filter_records(records):
    return [r for r in records if r % 2 == 0]

def generate_report(records):
    return sum(records)

# Time each step
start = time.perf_counter()
records = load_records()
print(f"Load     : {time.perf_counter() - start:.4f}s")

start = time.perf_counter()
filtered = filter_records(records)
print(f"Filter   : {time.perf_counter() - start:.4f}s")

start = time.perf_counter()
report = generate_report(filtered)
print(f"Report   : {time.perf_counter() - start:.4f}s")

# 2. Using Built-in Functions and Standard Library Tools

import time

numbers = list(range(1_000_000))

# Manual loop
start = time.perf_counter()
total = 0
for n in numbers:
    total += n
print(f"Manual loop : {time.perf_counter() - start:.4f}s  →  {total}")

# Built-in sum()
start = time.perf_counter()
total = sum(numbers)
print(f"Built-in    : {time.perf_counter() - start:.4f}s  →  {total}")

orders = [
    {"id": "ORD-003", "amount": 250.0},
    {"id": "ORD-001", "amount": 89.99},
    {"id": "ORD-002", "amount": 430.0},
]

# Slow: manual comparison logic
def manual_sort(orders):
    for i in range(len(orders)):
        for j in range(i + 1, len(orders)):
            if orders[i]["amount"] > orders[j]["amount"]:
                orders[i], orders[j] = orders[j], orders[i]
    return orders

# Fast: built-in sorted()
sorted_orders = sorted(orders, key=lambda o: o["amount"])
print(sorted_orders)

# 3. Avoiding Repeated Work Inside Loops

import time

approved = ["SKU-001", "SKU-002", "SKU-003", "SKU-004", "SKU-005"] * 1000
incoming = [f"SKU-{str(i).zfill(3)}" for i in range(5000)]

# Slow: len() and list membership check on every iteration
start = time.perf_counter()
valid = []
for code in incoming:
    if code in approved:        # list search is O(n) — slow
        valid.append(code)
print(f"List check : {time.perf_counter() - start:.4f}s  →  {len(valid)} valid")

# Fast: convert approved to a set once, before the loop
start = time.perf_counter()
approved_set = set(approved)    # set lookup is O(1) — fast
valid = []
for code in incoming:
    if code in approved_set:
        valid.append(code)
print(f"Set check  : {time.perf_counter() - start:.4f}s  →  {len(valid)} valid")

import re

# Slow: recompiles the pattern on every call
def extract_slow(text):
    return re.findall(r'\d+', text)

# Fast: compile once, reuse
DIGIT_PATTERN = re.compile(r'\d+')

def extract_fast(text):
    return DIGIT_PATTERN.findall(text)

# 4. Choosing the Right Data Structure

import time
import random

all_customers = [f"CUST-{i}" for i in range(100_000)]
ordered = [f"CUST-{i}" for i in random.sample(range(100_000), 10_000)]

# Slow: ordered is a list
start = time.perf_counter()
repeat_customers = [c for c in all_customers if c in ordered]
print(f"List : {time.perf_counter() - start:.4f}s  →  {len(repeat_customers)} found")

# Fast: ordered is a set
ordered_set = set(ordered)
start = time.perf_counter()
repeat_customers = [c for c in all_customers if c in ordered_set]
print(f"Set  : {time.perf_counter() - start:.4f}s  →  {len(repeat_customers)} found")

# 5. Vectorizing Operations on Numeric Data

import time
import numpy as np
import pandas as pd

prices = [round(10 + i * 0.05, 2) for i in range(500_000)]
discount_rate = 0.15

# Slow: Python loop
start = time.perf_counter()
discounted = []
for price in prices:
    discounted.append(round(price * (1 - discount_rate), 2))
print(f"Python loop : {time.perf_counter() - start:.4f}s")

# Fast: NumPy vectorisation
prices_array = np.array(prices)
start = time.perf_counter()
discounted = np.round(prices_array * (1 - discount_rate), 2)
print(f"NumPy       : {time.perf_counter() - start:.4f}s")

# Fast: pandas vectorisation
prices_series = pd.Series(prices)
start = time.perf_counter()
discounted = (prices_series * (1 - discount_rate)).round(2)
print(f"Pandas      : {time.perf_counter() - start:.4f}s")

df = pd.DataFrame({"price": prices})

# Slow: row-by-row with iterrows
start = time.perf_counter()
for idx, row in df.iterrows():
    df.at[idx, "discounted"] = round(row["price"] * 0.85, 2)
print(f"iterrows : {time.perf_counter() - start:.4f}s")

# Fast: vectorised column operation
start = time.perf_counter()
df["discounted"] = (df["price"] * 0.85).round(2)
print(f"Vectorised : {time.perf_counter() - start:.4f}s")


