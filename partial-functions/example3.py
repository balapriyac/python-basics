from functools import partial

# Function to scale a value
def scale_data(value, factor):
    return value * factor

# Create partial functions for specific scaling factors
scale_by_2 = partial(scale_data, factor=2)
scale_by_10 = partial(scale_data, factor=10)

data = [1, 2, 3, 4, 5]
scaled_by_2 = list(map(scale_by_2, data))   # Scales by 2
scaled_by_10 = list(map(scale_by_10, data))  # Scales by 10

print(scaled_by_2)  
print(scaled_by_10) 
