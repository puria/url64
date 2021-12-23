import json
from base64 import urlsafe_b64encode, urlsafe_b64decode

__all__ = ['encode', 'decode']


def pad(s):
    return s + '=' * (4 - len(s) & 3)


def encode(s):
    if isinstance(s, dict):
        s = json.dumps(s).encode()

    if isinstance(s, str):
        s = s.encode()
    return urlsafe_b64encode(s).decode().rstrip("=")


def decode(s):
    return urlsafe_b64decode(pad(s)).decode()
