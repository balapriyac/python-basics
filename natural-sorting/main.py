import natsort

# List of filenames
filenames = ["file10.txt", "file2.txt", "file1.txt"]

# Sort filenames naturally
sorted_filenames = natsort.natsorted(filenames)

print(sorted_filenames)

# List of version numbers
versions = ["v-1.10", "v-1.2", "v-1.5"]

# Sort versions naturally
sorted_versions = natsort.natsorted(versions)

print(sorted_versions)

# customize sorting w/ a key
# List of tuples containing filename and size
file_data = [
	("data_20230101_080000.csv", 100),
	("data_20221231_235959.csv", 150),
	("data_20230201_120000.csv", 120),
	("data_20230115_093000.csv", 80)
]

# Sort file data based on file size 
sorted_file_data = natsort.natsorted(file_data, key=lambda x:x[1])

# Print sorted file data
for filename, size in sorted_file_data:
	print(filename, size)

# Case-insensitive sorting
# List of strings with mixed case
words = ["apple", "Banana", "cat", "Dog", "Elephant"]

# Sort words naturally with case-insensitivity
sorted_words = natsort.natsorted(words, alg=natsort.ns.IGNORECASE)

print(sorted_words)
