# useful tips and does not focus on a specific dataset
# We’ll use generic filenames like large_dataset.csv in the code examples

# Use Generators Instead of Lists

def read_large_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line 

