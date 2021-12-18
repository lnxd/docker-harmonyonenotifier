#!/usr/bin/env python3
from apprise import Apprise
from os import environ    
from time import sleep
import json
import requests


def notify(message):
    print("-- Sending notification --")

    apobj = Apprise()
    apobj.add('pover://' + pushover_api_user + '@' + pushover_api_app + '')

    apobj.notify(
        body=message,
        title='Harmony One',
    )

def check_balance(last_balance):
    headers = {
        'Content-Type': 'application/json',
    }

    data = '{\n    "id": "1",\n    "jsonrpc": "2.0",\n    "method": "hmyv2_getBalance",\n    "params": [\n        "' + harmonyone_wallet + '"\n    ]\n}'

    response = requests.post('https://api.harmony.one/', headers=headers, data=data)
    response = json.loads(response.text)
    balance = int(response["result"])
    divisor = int("1" + (len(str(balance))-2)*"0")
    balance = balance/divisor
    if balance != last_balance:
        last_balance = balance
        notify(f"Balance Updated: {str(balance)}")
    return(last_balance)


if __name__ == "__main__":

    print("-- Starting --")

    # Get config
    pushover_api_app     = environ['NOTIFIER_API_APP']
    pushover_api_user    = environ['NOTIFIER_API_USER']
    harmonyone_wallet    = environ['HARMONYONE_WALLET']

    print("-- Checking Balance --")
    last_balance = 0
    initial_run = True
    loop = 0
    while True:
        loop+=1
        try:
            last_balance = check_balance(last_balance)
        except requests.exceptions.ReadTimeout:
            print("Error: Timed out")
            print("Continuing..")
        if loop%30 == 0:
            print("Still checking..")
        initial_run = False
        sleep(10)