
!pip install pyarrow pandas

import pandas as pd
import pyarrow as pa
import pyarrow.orc as orc

# Create sample employee data
data = {
    'employee_id': [101, 102, 103, 104, 105],
    'name': ['Alice Johnson', 'Bob Smith', 'Carol White', 'David Brown', 'Eve Davis'],
    'department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales'],
    'salary': [95000, 65000, 88000, 72000, 71000],
    'years_experience': [5, 3, 7, 4, 3]
}

df = pd.DataFrame(data)

# Convert to PyArrow Table and write as ORC
table = pa.Table.from_pandas(df)
orc.write_table(table, 'employees.orc')

print("ORC file created successfully!")

# Read ORC file
table = orc.read_table('employees.orc')

# Convert to pandas DataFrame for easier viewing
df_read = table.to_pandas()

print(df_read)
print(f"\nData types:\n{df_read.dtypes}")

# Read only specific columns
table_subset = orc.read_table('employees.orc', columns=['name', 'salary'])
df_subset = table_subset.to_pandas()

print(df_subset)

# Create a larger dataset
large_data = {
    'id': range(10000),
    'value': [f"data_{i}" for i in range(10000)],
    'category': ['A', 'B', 'C', 'D'] * 2500
}

df_large = pd.DataFrame(large_data)
table_large = pa.Table.from_pandas(df_large)

# Write with ZLIB compression (default)
orc.write_table(table_large, 'data_zlib.orc', compression='ZLIB')

# Write with SNAPPY compression (faster but less compression)
orc.write_table(table_large, 'data_snappy.orc', compression='SNAPPY')

# Write with ZSTD compression (good balance)
orc.write_table(table_large, 'data_zstd.orc', compression='ZSTD')

import os
print(f"ZLIB size: {os.path.getsize('data_zlib.orc'):,} bytes")
print(f"SNAPPY size: {os.path.getsize('data_snappy.orc'):,} bytes")
print(f"ZSTD size: {os.path.getsize('data_zstd.orc'):,} bytes")

# Create data with complex types
complex_data = {
    'user_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Carol'],
    'purchases': [
        ['laptop', 'mouse'],
        ['keyboard'],
        ['monitor', 'cable', 'stand']
    ],
    'ratings': [
        [4.5, 5.0],
        [3.5],
        [4.0, 4.5, 5.0]
    ]
}

df_complex = pd.DataFrame(complex_data)
table_complex = pa.Table.from_pandas(df_complex)
orc.write_table(table_complex, 'complex_data.orc')

# Read it back
table_read = orc.read_table('complex_data.orc')
df_read = table_read.to_pandas()

print(df_read)
print(f"\nType of 'purchases' column: {type(df_read['purchases'][0])}")

from datetime import datetime, timedelta
import random

# Generate sample log data
log_data = []
start_date = datetime(2025, 1, 1)

for i in range(1000):
    log_data.append({
        'timestamp': start_date + timedelta(minutes=i),
        'user_id': random.randint(1000, 9999),
        'endpoint': random.choice(['/api/users', '/api/products', '/api/orders']),
        'status_code': random.choice([200, 200, 200, 404, 500]),
        'response_time_ms': random.randint(50, 2000)
    })

df_logs = pd.DataFrame(log_data)

# Write logs to ORC
table_logs = pa.Table.from_pandas(df_logs)
orc.write_table(table_logs, 'server_logs.orc', compression='ZSTD')

# Later, query only failed requests
table_subset = orc.read_table('server_logs.orc')
df_subset = table_subset.to_pandas()

# Filter for errors
errors = df_subset[df_subset['status_code'] >= 400]
print(f"Total errors: {len(errors)}")
print(f"\nError breakdown:\n{errors['status_code'].value_counts()}")
print(f"\nSlowest error response: {errors['response_time_ms'].max()}ms")


