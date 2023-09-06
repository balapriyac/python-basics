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

# if-elif-else
# if-elif-else 

if option == 1:
    result = word.lower()
elif option == 2:
    result = word.upper()
elif option == 3:
    result = word.title()
elif option == 4:
    result = word.swapcase()
else:
    result = word

print(f"Your random word is {word} and the result is {result}")
