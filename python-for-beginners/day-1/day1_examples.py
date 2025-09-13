filename = "responses.txt"
survey_name = "Q3 Customer Feedback"
max_entries = 100

with open("responses.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    cleaned = line.strip()  # removes \n and spaces
    print(f"{i + 1}: {cleaned}")

with open("responses.txt", "r") as infile:
    lines = infile.readlines()

yes_responses = []

for line in lines:
    if line.strip().lower() == "yes":
        yes_responses.append(line.strip())

with open("yes_only.txt", "w") as outfile:
    for item in yes_responses:
        outfile.write(item + "\n")
