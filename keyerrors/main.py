books = {
	"1984": "George Orwell",
	"To Kill a Mockingbird": "Harper Lee",
	"The Great Gatsby": "F. Scott Fitzgerald"
}


# handle KeyError explicitly
try:
    # Try to access the key "Brave New World"
	author = books["Brave New World"]  
    # Catch the KeyError if the key does not exist
except KeyError:  
	author = "Book not found"  

print(author) 

# Try to get the value for "Brave New World"
author = books.get("Brave New World", "Book not found")  
print(author) 


# use defaultdict to handle missing keys natively
from collections import defaultdict

books_default = defaultdict(lambda: "Book not found",books)  
# Access the key "Brave New World"
author = books_default["Brave New World"]  
print(author) 
