import json

json_string = '{"name": "Sarah Chen", "age": 28, "city": "Portland"}'
person = json.loads(json_string)

print(person["name"])  # Sarah Chen
print(person["age"])   # 28
print(type(person))    # <class 'dict'>

weather_data = '''
{
    "location": {
        "city": "Seattle",
        "state": "WA",
        "coordinates": {
            "latitude": 47.6062,
            "longitude": -122.3321
        }
    },
    "current": {
        "temperature_f": 58,
        "conditions": "Partly Cloudy",
        "humidity": 72,
        "wind": {
            "speed_mph": 8,
            "direction": "NW"
        }
    }
}
'''

weather = json.loads(weather_data)

city = weather["location"]["city"]
temp = weather["current"]["temperature_f"]
wind_speed = weather["current"]["wind"]["speed_mph"]

print(f"{city}: {temp}°F, Wind {wind_speed} mph")


products_json = '''
[
    {
        "id": "PROD-001",
        "name": "Wireless Mouse",
        "price": 24.99,
        "in_stock": true
    },
    {
        "id": "PROD-002",
        "name": "Mechanical Keyboard",
        "price": 89.99,
        "in_stock": false
    },
    {
        "id": "PROD-003",
        "name": "USB-C Hub",
        "price": 34.99,
        "in_stock": true
    }
]
'''

products = json.loads(products_json)

print(f"Total products: {len(products)}")

for product in products:
    status = "Available" if product["in_stock"] else "Out of stock"
    print(f"{product['name']}: ${product['price']} - {status}")

first_product = products[0]
print(f"First product ID: {first_product['id']}")

available_products = [p for p in products if p["in_stock"]]
print(f"Available: {len(available_products)} products")

# First, let's create a sample config
config_data = {
    "api_url": "https://api.example.com/v2",
    "timeout": 30,
    "retry_attempts": 3,
    "enable_logging": True
}

with open('config.json', 'w') as f:
    json.dump(config_data, f, indent=2)

with open('config.json', 'r') as f:
    config = json.load(f)

print(f"API URL: {config['api_url']}")
print(f"Timeout: {config['timeout']} seconds")
print(f"Logging: {'Enabled' if config['enable_logging'] else 'Disabled'}")


def parse_json_safely(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"JSON parsing failed: {e.msg}")
        print(f"Error at line {e.lineno}, column {e.colno}")
        return None

# Missing closing quote
bad_json1 = '{"name": "Sarah, "age": 28}'
result1 = parse_json_safely(bad_json1)
print(f"Result 1: {result1}\n")

# Missing closing brace
bad_json2 = '{"name": "Sarah", "age": 28'
result2 = parse_json_safely(bad_json2)
print(f"Result 2: {result2}\n")

# Extra comma
bad_json3 = '{"name": "Sarah", "age": 28,}'
result3 = parse_json_safely(bad_json3)
print(f"Result 3: {result3}\n")

# Valid JSON for comparison
good_json = '{"name": "Sarah", "age": 28}'
result4 = parse_json_safely(good_json)
print(f"Result 4: {result4}")

def load_json_file_safely(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        return None
    except PermissionError:
        print(f"Error: Permission denied reading '{filepath}'")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{filepath}'")
        print(f"  {e.msg} at line {e.lineno}")
        return None

data = load_json_file_safely('missing_file.json')
if data is None:
    print("Using default configuration")
    data = {"timeout": 30, "retries": 3}
