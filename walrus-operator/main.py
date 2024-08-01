# example 1
# without walrus operator
data = input("Enter your data: ")
while len(data) > 0:
    print("You entered:", data)
    data = input("Enter your data: ")

# with walrus operator
while (data := input("Enter your data: ")) != "":
    print("You entered:", data)

