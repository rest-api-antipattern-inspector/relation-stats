import json


def get_endpoints():
    with open("endpoints_data.json", "r") as read_file:
        return json.load(read_file)
