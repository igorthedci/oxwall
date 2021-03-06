import json
import os.path
import random
import string
from conftest import PROJECT_DIR

with open(os.path.join(PROJECT_DIR, "data", "status_data.json"), encoding="utf8") as f:
    status_data = json.load(f)


def random_string(maxlength):
    length = random.randint(1, maxlength)
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    result = ""
    for _ in range(length):
        result += random.choice(symbols)
    return result
    # return ''.join([random.choice(symbols) for _ in range(length)])


status_data += [random_string(33) for _ in range(9)]

if __name__ == "__main__":
    print(random.random())
    print(random.randint(100, 200))
    print(random.randrange(2, 98, 2))
    print(random.choice(status_data))
    print(random_string(33))
