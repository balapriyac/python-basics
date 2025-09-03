# 1. Reverse an Array in Place
nums = [90,23,19,45,33,54]
nums.reverse()
print(nums)

# Output >> [54, 33, 45, 19, 23, 90]

# 2. Sort Arrays and Customize Sorts
nums = [23,67,12,78,94,113,47]
nums.sort()
print(nums)

# Output >> [12, 23, 47, 67, 78, 94, 113]

nums.sort(reverse=True)
print(nums)

# Output >> [113, 94, 78, 67, 47, 23, 12]

nums.sort(key=lambda num:num%7)
print(nums)

# Output >> [113, 78, 23, 94, 67, 47, 12]

rem_list = [num%7 for num in nums]
print(rem_list)

# Output >> [1, 1, 2, 3, 4, 5, 5]

str_list = ["puppet","trumpet","carpet","reset"]
str_list.sort(key=lambda x:x.count('p'))
print(str_list)

# Output >> ['reset', 'trumpet', 'carpet', 'puppet']

# 3. List and Dictionary Comprehensions
nums = [15,12,90,27,10,34,26,77]
div_by_3 = [num for num in nums if num%3==0]
print(div_by_3)

# Output >> [15, 12, 90, 27]

squares_dict = {i:i**2 for i in range(1,11)}
print(squares_dict)

# Output >> 
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

strings = ["hello","coding","blue","work"]
str_len = {string:len(string) for string in strings}
print(str_len)

# Output >> {'hello': 5, 'coding': 6, 'blue': 4, 'work': 4}

# 4. Unpacking Iterables
list1 = [i*2 for i in range(4)]
num1, num2, num3, num4 = list1
num1, *num2 = list1
num1, *num2, num3 = list1

fruits = ["apples","grapes","berries","oranges","melons"]

print('--'.join(fruits))
# Output >> 'apples--grapes--berries--oranges--melons'

print(''.join(fruits))
# Output >> 'applesgrapesberriesorangesmelons'

print(' '.join(fruits))
# Output >> 'apples grapes berries oranges melons'

# 6. Loop Using enumerate()
fruits = ["apples","grapes","berries","oranges","melons"]

for idx,fruit in enumerate(fruits):
    print(f"At index {idx}: {fruit}")


# Output >>
# At index 0: apples
# At index 1: grapes
# At index 2: berries
# At index 3: oranges
# At index 4: melons

for idx,fruit in enumerate(fruits,1):
    print(f"At index {idx}: {fruit}")

# Output >>
# At index 1: apples
# At index 2: grapes
# At index 3: berries
# At index 4: oranges
# At index 5: melons

idx_dict = {idx:fruit for idx,fruit in enumerate(fruits)}
print(idx_dict)

# Output >> {0: 'apples', 1: 'grapes', 2: 'berries', 3: 'oranges', 4: 'melons'}

# 7. Useful Math Functions to Know
import math
num1 = 2.47
print(math.ceil(num1))
# Output >> 3

num2 = 3.97
print(math.floor(num2))
# Output >> 3

sqrt_nums = [math.sqrt(num) for num in range(1,11)]
print(sqrt_nums)

# Output >> [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795]

sqrt_nums = [round(math.sqrt(num),2) for num in range(1,11)]
print(sqrt_nums)

# Output >> [1.0, 1.41, 1.73, 2.0, 2.24, 2.45, 2.65, 2.83, 3.0, 3.16]
