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
