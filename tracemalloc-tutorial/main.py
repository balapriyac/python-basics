# main.py
import pandas as pd

def load_data(file_path):
    print("Loading data...")
    df = pd.read_csv(file_path)
    return df

def process_data(df):
    print("Processing data...")
    df['DiscountedAmount'] = df['OrderAmount'] * 0.9  # Apply a 10% discount
    df['OrderYear'] = pd.to_datetime(df['OrderDate']).dt.year  # Extract the order year
    return df
