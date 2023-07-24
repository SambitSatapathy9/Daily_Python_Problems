#Problem 21 (24.06.2023)
## Problem Statement - Write a Python program to  extract year, month, date and time using Lambda.

import datetime
now = datetime.datetime.now()
print(now)

year       = lambda x: x.year
month      = lambda x: x.month
day        = lambda x: x.day
time       = lambda x:x.time()
print(f"DD:MM:YYYY, Time - {day(now)}:{month(now)}:{year(now)}, {time(now)}")
