import requests
import os

username = os.getenv('PDI_USERNAME')
pw = os.getenv('PDI_PASSWORD')

url = "https://dev82765.service-now.com/"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

res = requests.get(url, auth=(username, pw), headers=headers)

print(res)