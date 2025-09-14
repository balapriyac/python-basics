with open("scores.txt", "r") as file:
    scores = [float(line.strip()) for line in file]

print(scores)

average = sum(scores) / len(scores)
print(f"Average score: {average:.2f}")


with open("people.txt", "r") as file:
    records = []
    for line in file:
        name, age = line.strip().split(",")
        records.append((name.strip(), int(age.strip())))

for person in records:
    name, age = person
    if age > 30:
        print(f"{name} is over 30.")

people = []

with open("people.txt", "r") as file:
    for line in file:
        name, age = line.strip().split(",")
        person = {
            "name": name.strip(),
            "age": int(age.strip())
        }
        people.append(person)

for person in people:
    if person["age"] < 60:
        print(f"{person['name']} is perhaps a working professional.")

domains = set()

with open("emails.txt", "r") as file:
    for line in file:
        email = line.strip().lower()
        if "@" in email:
            domain = email.split("@")[1]
            domains.add(domain)

print(domains) 

