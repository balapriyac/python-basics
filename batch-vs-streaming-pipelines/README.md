# Batch vs Streaming Pipelines — Code Examples

Code examples from the article [Efficient Data Processing in Python: Batch vs Streaming Pipelines Explained](https://www.freecodecamp.org/news/efficient-data-processing-in-python-batch-vs-streaming-pipelines/).

## Files

- `batch_pipeline.py` — ETL pipeline that reads a daily order CSV, aggregates revenue by region, and writes to a destination file
- `streaming_pipeline.py` — Generator-based pipeline that validates and enriches order events one at a time as they arrive

## Requirements

```
pandas
```

## Usage

**Batch:**
```bash
python batch_pipeline.py
```
Expects `orders_2024_06_01.csv` with columns: `order_id`, `order_timestamp`, `status`, `region`, `order_value_gbp`.

**Streaming:**
```bash
python streaming_pipeline.py
```
Expects `order_events.jsonl` — one JSON object per line with fields: `order_id`, `customer_id`, `order_value_gbp`, `region`.
