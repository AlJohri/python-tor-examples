#!/usr/bin/env python3

import requests

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

url = 'http://icanhazip.com/'

response = requests.get(url)
host_ip = response.text.strip()
print(f'ip: {host_ip}')

response = requests.get(url, proxies=proxies)
tor_ip = response.text.strip()
print(f'tor ip: {tor_ip}')
