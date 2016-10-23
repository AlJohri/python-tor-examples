#!/usr/bin/env python3

import requests

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

url = 'http://icanhazip.com/'

response = requests.get(url)
print('ip: {}'.format(response.text.strip()))

response = requests.get(url, proxies=proxies)
print('tor ip: {}'.format(response.text.strip()))
