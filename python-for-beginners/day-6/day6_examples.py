try:
    with open("employees.txt") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Error: File not found.")
    lines = []

records = []

for line in lines:
    try:
        parts = line.strip().split(",")
        if len(parts) != 4:
            raise ValueError("Incorrect number of fields")
        record = {
            "name": parts[0],
            "city": parts[1],
            "role": parts[2],
            "salary": int(parts[3])
        }
        records.append(record)
    except Exception as e:
        print(f"Skipping bad line: {line.strip()} ({e})")

with open("cleaned_employees.txt", "w") as out:
    for r in records:
        out.write(f"{r['name']},{r['city']},{r['role']},{r['salary']}\n")
