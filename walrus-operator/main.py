# Example 1
# Without walrus operator
data = input("Enter your data: ")
while len(data) > 0:
    print("You entered:", data)
    data = input("Enter your data: ")

# With walrus operator
while (data := input("Enter your data: ")) != "":
    print("You entered:", data)

# Example 2
# Without Walrus Operator
# Function to compute profit
def compute_profit(sales, cost):
	return sales - cost

sales_data = [(100, 70), (200, 150), (150, 100), (300, 200)]
profits = []
for sales, cost in sales_data:
    profit = compute_profit(sales, cost)
    if profit > 50:
        profits.append(profit)

# With Walrus Operator
# Function to compute profit
def compute_profit(sales, cost):
	return sales - cost

sales_data = [(100, 70), (200, 150), (150, 100), (300, 200)]
profits = [profit for sales, cost in sales_data if (profit := compute_profit(sales, cost)) > 50]
