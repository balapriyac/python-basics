from functools import partial

# Original function to compute power
def power(base, exponent):
    return base ** exponent

# Create a partial function that always squares the base
square = partial(power, exponent=2)

print(square(5))  
print(square(9))
