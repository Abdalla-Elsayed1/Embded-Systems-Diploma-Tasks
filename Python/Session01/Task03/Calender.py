import calendar
year = input("input the year: ")
month = input("input the month: ")
dates = calendar.month(int(year), int(month))
print(dates)