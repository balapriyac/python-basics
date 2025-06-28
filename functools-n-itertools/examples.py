# ex 1
from functools import lru_cache

@lru_cache(maxsize=128)
def fetch_user_data(user_id):
    # Expensive database call
    return database.get_user(user_id)

# First call hits database, subsequent calls use cache
user = fetch_user_data(123)  # Database call
user = fetch_user_data(123)  # Returns cached result

# ex 2
from itertools import chain

# Process multiple log files as one stream
error_logs = ['app.log', 'db.log', 'api.log']
all_lines = chain.from_iterable(open(f) for f in error_logs)

error_count = sum(1 for line in all_lines if 'ERROR' in line)

# ex 3
from functools import partial
import logging

def log_event(level, component, message):
    logging.log(level, f"[{component}] {message}")

# Create specialized loggers
auth_error = partial(log_event, logging.ERROR, 'AUTH')
db_info = partial(log_event, logging.INFO, 'DATABASE')

# Clean usage
auth_error("Login failed for user")
db_info("Connection established")

# ex 4
from itertools import combinations

features = ['cache', 'compression', 'cdn']

# Test all pairs of features
for combo in combinations(features, 2):
    performance = test_feature_combo(combo)
    print(f"{combo}: {performance}ms")

# ex 5
from functools import singledispatch
from datetime import datetime

@singledispatch
def format_data(value):
    return str(value)  # Default

@format_data.register(datetime)
def _(value):
    return value.strftime("%Y-%m-%d")

@format_data.register(list)
def _(value):
    return ", ".join(str(item) for item in value)

# Automatically picks the right formatter
print(format_data(datetime.now()))  # "2025-06-27"
print(format_data([1, 2, 3]))       # "1, 2, 3"

# ex 6
from itertools import groupby

transactions = [
    {'type': 'credit', 'amount': 100},
    {'type': 'credit', 'amount': 50},
    {'type': 'debit', 'amount': 75},
    {'type': 'debit', 'amount': 25}
]

# Group by transaction type
for trans_type, group in groupby(transactions, key=lambda x: x['type']):
    total = sum(item['amount'] for item in group)
    print(f"{trans_type}: ${total}")

from functools import reduce

# Calculate compound interest
monthly_rates = [1.01, 1.02, 0.99, 1.015]  # Monthly growth rates

final_amount = reduce(lambda total, rate: total * rate, monthly_rates, 1000)
print(f"Final amount: ${final_amount:.2f}")



