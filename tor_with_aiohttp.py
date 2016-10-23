#!/usr/bin/env python3

import asyncio
import aiohttp
import aiosocks
from aiosocks.connector import SocksConnector

async def main():
  response = await aiohttp.get('http://icanhazip.com/')
  body = await response.text()
  print('ip: {}'.format(body.strip()))

  addr = aiosocks.Socks5Addr('127.0.0.1', 9050)
  conn = SocksConnector(proxy=addr, remote_resolve=False)
  response = await aiohttp.get('http://icanhazip.com/', connector=conn)
  body = await response.text()
  print('tor ip: {}'.format(body.strip()))

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  loop.close()
