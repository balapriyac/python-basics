import copy


# shallow copy
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Shallow copy of the original list
shallow_copy = original_list

# Modify the shallow copy
shallow_copy[0][0] = 100

# Print both the lists
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)


# deep copy
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Deep copy of the original list
deep_copy = copy.deepcopy(original_list)

# Modify an element of the deep copy
deep_copy[0][0] = 100

# Print both lists
print("Original List:", original_list)
print("Deep Copy:", deep_copy)
