import json


def get_json_data():
    with open("endpoints_data.json", "r") as read_file:
        return json.load(read_file)


def get_endpoints_data():
    json_data = get_json_data()

    data = {
        "linguistic": {
            "AmorphousURI": [],
            "CRUDyURI": [],
            "ContextlessResource": [],
            "NonHierarchicalNodes": [],
            "PluralisedNodes": []
        },
        "design": {
            "isBreakingSelfDescriptiveness": [],
            "isForgettingHypermedia": [],
            "isIgnoringCaching": [],
            "isIgnoringMIMEType": [],
            "isIgnoringStatusCode": [],
            "isMisusingCookies": []
        }
    }

    for endpoint in json_data:
        for lKey in data["linguistic"].keys():
            lBinary = 1 if endpoint["linguisticAntipatterns"][lKey] else 0
            data["linguistic"][lKey].append(lBinary)

        for dKey in data["design"].keys():
            dBinary = 1 if endpoint["designAntipatterns"][dKey] else 0
            data["design"][dKey].append(dBinary)

    return data
