def clean_text(text):
    return text.strip().lower().replace(",", "").replace("$", "")

def parse_row(line):
    parts = line.strip().split(",")
    return {
        "name": parts[0],
        "city": parts[1],
        "role": parts[2],
        "salary": int(parts[3])
    }

with open("employees.txt") as file:
    rows = [parse_row(line) for line in file]

def average(values):
    return sum(values) / len(values) if values else 0

def count_by_key(data, key):
    counts = {}
    for item in data:
        k = item[key]
        counts[k] = counts.get(k, 0) + 1
    return counts
