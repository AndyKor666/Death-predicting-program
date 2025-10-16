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

def is_valid_date_parts(mm,dd,yyyy):
    days_in_month = {
        1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
        7:31, 8:31, 9:30, 10:31, 11:30, 12:31
    }
    if mm < 1 or mm > 12:
        return False
    max_day = days_in_month.get(mm, 31)
    if dd < 1 or dd > max_day:
        return False
    if yyyy < 1900 or yyyy > date.today().year:
        return False
    return True

def parse_birth_date(date_str):
    parts = date_str.split('.')
    if len(parts) != 3:
        return None
    try:
        mm, dd, yyyy = map(int, parts)
    except ValueError:
        return None
    if not is_valid_date_parts(mm, dd, yyyy):
        return None
    try:
        return date(yyyy, mm, dd)
    except ValueError:
        return None

def predict_death(birth_date):
    fate_roll = random.randint(1,10)
    if fate_roll==1:
    elif fate_roll==2:
    elif fate_roll==3:

    years_to_add=random.randint(18, 80)
    extra_days=random.randint(0, 364)
    target_year=birth_date.year+years_to_add
    try:
        death=birth_date.replace(year=target_year)+timedelta(days=extra_days)
    except ValueError:
        if birth_date.month == 2 and birth_date.day == 29:
            corrected = date(target_year, 2, 28)
            death = corrected + timedelta(days=extra_days)
        else: