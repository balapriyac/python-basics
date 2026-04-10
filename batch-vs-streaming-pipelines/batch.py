import pandas as pd
from datetime import datetime, timedelta


def extract(filepath: str) -> pd.DataFrame:
    """Load raw orders from a daily export file."""
    df = pd.read_csv(filepath, parse_dates=["order_timestamp"])
    return df


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and aggregate orders into daily revenue by region."""
    # Filter to completed orders only
    df = df[df["status"] == "completed"].copy()

    # Extract date from timestamp for grouping
    df["order_date"] = df["order_timestamp"].dt.date

    # Aggregate: total revenue and order count per region per day
    summary = (
        df.groupby(["order_date", "region"])
        .agg(
            total_revenue=("order_value_gbp", "sum"),
            order_count=("order_id", "count"),
            avg_order_value=("order_value_gbp", "mean"),
        )
        .reset_index()
    )
    return summary


def load(df: pd.DataFrame, output_path: str) -> None:
    """Write the aggregated result to the warehouse (here, a CSV)."""
    df.to_csv(output_path, index=False)
    print(f"Loaded {len(df)} rows to {output_path}")


if __name__ == "__main__":
    raw = extract("orders_2024_06_01.csv")
    aggregated = transform(raw)
    load(aggregated, "warehouse/daily_revenue_2024_06_01.csv")

