import data

endpoints = data.get_endpoints()

for ep in endpoints:
    print(ep["endpoint"])
