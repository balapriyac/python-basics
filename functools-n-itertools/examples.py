from functools import lru_cache

@lru_cache(maxsize=128)
def fetch_user_data(user_id):
    # Expensive database call
    return database.get_user(user_id)

# First call hits database, subsequent calls use cache
user = fetch_user_data(123)  # Database call
user = fetch_user_data(123)  # Returns cached result

from itertools import chain

# Process multiple log files as one stream
error_logs = ['app.log', 'db.log', 'api.log']
all_lines = chain.from_iterable(open(f) for f in error_logs)

error_count = sum(1 for line in all_lines if 'ERROR' in line)


from itertools import combinations

features = ['cache', 'compression', 'cdn']

# Test all pairs of features
for combo in combinations(features, 2):
    performance = test_feature_combo(combo)
    print(f"{combo}: {performance}ms")


from functools import reduce

# Calculate compound interest
monthly_rates = [1.01, 1.02, 0.99, 1.015]  # Monthly growth rates

final_amount = reduce(lambda total, rate: total * rate, monthly_rates, 1000)
print(f"Final amount: ${final_amount:.2f}")



