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

def predict_death(name, birth_date):
    fate_roll = random.randint(1,10)
    if fate_roll==1:
        return ">> You will die today . . ."
    elif fate_roll==2:
        return ">> You will die tomorrow . . ."
    elif fate_roll==3:
        return ">> You will die the day after tomorrow . . ."

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
            return ">> ERR . . . Unexpected error in prediction.\n------------------------------------------"

    return f">> {name}'s death date: {death.strftime('%m.%d.%Y')}"

def save_record(name, birth_str, result):
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"DeathRecord_{ts}.txt"
    with open(filename, "a") as f:
        f.write("============== FUTURE DEATH ==============\n")
        f.write("------------------------------------------\n")
        f.write(f">> Name: {name}\n")
        f.write(f">> Birth: {birth_str}\n")
        f.write("------------------------------------------\n")
        f.write(result + "\n")
        f.write("------------------------------------------\n")
        f.write(f">> Record created at {datetime.now().strftime('%H:%M:%S %d.%m.%Y')}\n")
        f.write("------------------------------------------\n")
        f.write("==========================================\n")
    return filename

def main():
    slow_print("=========== FUTURE DEATH SYSTEM ===========")
    slow_print("-------------------------------------------")
    name = input(">> Input your name: ").strip()
    while not name:
        slow_print("-------------------------------------------")
        slow_print(">> ERR . . . Name cannot be empty.")
        slow_print("-------------------------------------------")
        name = input(">> Input your name: ").strip()
    today = date.today()
    while True:
        birth_input = input(">> Input birth date (MM.DD.YYYY): ").strip()
        bd = parse_birth_date(birth_input)
        if bd is None:
            slow_print("-------------------------------------------")
            slow_print(">> ERR . . . Invalid date or wrong format.\n>> Example: 4.13.1997 . . .")
            slow_print("------------------------------------------")
            continue
        if bd > today:
            slow_print(">> ERR . . . Birth date cannot be in the future.")
            slow_print("------------------------------------------")
            continue
        break
    slow_print("-------------------------------------------")
    slow_print(">> Processing . . .")
    time.sleep(1.5)
    slow_print("-------------------------------------------")
    result = predict_death(name, bd)
    slow_print(result)
    saved = save_record(name, birth_input, result)
    slow_print("-------------------------------------------")
    slow_print(f">> Record saved to '{saved}'")
    slow_print("-------------------------------------------")
    slow_print("             --- DEAD END ---              ")
    slow_print("-------------------------------------------")
    slow_print("===========================================")
if __name__ == "__main__":
    main()