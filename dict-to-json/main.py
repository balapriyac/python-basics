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


# Nested dict to JSON
books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication_year": 1925,
        "genre": "Fiction",
        "reviews": [
            {"user": "Alice", "rating": 4, "comment": "Captivating story"},
            {"user": "Bob", "rating": 5, "comment": "Enjoyed it!"}
        ]
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publication_year": 1960,
        "genre": "Fiction",
        "reviews": [
            {"user": "Charlie", "rating": 5, "comment": "A great read!"},
            {"user": "David", "rating": 4, "comment": "Engaging narrative"}
        ]
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "publication_year": 1949,
        "genre": "Fiction",
        "reviews": [
            {"user": "Emma", "rating": 5, "comment": "Orwell pulls it off well!"},
            {"user": "Frank", "rating": 4, "comment": "Dystopian masterpiece"}
        ]
    }
]

# Convert dictionary to JSON string
json_string = json.dumps(books, indent=4)
print(json_string)
