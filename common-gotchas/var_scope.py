# loops
x = 10
squares = []
for x in range(5):
    squares.append(x ** 2)

print("Squares list:", squares)  

# x is accessible here and is the last value of the looping var
print("x after for loop:", x) 

# list comp
x = 10
squares = [x ** 2 for x in range(5)]

print("Squares list:", squares)  

# x is 10 here
print("x after list comprehension:", x)
