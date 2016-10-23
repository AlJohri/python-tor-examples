# python-tor-examples

Examples on how to use Tor in python with [`requests`](https://github.com/kennethreitz/requests) or [`aiohttp`](https://github.com/KeepSafe/aiohttp) (via [`aiosocks`](https://github.com/nibrag/aiosocks)).

Assumes Tor will run on `127.0.0.1:9050`.

## Setup

```
mkvirtualenv python-tor-examples -p python3 -r requirements.txt -a `pwd`
```

## Usage

```
workon python-tor-examples
./tor_with_requests.py
./tor_with_aiohttp.py
```

## Setting up Tor

#### Mac OS X

```
brew install tor
brew services start tor
```

#### Other
- Debian/Ubuntu: https://www.torproject.org/docs/debian.html.en
- Fedora/Centos: https://www.torproject.org/docs/rpms.html.en
- Source: https://www.torproject.org/docs/tor-doc-unix.html.en
