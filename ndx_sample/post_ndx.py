import csv
import sys
import requests
import random
import json
from urllib.parse import urlparse

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("wrong number of args.")
        sys.exit(1)
    pr = urlparse(sys.argv[1])
    if pr[0] == '' or pr[1] == '':
        print("wrong base url given.")
        sys.exit(2)
    token = sys.argv[2]
    r = requests.get(
        '{}/api/stocks'.format(sys.argv[1]),
        headers={
            'Authorization': 'Bearer ' + token
        }
    )
    if (r.status_code != 200):
        print("wrong token given.")
        sys.exit(3)
    symbol_list = []
    with open('NASDAQ.csv', mode='r') as infile:
        reader = csv.DictReader(infile)
        for line in reader:
            symbol_list.append(line['Symbol'].strip())
    with open('NYSE.csv', mode='r') as infile:
        reader = csv.DictReader(infile)
        for line in reader:
            symbol_list.append(line['Symbol'].strip())
    with open('ASX.csv', mode='r') as infile:
        reader = csv.DictReader(infile)
        for line in reader:
            symbol_list.append(line['ASX code'].strip())
    symbol_list = list(set(symbol_list))
    print('Total Number Of Symbol: {}'.format(len(symbol_list)))
    with open('ndx.csv', mode='r') as infile:
        reader = csv.DictReader(infile)
        for line in reader:
            line.pop('oi', None)
            line['symbol'] = random.choice(symbol_list)
            symbol_list.remove(line['symbol'])
            r = requests.post(
                '{}/api/stock'.format(sys.argv[1]),
                data=json.dumps(line),
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + token
                }
            )
            print(r.status_code)
            print(r.text)
