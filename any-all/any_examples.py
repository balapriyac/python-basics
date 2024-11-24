list_1 = [0,0,0,1,0,0,0,0]
# any(a list with at least one non-zero entry) returns True
print(any(list_1))
# Output True

list_2 = [0j,0,0,0.0,0,0,0.0,0]
# any(a list of zeros) returns False
print(any(list_2))
# Output False

list_3 = [True, False, False]
# any(a list with at least one True value) returns True
print(any(list_3))
# Output True

list_4 = ["","","code more"]
# any(a list with at least one non-empty string) returns True
print(any(list_4))
# Output True

list_5 = ["","",""]
# any(a list of empty strings) returns False
print(any(list_5))
# Output False

my_string = "coding**is**cool**345"
are_there_digits = [char.isdigit() for char in my_string]
print(any(are_there_digits))

# Output True

my_string = "***456278)))"
num = [char.isalpha() for char in my_string]
print(any(num))

# Output False
