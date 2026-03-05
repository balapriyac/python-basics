# install pyarrow: !pip install pyarrow

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Create a product inventory dataset
data = {
    'product_id': [1001, 1002, 1003, 1004, 1005],
    'product_name': ['Wireless Mouse', 'Mechanical Keyboard', 'USB-C Hub', 'Monitor Stand', 'Webcam HD'],
    'category': ['Peripherals', 'Peripherals', 'Accessories', 'Accessories', 'Peripherals'],
    'price': [29.99, 89.99, 49.99, 34.99, 74.99],
    'stock': [150, 80, 200, 95, 60]
}

df = pd.DataFrame(data)

# Convert to PyArrow Table and write as Parquet
table = pa.Table.from_pandas(df)
pq.write_table(table, 'inventory.parquet')

print("Parquet file created successfully!")

# Read the Parquet file
table = pq.read_table('inventory.parquet')

# Convert to pandas for easy viewing
df_read = table.to_pandas()

print(df_read)
print(f"\nData types:\n{df_read.dtypes}")

# Read only product name and price
table_subset = pq.read_table('inventory.parquet', columns=['product_name', 'price'])
df_subset = table_subset.to_pandas()

print(df_subset)

import os

# Generate a larger dataset
large_data = {
    'transaction_id': range(50000),
    'store': ['Downtown', 'Uptown', 'Suburban', 'Airport', 'Mall'] * 10000,
    'product': [f'product_{i % 200}' for i in range(50000)],
    'amount': [round(10 + (i % 500) * 0.5, 2) for i in range(50000)]
}

df_large = pd.DataFrame(large_data)
table_large = pa.Table.from_pandas(df_large)

# Write with different compression codecs
for codec in ['NONE', 'SNAPPY', 'GZIP', 'ZSTD']:
    path = f'transactions_{codec.lower()}.parquet'
    pq.write_table(table_large, path, compression=codec)
    size = os.path.getsize(path)
    print(f"{codec:<8}: {size:>10,} bytes")

# Write with smaller row groups (useful for filtering large files)
pq.write_table(
    table_large,
    'transactions_grouped.parquet',
    compression='ZSTD',
    row_group_size=10000
)

# Use PyArrow's dataset API for efficient filtering
import pyarrow.dataset as ds

dataset = ds.dataset('transactions_grouped.parquet', format='parquet')

# Filter: only transactions from the Downtown store over $150
filtered = dataset.to_table(
    filter=(ds.field('store') == 'Downtown') & (ds.field('amount') > 150)
)

df_filtered = filtered.to_pandas()
print(f"Matching transactions: {len(df_filtered)}")
print(df_filtered.head())

from datetime import datetime, timedelta
import random

# Simulate 30 days of sales data
regions = ['North', 'South', 'East', 'West']
products = ['Laptop', 'Tablet', 'Headphones', 'Charger', 'Case']

records = []
start = datetime(2025, 1, 1)

for day in range(30):
    date = start + timedelta(days=day)
    for _ in range(200):
        records.append({
            'date': date.strftime('%Y-%m-%d'),
            'region': random.choice(regions),
            'product': random.choice(products),
            'units_sold': random.randint(1, 20),
            'revenue': round(random.uniform(50, 2000), 2)
        })

df_sales = pd.DataFrame(records)
table_sales = pa.Table.from_pandas(df_sales)

# Save as compressed Parquet
pq.write_table(table_sales, 'sales_jan2025.parquet', compression='ZSTD')
print(f"Saved {len(df_sales):,} records to Parquet")

# Query: total revenue by region for the first two weeks
dataset = ds.dataset('sales_jan2025.parquet', format='parquet')

first_two_weeks = dataset.to_table(
    columns=['region', 'revenue', 'date'],
    filter=ds.field('date') <= '2025-01-14'
).to_pandas()

summary = first_two_weeks.groupby('region')['revenue'].sum().sort_values(ascending=False)
print(f"\nRevenue by region (Jan 1–14):")
print(summary.round(2))
