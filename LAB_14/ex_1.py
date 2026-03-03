from datetime import datetime, timedelta
import time
import calendar

print("DATES AND TIMES LABORATORY")
print("=" * 40)

# Exercise 1: Current Date and Time
now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"\n1. Current Date and Time: {formatted}")

# Exercise 2: Days Until New Year
current = datetime.now()
new_year = datetime(current.year, 12, 31)
if current > new_year:
    new_year = datetime(current.year + 1, 12, 31)
days_left = (new_year - current).days
print(f"\n2. Days until New Year's Eve: {days_left}")

# Exercise 3: Countdown Timer
def countdown_timer(seconds):
    print(f"\n3. Countdown Timer ({seconds} seconds):")
    end = datetime.now() + timedelta(seconds=seconds)
    while True:
        remaining = end - datetime.now()
        secs = int(remaining.total_seconds())
        if secs <= 0:
            break
        print(f"   Time remaining: {secs} seconds", end="\r")
        time.sleep(1)
    print("\n   Timer finished!")

countdown_timer(5)

# Exercise 4: Month Calendar
def month_calendar(year, month):
    print(f"\n4. Calendar for {month}/{year}:")
    cal = calendar.month(year, month)
    print(cal)

month_calendar(2026, 3)

# Bonus: Date Arithmetic
print("\n5. Date Arithmetic:")
today = datetime.now()
week_later = today + timedelta(days=7)
week_ago = today - timedelta(days=7)
print(f"   Today: {today.strftime('%Y-%m-%d')}")
print(f"   Next week: {week_later.strftime('%Y-%m-%d')}")
print(f"   Last week: {week_ago.strftime('%Y-%m-%d')}")