from functools import partial

# Use lambda with partial to create a custom scaling function
scale = partial(lambda x, factor: x * factor, factor=3)

# Apply the partial function to a list of numbers
scaled_values = [scale(i) for i in range(1, 6)]
print(scaled_values) 
