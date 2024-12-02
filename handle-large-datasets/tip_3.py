# useful tips that do not focus on a specific dataset
# We’ll use generic filenames like large_dataset.csv in the code examples

# Use Pandas' chunksize for Chunked Processing

import pandas as pd

total_sales = 0
chunk_size = 100000  # Define chunk size to read data in batches

# Load data in chunks and process each chunk
for chunk in pd.read_csv('large_sales_data.csv', chunksize=chunk_size):
    total_sales += chunk['sales'].sum()  # Summing up sales column in each chunk

print(f"Total Sales: {total_sales}")
