# Positional Arguments
def meet(name,job_title,city):
    return f"Meet {name}, a {job_title} from {city}."

meet1 = meet('James','Writer','Nashville')
print(meet1)

# Keyword Arguments
meet3 = meet(city='Madison',name='Ashley',job_title='Developer')
print(meet3)
