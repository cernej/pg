import re
import json
import datetime

r_date = re.compile(r"\d{4}-\d{2}-\d{2}")


def datetime_serializer(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")


def datetime_deserializer(obj):
    for key, value in obj.items():
        if isinstance(value, str) and r_date.match(value):
            obj[key] = datetime.datetime.fromisoformat(value)
    return obj


data = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "Main Street",
        "city": "New York"
    },
    "phone": [
        "123456789",
        "987654321"
    ],
    "isMarried": True,
    "isEmployed": False,
    "born": datetime.datetime(1990, 1, 1)
}

print(data)

json_data = json.dumps(data, default=datetime_serializer)

print(json_data)

data2 = json.loads(json_data, object_hook=datetime_deserializer)

print(type(data2["born"]))

print(data2)