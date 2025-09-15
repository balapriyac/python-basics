titles = [
    "  Data Scientist\n",
    "data scientist",
    "Senior Data Scientist ",
    "DATA scientist",
    "Data engineer",
    "Data Scientist"
]

cleaned = [title.strip().lower() for title in titles]
print(cleaned)

standardized = []

for title in cleaned:
    if "data scientist" in title:
        standardized.append("data scientist")
    else:
        standardized.append(title)

text = " The price is $5,000!  "

# Clean up
clean = text.strip().lower().replace("$", "").replace(",", "").replace("!", "")
print(clean)  

email = "  Alice.Johnson@Example.com  "
email = email.strip().lower()

username, domain = email.split("@")

print(f"User: {username}, Domain: {domain}")

comment = "I'm learning Python and SQL for data jobs."

if "python" in comment.lower():
    print("Mentioned Python")

# Word count
word_count = len(clean.split())

# Contains digit
has_number = any(char.isdigit() for char in clean)

print(word_count)
print(has_number)
