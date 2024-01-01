# time til but in python so that I can think of the logic or something


from datetime import date

Today = str(date.today())

# print(day1,day2,month1,month2)

#while correct:
#    if day2 > 0 & day2 < 32 & day1 > 0 & day1 < 32:
#        correct = False
#    if day2 < 0 & day2 > 32 & day1 > 0 & day1 > 32:
#        print("Please type in a day value which does not exceed 31 and does not go bellow 0")
#    if month1 > 0 & month1 < 13:
#        correct = False
#    elif month1 < 0 & month1 > 13:
#        correct = False
#        print("Please type in a month value which does not exceed 12 and does not got bellow 0")

while True:
    NextDate = input("Please type in your desired date (use the format yyyy-mm-dd with the -: ")
    try:
        year,month,day = map(int, NextDate.split("-"))
        if 0 < day <= 31 and 0 < month <= 12:
            break
        else:
            print("Invalid input, please try again")
    except ValueError:
        print("Invalid format, please try agaon")

# Split the Today string into individual date objects
list1 = Today.split("-")# Take out the year from the list
year2 = int(list1[0].strip())

# Take out the month from the list
month2 = int(list1[1].strip())

# Take out the day from the list
day2 = int(list1[2].strip())

# dd/mm/yy 24/12/2024

# 1 - 31 days
# 2 - 28||29 days
# 3 - 31 days
# 4 - 30 days
# 5 - 31 days
# 6 - 30 days
# 7 - 31 days
# 8 - 31 days
# 9 - 30 days
# 10 - 31 days
# 11 - 30 days
# 12 - 31 days



# list of days

FirDay = 31
SecDay = 28
ThirDay = 31
FourDay = 30
FiveDay = 31
SixDay = 30
SevenDay = 31
EightDay = 31
NineDay = 30
TenDay = 31
ElevDay = 30
TwelvDay = 31

# year = 2024

# We need to calculate each year length, some years
# are longer than others (leap years) for that we
# make a for loop which checks if every year after the
# one we are in is a leap year, and then stores an
# additional day which we add onto the day difference
# (AddDays being the one which adds the day diff)
# (Year count being the way we check each year)

AddDays = 0
YearCount = year

for i in range(year-year2):
    if YearCount % 4 == 0 & YearCount % 4 == 0:
        print("Leap year detected")
        AddDays += 1
    elif YearCount % 4 == 0 & YearCount % 400 == 0:
        print("Leap year detected")
        AddDays += 1
    else:
        print("The curhowManyMonthsrent year is not a leap year")
    YearCount += 1

print("Desired year: ", year)
print("Current year: ", year2)

# calculating the time until said date

# we need to take the difference between the days months and years

# month2 is the current
# day2 is the current
# year2 is the current



# curr day 5
# desire day 6
# 11 = 31-5 = 26+6
# (count in the desired days plus the days until the next month) = 32
# we do this to get the next month in order to set a value for
# "month" in the print out, like 3 months until x
if month == 1:
    NextMonthOver = SecDay
elif month == 2:
    NextMonthOver = ThirDay
elif month == 3:
    NextMonthOver = FourDay
elif month == 4:
    NextMonthOver = FiveDay
elif month == 5:
    NextMonthOver = SixDay
elif month == 6:
    NextMonthOver = SevenDay
elif month == 7:
    NextMonthOver = EightDay
elif month == 8:
    NextMonthOver = NineDay
elif month == 9:
    NextMonthOver = TenDay
elif month == 10:
    NextMonthOver = ElevDay
elif month == 11:
    NextMonthOver = TwelvDay
elif month == 12:
    NextMonthOver = FirDay

print("The next month is", NextMonthOver, "days long")

DayDiff = day-day2+AddDays
MonthDiff = month-month2
YearDiff = year-year2

print("Days:", DayDiff, "months:", MonthDiff, "Years:", YearDiff)
# we need to know which months are in between the
# two if the months are not the same
# first we check if the months are the same and if 
# the years are the same 
howManyMonths = 0


# this is a planned feature to calculate the total days
# instead of just the months and days
ListOfMonths = []
if month != month2 & year2 != year:
    if MonthDiff < 0:
        for i in range(MonthDiff*-1):
            howManyMonths += 1
            print(howManyMonths)
            month -= 1
            print(month)
            if month == 1 or month == -12:
                ListOfMonths.append("FirDay")
            elif month == 2 or month == -11:
                ListOfMonths.append("SecDay")
            elif month == 3 or month == -10:
                ListOfMonths.append("ThirDay")
            elif month == 4 or month == -9:
                ListOfMonths.append("FourDay")
            elif month == 5 or month == -8:
                ListOfMonths.append("FiveDay")
            elif month == 6 or month == -7:
                ListOfMonths.append("SixDay")
            elif month == 7 or month == -6:
                ListOfMonths.append("SevenDay")
            elif month == 8 or month == -5:
                ListOfMonths.append("EightDay")
            elif month == 9 or month == -4:
                ListOfMonths.append("NineDay")
            elif month == 10 or month == -3:
                ListOfMonths.append("TenDay")
            elif month == 11 or month == -2:
                ListOfMonths.append("ElevDay")
            elif month == 12 or month == -1:
                ListOfMonths.append("TwelvDay")
            elif month == 0:
                ListOfMonths.append("SecDay")
elif year > year2:
    print("Desired year is bigger than current")
    for i in range(MonthDiff*-1):
            howManyMonths += 1
            print(howManyMonths)
            month -= 1
            print(month)
            if month == 1 or month == -12:
                ListOfMonths.append("FirDay")
            elif month == 2 or month == -11:
                ListOfMonths.append("SecDay")
            elif month == 3 or month == -10:
                ListOfMonths.append("ThirDay")
            elif month == 4 or month == -9:
                ListOfMonths.append("FourDay")
            elif month == 5 or month == -8:
                ListOfMonths.append("FiveDay")
            elif month == 6 or month == -7:
                ListOfMonths.append("SixDay")
            elif month == 7 or month == -6:
                ListOfMonths.append("SevenDay")
            elif month == 8 or month == -5:
                ListOfMonths.append("EightDay")
            elif month == 9 or month == -4:
                ListOfMonths.append("NineDay")
            elif month == 10 or month == -3:
                ListOfMonths.append("TenDay")
            elif month == 11 or month == -2:
                ListOfMonths.append("ElevDay")
            elif month == 12 or month == -1:
                ListOfMonths.append("TwelvDay")
            elif month == 0:
                ListOfMonths.append("SecDay")


print(ListOfMonths)
