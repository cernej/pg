import json

data = [
    {'Jmeno': 'Alice', 'vek': 20, 'student': True}, 
    {'Jmeno': 'Bob', 'vek': 25, 'student': False}, 
    {'Jmeno': 'Dave', 'vek': 31, 'student': False}, 
    {'Jmeno': 'Monika', 'vek': 28, 'student': True}
]

if __name__ == "__main__":
    
    data.pop(3)
    print(data)
    
    with open("data.json", "w") as fp:
        fp.write(json_data)

    with open("data.json", "r") as fp:
        json_data2 = fp.read()
        data2 = json.loads(json_data2)
    
    data2.pop(0)
    print(data2)

