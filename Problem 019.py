import datetime

start = datetime.date(1901, 1, 1)

number_sundays_on_first = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if datetime.date(year, month, 1).weekday() == 6:
            number_sundays_on_first += 1

print(number_sundays_on_first)