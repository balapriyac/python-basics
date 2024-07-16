# Prefer list comprehensions over loops
data = [{'name': 'Alice', 'age': 25, 'score': 90},
    	{'name': 'Bob', 'age': 30, 'score': 85},
    	{'name': 'Charlie', 'age': 22, 'score': 95}]

# Using a loop
result = []
for row in data:
    if row['score'] > 85:
        result.append(row['name'])

print(result)

# Using a list comprehension
result = [row['name'] for row in data if row['score'] > 85]

# Generator function to read and process a CSV file
import csv
from typing import Generator, Dict

def read_large_csv_with_generator(file_path: str) -> Generator[Dict[str, str], None, None]:
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row

# Path to a sample CSV file
file_path = 'large_data.csv'

for row in read_large_csv_with_generator(file_path):
    print(row)
