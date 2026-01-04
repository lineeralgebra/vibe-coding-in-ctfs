payloads = []

with open("basic-payloads.txt", "r") as file:
    payloads = file.read().splitlines()

modified_payloads = []

wrappers = ["$", "#", "&"]

for payload in payloads:
    modified_payloads.append(payload)

    for char in wrappers:
        modified_payloads.append(f"{char}{payload}{char}")

for p in modified_payloads:
    print(p)

with open("modified-payloads.txt", "w") as outfile:
    for p in modified_payloads:
        outfile.write(p + "\n")
