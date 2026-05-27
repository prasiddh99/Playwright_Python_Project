import random
import string
from datetime import datetime


def generate_random_email():

    random_number = random.randint(1000, 9999)

    return f"parth{random_number}@gmail.com"


def generate_random_string(length=5):

    letters = string.ascii_letters

    return ''.join(random.choice(letters) for _ in range(length))


def current_timestamp():

    return datetime.now().strftime("%Y%m%d_%H%M%S")