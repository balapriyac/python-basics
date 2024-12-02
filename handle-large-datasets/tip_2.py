# useful tips that do not focus on a specific dataset
# We’ll use generic filenames like large_dataset.csv in the code examples

# Go Parallel with Multiprocessing
 
import pandas as pd
import numpy as np
from multiprocessing import Pool

# Function to clean and normalize data for each chunk
def clean_and_normalize(df_chunk):
    # Remove top 5% as outliers in the 'price' column
    df_chunk = df_chunk[df_chunk['price'] < df_chunk['price'].quantile(0.95)]
    
    # Normalize the 'price' column
    df_chunk['price'] = (df_chunk['price'] - df_chunk['price'].min()) / (df_chunk['price'].max() - df_chunk['price'].min())
    return df_chunk

# Function to read data in chunks and process it in parallel
def process_in_chunks(file_name, chunk_size):
    chunks = pd.read_csv(file_name, chunksize=chunk_size)
    
    with Pool(4) as pool:  # Adjust the number of processes for your CPU
        # Process each chunk in parallel and combine results
        cleaned_data = pd.concat(pool.map(clean_and_normalize, chunks))
    
    return cleaned_data

if __name__ == "__main__":
    cleaned_df = process_in_chunks('large_house_data.csv', chunk_size=100000)
    print(cleaned_df.head())
