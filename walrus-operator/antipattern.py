# Function to compute profit
def compute_profit(sales, cost):
    return sales - cost

# Messy list comprehension with nested walrus operator
sales_data = [(100, 70), (200, 150), (150, 100), (300, 200)]
results = [
	(sales, cost, profit, sales_ratio)
	for sales, cost in sales_data
	if (profit := compute_profit(sales, cost)) > 50
	if (sales_ratio := sales / cost) > 1.5
	if (profit_margin := (profit / sales)) > 0.2
]

# Example of nested walrus operators 
values = [5, 15, 25, 35, 45]
threshold = 20
results = []

for value in values:
    if (above_threshold := value > threshold) and (incremented := (new_value := value + 10) > 30):
        results.append(new_value)

print(results)
