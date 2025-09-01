books = {'Fluent Python':50,
         'Learning Python':58}

more_books = {'Effective Python':40,
              'Think Python':29}

for book in more_books.keys():
    books[book] = more_books[book]
print(books)

for book, price in more_books.items():
    books[book] = price
print(books)

# Update a Python Dictionary Using update()
books.update(more_books)
print(books)

some_more_books = [('Python Cookbook',33),('Python Crash Course',41)]
books.update(some_more_books)
print(books)

# Updating a Dictionary in the Presence of Repeating Keys
and_some_more = [('Fluent Python',45),('Python for Everybody',30)]
books.update(and_some_more)
print(books)
