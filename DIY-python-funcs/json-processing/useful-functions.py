def get_nested_value(data, path, default=None):
    """
    Safely extract nested values from JSON using dot notation.

    Args:
        data: Dictionary or JSON object
        path: Dot-separated string like "user.profile.email"
        default: Value to return if path doesn't exist

    Returns:
        The value at the path, or default if not found
    """
    keys = path.split('.')
    current = data

    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
            if current is None:
                return default
        elif isinstance(current, list):
            try:
                index = int(key)
                current = current[index]
            except (ValueError, IndexError):
                return default
        else:
            return default

    return current

# Sample JSON data
user_data = {
    "user": {
        "id": 123,
        "profile": {
            "name": "Alice",
            "email": "alice@example.com",
            "settings": {
                "theme": "dark",
                "notifications": True
            }
        },
        "posts": [
            {"id": 1, "title": "First Post"},
            {"id": 2, "title": "Second Post"}
        ]
    }
}

# Extract values
email = get_nested_value(user_data, "user.profile.email")
theme = get_nested_value(user_data, "user.profile.settings.theme")
first_post = get_nested_value(user_data, "user.posts.0.title")
missing = get_nested_value(user_data, "user.profile.age", default=25)

print(f"Email: {email}")
print(f"Theme: {theme}")
print(f"First post: {first_post}")
print(f"Age (default): {missing}")

def flatten_json(data, parent_key='', separator='_'):
    """
    Flatten nested JSON into a single-level dictionary.

    Args:
        data: Nested dictionary or JSON object
        parent_key: Prefix for keys (used in recursion)
        separator: String to join nested keys

    Returns:
        Flattened dictionary with concatenated keys
    """
    items = []

    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}{separator}{key}" if parent_key else key

            if isinstance(value, dict):
                # Recursively flatten nested dicts
                items.extend(flatten_json(value, new_key, separator).items())
            elif isinstance(value, list):
                # Flatten lists with indexed keys
                for i, item in enumerate(value):
                    list_key = f"{new_key}{separator}{i}"
                    if isinstance(item, (dict, list)):
                        items.extend(flatten_json(item, list_key, separator).items())
                    else:
                        items.append((list_key, item))
            else:
                items.append((new_key, value))
    else:
        items.append((parent_key, data))

    return dict(items)

# Complex nested JSON
product_data = {
    "product": {
        "id": 456,
        "name": "Laptop",
        "specs": {
            "cpu": "Intel i7",
            "ram": "16GB",
            "storage": {
                "type": "SSD",
                "capacity": "512GB"
            }
        },
        "reviews": [
            {"rating": 5, "comment": "Excellent"},
            {"rating": 4, "comment": "Good value"}
        ]
    }
}

flattened = flatten_json(product_data)

for key, value in flattened.items():
    print(f"{key}: {value}")

def deep_merge_json(base, override):
    """
    Deep merge two JSON objects, with override taking precedence.

    Args:
        base: Base dictionary
        override: Dictionary with values to override/add

    Returns:
        New dictionary with merged values
    """
    result = base.copy()

    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            # Recursively merge nested dictionaries
            result[key] = deep_merge_json(result[key], value)
        else:
            # Override or add the value
            result[key] = value

    return result

# Default configuration
default_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "timeout": 30,
        "pool": {
            "min": 2,
            "max": 10
        }
    },
    "cache": {
        "enabled": True,
        "ttl": 300
    },
    "logging": {
        "level": "INFO"
    }
}

# Production overrides
prod_config = {
    "database": {
        "host": "prod-db.example.com",
        "pool": {
            "min": 5,
            "max": 50
        }
    },
    "cache": {
        "ttl": 600
    },
    "monitoring": {
        "enabled": True
    }
}

merged = deep_merge_json(default_config, prod_config)

import json
print(json.dumps(merged, indent=2))

