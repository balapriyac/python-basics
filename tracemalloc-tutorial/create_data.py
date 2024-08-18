# create_data.py
import pandas as pd
import numpy as np

# Create a sample dataset with order details
num_orders = 100000
data = {
	'OrderID': np.arange(1, num_orders + 1),
	'CustomerID': np.random.randint(1000, 5000, num_orders),
	'OrderAmount': np.random.uniform(10.0, 1000.0, num_orders).round(2),
	'OrderDate': pd.date_range(start='2023-01-01', periods=num_orders, freq='min')
}

df = pd.DataFrame(data)
df.to_csv('order_data.csv', index=False)
