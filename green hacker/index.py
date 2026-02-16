# first install this mudles => pip install colorama

import random
import string
import time
from colorama import Fore, Style, init

init(autoreset=True)

chars = string.ascii_letters + string.digits + "!@#$%^&*()"

while True:
    line = ''.join(random.choice(chars) for _ in range(80))
    print(Fore.GREEN + line)
    time.sleep(0.01)
