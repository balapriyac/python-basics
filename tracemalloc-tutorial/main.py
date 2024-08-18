# main.py
import pandas as pd
import tracemalloc

def load_data(file_path):
    print("Loading data...")
    df = pd.read_csv(file_path)
    return df

def process_data(df):
    print("Processing data...")
    df['DiscountedAmount'] = df['OrderAmount'] * 0.9  # Apply a 10% discount
    df['OrderYear'] = pd.to_datetime(df['OrderDate']).dt.year  # Extract the order year
    return df

def main():
    # Start tracing memory allocations
    tracemalloc.start()

    # Load data
    df = load_data('order_data.csv')

    # Take a snapshot
    snapshot1 = tracemalloc.take_snapshot()

    # Process data
    df = process_data(df)

    # Take another snapshot
    snapshot2 = tracemalloc.take_snapshot()

    # Compare snapshots
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')

    print("[ Top memory-consuming lines ]")
    for stat in top_stats[:10]:
        print(stat)

    # Current and peak memory usage
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024 / 1024:.1f} MB")
    print(f"Peak usage: {peak / 1024 / 1024:.1f} MB")

    tracemalloc.stop()

if __name__ == "__main__":
    main()
