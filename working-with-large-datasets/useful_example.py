import pandas as pd

chunk_size = 200000
product_revenue = {}

# Read in chunks, using only needed columns
for chunk in pd.read_csv('orders.csv', 
                         chunksize=chunk_size,
                         usecols=['product_id', 'quantity', 'price']):
    
    # Calculate revenue for each row
    chunk['revenue'] = chunk['quantity'] * chunk['price']
    
    # Aggregate by product
    chunk_summary = chunk.groupby('product_id')['revenue'].sum()
    
    # Add to our running totals
    for product_id, revenue in chunk_summary.items():
        product_revenue[product_id] = product_revenue.get(product_id, 0) + revenue

# Convert to dataframe and get top 10
result = pd.DataFrame(list(product_revenue.items()), 
                     columns=['product_id', 'revenue'])
top_10 = result.nlargest(10, 'revenue')

print(top_10)
