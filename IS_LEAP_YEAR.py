import time
from calendar import isleap

# --- HELPER FUNCTIONS ---
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2:
        return 28








#--MAIN PROGRAM--#
name = input("Your name: ")
age = input("Your age: ")

year = int(age)


localtime = time.localtime(time.time())
month = 12 * year + localtime.tm_mon

begin_year = localtime.tm_year - year
end_year = localtime.tm_year + year

day = 0

for i in range(begin_year, end_year):
    if judge_leap_year(i):
        day += 366
    else:
        day += 365


leap_year = judge_leap_year(localtime.tm_year)

for m in range(1, localtime.tm_mon):
    day += month_days(m, leap_year)


day += localtime.tm_mday


print(name + "'s age is " + str(year) + " years or " + str(month) + " months or " + str(day) + " days")
    
















