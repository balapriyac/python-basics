my_tuple = ([1,2],3,4)
my_tuple[0].append(3) # works fine!
print(my_tuple) 

# now this is where things get interesting...
my_tuple[0] += [4,5]
