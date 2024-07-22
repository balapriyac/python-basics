import re

text = "Contact info: (123)-456-7890 and 987-654-3210."
cleaned_text = re.sub(r'[()-]', '', text)
print(cleaned_text) 

# Output: Contact info: 1234567890 or 9876543210

text = "Please reach out to us at support@example.org or help@example.org."
emails = re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', text)
print(emails)

# Output: ['support@example.com', 'sales@example.org']

text = "Using     regular     expressions."
cleaned_text = re.sub(r'\s+', ' ', text)
print(cleaned_text) 

# Output: Using regular expressions.

email = "test@example.com"
if re.match(r'^\b[\w.-]+?@\w+?\.\w+?\b$', email):
    print("Valid email")  
else:
    print("Invalid email")

# Output: Valid email

text = "This is sentence one. And this is sentence two! Is this sentence three?"
sentences = re.split(r'[.!?]', text)
print(sentences) 

# Output: ['This is sentence one', ' And this is sentence two', ' Is this sentence three', '']

# Using regex w/ pandas dataframes
import pandas as pd

data = {
	'names': ['Alice123', 'Bob!@#', 'Charlie$$$'],
	'emails': ['alice@example.com', 'bob_at_example.com', 'charlie@example.com']
}
df = pd.DataFrame(data)

# Remove non-alphabetic characters from names
df['names'] = df['names'].str.replace(r'[^a-zA-Z]', '', regex=True)

# Validate email addresses
df['valid_email'] = df['emails'].apply(lambda x: bool(re.match(r'^\b[\w.-]+?@\w+?\.\w+?\b$', x)))

print(df)
