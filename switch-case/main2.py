import random

# List of words to choose from
word_list = ["Python", "programming", "Hello", "world", "context", "Switch"]

# Randomly select a word from the list
word = random.choice(word_list)

# Provide context and available options to the user
print("Welcome! You have a randomly selected word.")
print("Choose an option to manipulate the word:")
print("1. Lowercase")
print("2. Uppercase")
print("3. Titlecase")
print("4. Swapcase")
print("5. Default behavior")

# Get user option
option = int(input("Enter your option: "))

# functions & dictionary mapping
# Define functions for each option
def lower_case(word):
    return word.lower()

def upper_case(word):
    return word.upper()

def title_case(word):
    return word.title()

def swap_case(word):
    return word.swapcase()

# Store functions in a dictionary
options = {
    1: lower_case,
    2: upper_case,
    3: title_case,
    4: swap_case,
}

# Use the dictionary to select and call the appropriate function
result = options.get(option, lambda x: x)(word)

print(f"Your random word is {word} and the result is {result}")
