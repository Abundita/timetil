# time til but in python so that I can think of the logic or something
# Imports
from datetime import date
# Variables
# error checking, checks if the user has inputted the correct format
# also checks if the user has inputted proper lengths
while True:
    NextDate = input("Please type in your desired date (use the format yyyy-mm-dd with the -: ")
    try:
        desired_year, desired_month, desired_day = map(int, NextDate.split("-"))
        if 0 < desired_day <= 31 and 0 < desired_month <= 12:
            break
        else:
            print("Invalid input, please try again")
    except ValueError:
        print("Invalid format, please try again")

# Variables
YearCount = desired_year
Today = date.today()
today_year, today_month, today_day = Today.year, Today.month, Today.day
# better method of storing all of the months
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# better way of checking leap years, we make a for loop
# which goes from out current year until the desired year
# and then checks if each year is equally divisible by either 4 or 400
# if it is then it sums them up (the ammount of years not the years themselves)

add_leap_years = sum(1 for i in range(today_year, desired_year) if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0))

DayDiff = desired_day-today_day+add_leap_years
MonthDiff = desired_month-today_month
YearDiff = desired_year-today_year

print("Days:", DayDiff, "months:", MonthDiff, "Years:", YearDiff)
