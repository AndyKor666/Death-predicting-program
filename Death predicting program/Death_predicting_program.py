import random
import time
from datetime import datetime, date, timedelta

def slow_print(text, delay=0.03):
    for line in text.split('\n'):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
        time.sleep(delay*10)