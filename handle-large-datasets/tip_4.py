# useful tips that do not focus on a specific dataset
# We’ll use generic filenames like large_dataset.csv in the code examples

# Use Dask for Parallel Computing

import dask.dataframe as dd

# Load data into a Dask DataFrame
df = dd.read_csv('large_sales_data.csv')

# Group by 'category' and calculate mean sales (executed in parallel)
mean_sales = df.groupby('category')['sales'].mean().compute()

print(mean_sales)
