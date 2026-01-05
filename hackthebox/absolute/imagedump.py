import requests
import os
numbers = range(1, 100)
base_url = "http://10.129.232.60/images"

os.makedirs("downloads", exist_ok=True)

for number in numbers:
    url = f"{base_url}/hero_{number}.jpg"
    filename = f"downloads/hero_{number}.jpg"

    response = requests.get(url)

    if response.status_code == 200:
        print(url, f"exist")
        with open(filename, "wb") as outfile:
            outfile.write(response.content)
    else:
        continue
