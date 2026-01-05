password = "PleaseSubscribe!"

numbers = range(1, 100)

modified_passwords = []

for number in numbers:
    modified_passwords.append(f"{password}{number}")

for p in modified_passwords:
    print(p)

with open("passwods.txt", "w") as outfile:
    for p in modified_passwords:
        outfile.write(p + "\n")
