import json
import time
from typing import Generator, Dict


def event_source(filepath: str) -> Generator[Dict, None, None]:
    """
    Simulate a stream of order events from a file.
    In production, this would consume from Kafka or a message queue.
    """
    with open(filepath, "r") as f:
        for line in f:
            event = json.loads(line.strip())
            yield event
            time.sleep(0.01)  # simulate arrival delay between events


def validate(event: Dict) -> bool:
    """Check that the event has the required fields and valid values."""
    required_fields = ["order_id", "customer_id", "order_value_gbp", "region"]
    if not all(field in event for field in required_fields):
        return False
    if event["order_value_gbp"] <= 0:
        return False
    return True


def enrich(event: Dict) -> Dict:
    """Add derived fields to the event before routing downstream."""
    event["processed_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    event["value_tier"] = (
        "high" if event["order_value_gbp"] >= 500
        else "mid" if event["order_value_gbp"] >= 100
        else "low"
    )
    return event


def run_streaming_pipeline(source_file: str) -> None:
    """Process each event as it arrives from the source."""
    processed = 0
    skipped = 0

    for raw_event in event_source(source_file):
        if not validate(raw_event):
            skipped += 1
            continue

        enriched_event = enrich(raw_event)

        # In production: publish to downstream topic or write to sink
        print(
            f"[{enriched_event['processed_at']}] "
            f"Order {enriched_event['order_id']} | "
            f"£{enriched_event['order_value_gbp']:.2f} | "
            f"tier={enriched_event['value_tier']}"
        )
        processed += 1

    print(f"\nDone. Processed: {processed} | Skipped: {skipped}")


if __name__ == "__main__":
    run_streaming_pipeline("order_events.jsonl")

