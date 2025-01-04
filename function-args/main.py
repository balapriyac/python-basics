# Positional Arguments
def meet(name,job_title,city):
    return f"Meet {name}, a {job_title} from {city}."

meet1 = meet('James','Writer','Nashville')
print(meet1)

# Keyword Arguments
meet3 = meet(city='Madison',name='Ashley',job_title='Developer')
print(meet3)

# Variable Number of Positional Arguments
def reverse_strings(*strings):
    reversed_strs = []
    for string in strings:
        reversed_strs.append(string[::-1])
    return reversed_strs

rev_strs2 = reverse_strings('Coding','Is','Fun')
print(rev_strs2) # ['gnidoC', 'sI', 'nuF']

# Variable Number of Keyword Arguments
def running_sum(**nums):
    sum = 0
    for key,val in nums.items():
        sum+=val
    return sum

sum1 = running_sum(a=1,b=5,c=10)
print(sum1)

sum2 = running_sum(num1=7,num2=20)
print(sum2)
