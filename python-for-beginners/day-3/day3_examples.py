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

# Word count
word_count = len(clean.split())

# Contains digit
has_number = any(char.isdigit() for char in clean)

print(word_count)
print(has_number)
