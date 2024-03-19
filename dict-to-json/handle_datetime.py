import json
from datetime import datetime

# Define custom serialization function for datetime objects
def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()

# Sample dictionary with a datetime object
data = {
    "event": "Meeting",
    "date": datetime.now()
}

# Convert dictionary to JSON string 
json_string = json.dumps(data, default=serialize_datetime, indent=2)
print(json_string)
