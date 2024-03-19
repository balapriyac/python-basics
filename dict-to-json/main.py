# Python dict to JSON
import json

books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication_year": 1925,
        "genre": "Fiction"
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publication_year": 1960,
        "genre": "Fiction"
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "publication_year": 1949,
        "genre": "Fiction"
    }
]

# Convert dictionary to JSON string
json_string = json.dumps(books, indent=4)
print(json_string)
