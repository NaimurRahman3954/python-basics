print("What's the year, Buddy?")
yearStr = input()
year = int(yearStr)

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("It's a leap year")
else:
    print("not a leap year")
