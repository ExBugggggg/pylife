import string
import random

def generate_random_string(length: int = 10) -> str:
    return ''.join(random.sample(string.ascii_letters + string.digits, length))