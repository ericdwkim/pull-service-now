import logging
import requests
import os
import json
from utils.log_config import setup_logger


class Main:

    def __init__(self):
        setup_logger()

    def get_data(self):

        username = os.getenv('PDI_USERNAME')
        pw = os.getenv('PDI_PASSWORD')
        url = "https://dev82765.service-now.com/api/now/table/incident"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        res = requests.get(url, auth=(username, pw), headers=headers)


        if res.status_code != 200:
            logging.error('Status', res.status_code, 'Headers:', res.headers, 'Error Response:', res.json())
            exit()

        data = res.json()

        return json.dumps(data, indent=4)


if __name__ == "__main__":
    main = Main()
    data = main.get_data()
    logging.info(f'Fetched data:\n {data}\n')