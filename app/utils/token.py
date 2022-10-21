import hmac
from hashlib import sha1

def HmacSHA1(key, code):
    hash_string = hmac.new(key.encode(), code.encode(), sha1)
    return hash_string.hexdigest()