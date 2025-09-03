nums = [90,23,19,45,33,54]
nums.reverse()
print(nums)

# Output >> [54, 33, 45, 19, 23, 90]

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
