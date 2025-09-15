data = [
    {"name": "Alice", "city": "London"},
    {"name": "Bob", "city": "Paris"},
    {"name": "Eve", "city": "London"},
    {"name": "John", "city": "New York"},
    {"name": "Dana", "city": "Paris"},
]

city_counts = {}

for person in data:
    city = person["city"]
    if city not in city_counts:
        city_counts[city] = 1
    else:
        city_counts[city] += 1

print(city_counts)

salaries = [
    {"role": "Engineer", "salary": 75000},
    {"role": "Analyst", "salary": 62000},
    {"role": "Engineer", "salary": 80000},
    {"role": "Manager", "salary": 95000},
    {"role": "Analyst", "salary": 64000},
]

totals = {}
counts = {}

for person in salaries:
    role = person["role"]
    salary = person["salary"]
    
    totals[role] = totals.get(role, 0) + salary
    counts[role] = counts.get(role, 0) + 1

averages = {role: totals[role] / counts[role] for role in totals}

print(averages)