def filter_json(data, schema):
    """
    Filter JSON to keep only fields specified in schema.

    Args:
        data: Dictionary or JSON object to filter
        schema: Dictionary defining which fields to keep
                Use True to keep a field, nested dict for nested filtering

    Returns:
        Filtered dictionary containing only specified fields
    """
    if not isinstance(data, dict) or not isinstance(schema, dict):
        return data

    result = {}

    for key, value in schema.items():
        if key not in data:
            continue

        if value is True:
            # Keep this field as-is
            result[key] = data[key]
        elif isinstance(value, dict):
            # Recursively filter nested object
            if isinstance(data[key], dict):
                filtered_nested = filter_json(data[key], value)
                if filtered_nested:
                    result[key] = filtered_nested
            elif isinstance(data[key], list):
                # Filter each item in the list
                filtered_list = []
                for item in data[key]:
                    if isinstance(item, dict):
                        filtered_item = filter_json(item, value)
                        if filtered_item:
                            filtered_list.append(filtered_item)
                    else:
                        filtered_list.append(item)
                if filtered_list:
                    result[key] = filtered_list

    return result

# Large API response
api_response = {
    "user": {
        "id": 789,
        "username": "bob",
        "email": "bob@example.com",
        "password_hash": "secret123",
        "profile": {
            "name": "Bob Smith",
            "bio": "Software developer",
            "avatar_url": "https://example.com/avatar.jpg",
            "private_notes": "Internal notes"
        },
        "posts": [
            {
                "id": 1,
                "title": "Hello World",
                "content": "My first post",
                "views": 100,
                "internal_score": 0.85
            },
            {
                "id": 2,
                "title": "Python Tips",
                "content": "Some tips",
                "views": 250,
                "internal_score": 0.92
            }
        ]
    },
    "metadata": {
        "request_id": "abc123",
        "server": "web-01"
    }
}

# Schema defining what to keep
public_schema = {
    "user": {
        "id": True,
        "username": True,
        "profile": {
            "name": True,
            "avatar_url": True
        },
        "posts": {
            "id": True,
            "title": True,
            "views": True
        }
    }
}

filtered = filter_json(api_response, public_schema)

import json
print(json.dumps(filtered, indent=2))

def json_to_dot_notation(data, parent_key=''):
    """
    Convert nested JSON to flat dot-notation dictionary.

    Args:
        data: Nested dictionary
        parent_key: Prefix for keys (used in recursion)

    Returns:
        Flat dictionary with dot-notation keys
    """
    items = {}

    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}.{key}" if parent_key else key

            if isinstance(value, dict):
                items.update(json_to_dot_notation(value, new_key))
            else:
                items[new_key] = value
    else:
        items[parent_key] = data

    return items


def dot_notation_to_json(flat_data):
    """
    Convert flat dot-notation dictionary to nested JSON.

    Args:
        flat_data: Dictionary with dot-notation keys

    Returns:
        Nested dictionary
    """
    result = {}

    for key, value in flat_data.items():
        parts = key.split('.')
        current = result

        for i, part in enumerate(parts[:-1]):
            if part not in current:
                current[part] = {}
            current = current[part]

        current[parts[-1]] = value

    return result

# Original nested JSON
config = {
    "app": {
        "name": "MyApp",
        "version": "1.0.0"
    },
    "database": {
        "host": "localhost",
        "credentials": {
            "username": "admin",
            "password": "secret"
        }
    },
    "features": {
        "analytics": True,
        "notifications": False
    }
}

# Convert to dot notation (for environment variables)
flat = json_to_dot_notation(config)
print("Flat format:")
for key, value in flat.items():
    print(f"  {key} = {value}")

print("\n" + "="*50 + "\n")

# Convert back to nested JSON
nested = dot_notation_to_json(flat)
import json
print("Nested format:")
print(json.dumps(nested, indent=2))

# Load from environment variables
import os
flat_config = {
    "database.host": os.getenv("DATABASE_HOST", "localhost"),
    "database.port": os.getenv("DATABASE_PORT", "5432"),
    "api.key": os.getenv("API_KEY")
}

# Convert to nested structure for use in code
app_config = dot_notation_to_json(flat_config)
db_host = app_config["database"]["host"]


