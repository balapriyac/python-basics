"""
Sample Data Generator for Large Dataset Tutorial
Run this script to create the sample CSV files used in the tutorial examples.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

print("Starting data generation...\n")

# ============================================================================
# 1. Generate large_sales_data.csv (for chunking example)
# ============================================================================
print("1. Creating large_sales_data.csv...")

num_rows = 1_000_000  # 1 million rows
np.random.seed(42)

sales_data = {
    'transaction_id': range(1, num_rows + 1),
    'date': [datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365)) 
             for _ in range(num_rows)],
    'revenue': np.random.uniform(10, 1000, num_rows).round(2),
    'product_id': np.random.randint(1, 1000, num_rows),
    'region': np.random.choice(['North', 'South', 'East', 'West'], num_rows)
}

df_sales = pd.DataFrame(sales_data)
df_sales.to_csv('large_sales_data.csv', index=False)
print(f"   ✓ Created with {num_rows:,} rows ({df_sales.memory_usage(deep=True).sum() / 1024**2:.1f} MB)")

# ============================================================================
# 2. Generate customers.csv (for column selection example)
# ============================================================================
print("2. Creating customers.csv...")

num_customers = 500_000
np.random.seed(42)

# Create lots of columns (but we'll only use a few in the tutorial)
customers_data = {
    'customer_id': range(1, num_customers + 1),
    'age': np.random.randint(18, 80, num_customers),
    'purchase_amount': np.random.uniform(5, 500, num_customers).round(2),
    'first_name': [f'User{i}' for i in range(num_customers)],
    'last_name': [f'Lastname{i}' for i in range(num_customers)],
    'email': [f'user{i}@example.com' for i in range(num_customers)],
    'phone': [f'555-{random.randint(1000, 9999)}' for _ in range(num_customers)],
    'address': [f'{random.randint(1, 9999)} Main St' for _ in range(num_customers)],
    'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston'], num_customers),
    'state': np.random.choice(['NY', 'CA', 'IL', 'TX'], num_customers),
    'zip_code': [f'{random.randint(10000, 99999)}' for _ in range(num_customers)],
}

df_customers = pd.DataFrame(customers_data)
df_customers.to_csv('customers.csv', index=False)
print(f"   ✓ Created with {num_customers:,} rows and {len(customers_data)} columns")

# ============================================================================
# 3. Generate ratings.csv (for data type optimization)
# ============================================================================
print("3. Creating ratings.csv...")

num_ratings = 2_000_000
np.random.seed(42)

ratings_data = {
    'user_id': np.random.randint(1, 100000, num_ratings),
    'product_id': np.random.randint(1, 10000, num_ratings),
    'rating': np.random.randint(1, 6, num_ratings),  # 1-5 stars
    'timestamp': [datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365)) 
                  for _ in range(num_ratings)]
}

df_ratings = pd.DataFrame(ratings_data)
df_ratings.to_csv('ratings.csv', index=False)
print(f"   ✓ Created with {num_ratings:,} rows")

# ============================================================================
# 4. Generate products.csv (for categorical data example)
# ============================================================================
print("4. Creating products.csv...")

num_products = 5_000_000
np.random.seed(42)

# Only 20 unique categories to demonstrate categorical efficiency
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books',
              'Toys', 'Food', 'Beauty', 'Automotive', 'Health',
              'Office', 'Pet Supplies', 'Baby', 'Jewelry', 'Tools',
              'Music', 'Movies', 'Games', 'Crafts', 'Outdoor']

products_data = {
    'product_id': range(1, num_products + 1),
    'category': np.random.choice(categories, num_products),
    'price': np.random.uniform(5, 500, num_products).round(2),
    'stock': np.random.randint(0, 1000, num_products)
}

df_products = pd.DataFrame(products_data)
df_products.to_csv('products.csv', index=False)
print(f"   ✓ Created with {num_products:,} rows")

# ============================================================================
# 5. Generate transactions.csv (for filtering example)
# ============================================================================
print("5. Creating transactions.csv...")

num_transactions = 3_000_000
np.random.seed(42)

# Mix of years 2022-2024
transactions_data = {
    'transaction_id': range(1, num_transactions + 1),
    'year': np.random.choice([2022, 2023, 2024], num_transactions, p=[0.3, 0.3, 0.4]),
    'customer_id': np.random.randint(1, 100000, num_transactions),
    'amount': np.random.uniform(10, 1000, num_transactions).round(2),
    'product_id': np.random.randint(1, 10000, num_transactions)
}

df_transactions = pd.DataFrame(transactions_data)
df_transactions.to_csv('transactions.csv', index=False)
print(f"   ✓ Created with {num_transactions:,} rows")

# ============================================================================
# 6. Generate orders.csv (for the practical example)
# ============================================================================
print("6. Creating orders.csv...")

num_orders = 2_500_000
np.random.seed(42)

orders_data = {
    'order_id': range(1, num_orders + 1),
    'product_id': np.random.randint(1, 5000, num_orders),
    'quantity': np.random.randint(1, 10, num_orders),
    'price': np.random.uniform(10, 500, num_orders).round(2),
    'customer_id': np.random.randint(1, 100000, num_orders),
    'order_date': [datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365)) 
                   for _ in range(num_orders)]
}

df_orders = pd.DataFrame(orders_data)
df_orders.to_csv('orders.csv', index=False)
print(f"   ✓ Created with {num_orders:,} rows")

# ============================================================================
# Summary
# ============================================================================
print("\n" + "="*60)
print("DATA GENERATION COMPLETE!")
print("="*60)

files_created = [
    'large_sales_data.csv',
    'customers.csv',
    'ratings.csv',
    'products.csv',
    'transactions.csv',
    'orders.csv'
]

total_size = 0
for filename in files_created:
    import os
    if os.path.exists(filename):
        size_mb = os.path.getsize(filename) / 1024**2
        total_size += size_mb
        print(f"✓ {filename:<30} {size_mb:>8.1f} MB")

print("="*60)
print(f"Total size: {total_size:.1f} MB")
