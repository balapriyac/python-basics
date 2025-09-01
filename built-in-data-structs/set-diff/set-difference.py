fruits = {"apples","oranges","berries","cherries"}
to_eat = {"apples","cereals","berries","bread"}

print(fruits.difference(to_eat))
print(to_eat.difference(fruits))

print(fruits - to_eat)
print(to_eat - fruits)

set1 = {1,2,3,4,5}
list1 = [2,4,6]
list2 = [3,6,9]
list3 = [10,11]

print(set1.difference(list1,list2,list3))

# >>> set1 - (list1 + list2 + list3)
# Traceback (most recent call last):
#   File "", line 1, in 
# TypeError: unsupported operand type(s) for -: 'set' and 'list'

print(set1 - set(list1 + list2 + list3))
