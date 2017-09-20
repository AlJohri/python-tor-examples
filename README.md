# python-tor-examples

Examples on how to use Tor in python with [`requests`](https://github.com/kennethreitz/requests) or [`aiohttp`](https://github.com/KeepSafe/aiohttp) (via [`aiosocks`](https://github.com/nibrag/aiosocks)).

Assumes Tor will run on `127.0.0.1:9050`.

Requires Python 3.6+

## Setup

```
pipenv install
```

## Usage

```
pipenv run python tor_with_aiohttp.py
pipenv run python tor_with_requests.py
```

## Setting up Python and Pipenv

```
brew install python3
pip3 install --upgrade pipenv
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
