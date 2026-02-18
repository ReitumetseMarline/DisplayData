import json

with open("covid.json", "r") as file:
    data = json.load(file)

    print(data)