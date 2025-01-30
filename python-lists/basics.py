shopping_list = ['apples','pens','oatmeal  cookies','notepad','brushes','paint']

shopping_list[2] = 'candy'
print(shopping_list)

for item in shopping_list:
  print(item)

print(shopping_list[2:])
# Output: ['candy', 'notepad', 'brushes', 'paint']

print(shopping_list[:2])
# Output: ['apples', 'pens']

print(shopping_list[:])
# Output: ['apples', 'pens', 'candy', 'notepad', 'brushes', 'paint']

print(len(shopping_list))
# 6

print(max(shopping_list))
# pens

print(min(shopping_list))
# apples

# list methods
shopping_list.append('grapes')
print(shopping_list)

shopping_list.extend(['protein bars','cheese'])
print(shopping_list)

last_element = shopping_list.pop()
print(shopping_list)
print(last_element)

not_needed = shopping_list.pop(2)
print(not_needed)

del shopping_list[1]
print(shopping_list)

shopping_list.sort()
print(shopping_list)

list_2 = shopping_list + ['noodles','almonds']
print(list_2)
