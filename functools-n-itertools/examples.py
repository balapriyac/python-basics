from functools import lru_cache

@lru_cache(maxsize=128)
def fetch_user_data(user_id):
    # Expensive database call
    return database.get_user(user_id)

# First call hits database, subsequent calls use cache
user = fetch_user_data(123)  # Database call
user = fetch_user_data(123)  # Returns cached result


