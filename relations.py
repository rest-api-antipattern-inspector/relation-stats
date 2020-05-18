import json

with open("endpoints_data.json", "r") as read_file:
    endpoints = json.load(read_file)

    for ep in endpoints:
        print(ep["endpoint"])
