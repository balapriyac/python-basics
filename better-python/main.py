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

# Caching
from functools import cache
from typing import Tuple
import numpy as np

@cache
def euclidean_distance(pt1: Tuple[float, float], pt2: Tuple[float, float]) -> float:
    return np.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

def assign_clusters(data: np.ndarray, centroids: np.ndarray) -> np.ndarray:
    clusters = np.zeros(data.shape[0])
    for i, point in enumerate(data):
        distances = [euclidean_distance(tuple(point), tuple(centroid)) for centroid in centroids]
        clusters[i] = np.argmin(distances)
    return clusters

# Context managers
import sqlite3

def query_db(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        for row in cursor.fetchall():
            yield row
