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
