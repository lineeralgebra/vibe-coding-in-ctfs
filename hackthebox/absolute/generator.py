import sys

def username_generator(first, last):
    first = first.lower()
    last = last.lower()
    usernames = []
    usernames.append(first)  # first
    usernames.append(first + last)  # firstlast
    usernames.append(first + "." + last)  # first.last
    usernames.append(first + last[0])  # firstl
    usernames.append(first[0] + "." + last)  # f.last
    usernames.append(first[0] + last)  # flast
    return usernames
if len(sys.argv) < 2:
    print("Usage: python3 generator.py list.txt")
    sys.exit(1)

filename = sys.argv[1]
all_usernames = []

with open(filename, "r") as file:
    for line in file:
        line = line.strip()
        parts = line.split()
        first = parts[0]
        last = parts[1]
        generated = username_generator(first, last)
        all_usernames.extend(generated)

for username in all_usernames:
    print(username)

with open("usernames.txt", "w") as outfile:
    for username in all_usernames:
        outfile.write(username + "\n")
