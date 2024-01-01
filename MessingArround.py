# time til but in python so that I can think of the logic or something


from datetime import date

Today = str(date.today())
NextDate = input ("Timetil is a utility which calculates the time until a certain date for you! Please type in your desired date (use the format yyyy-mm-dd with the -: ")

# Split the Today string into individual date objects
list1 = Today.split("-")
list2 = NextDate.split("-")
# Take out the year from the list
year2 = int(list1[0].strip())
year1 = int(list2[0].strip())

# Take out the month from the list
month2 = int(list1[1].strip())
month1 = int(list2[1].strip())

# Take out the day from the list
day2 = int(list1[2].strip())
day1 = int(list2[2].strip())


correct = True

#print(day1,day2,month1,month2)

while correct:
    if day2 > 0 & day2 < 32 & day1 > 0 & day1 < 32:
        correct = False
    if day2 < 0 & day2 > 32 & day1 > 0 & day1 > 32:
        print("Please type in a day value which does not exceed 31 and does not go bellow 0")
    if month1 > 0 & month1 < 13:
        correct = False
    elif month1 < 0 & month1 > 13:
        correct = False
        print("Please type in a month value which does not exceed 12 and does not got bellow 0")
        
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
if year1 % 4 == 0 & year1 % 4 == 0:
    print("Leap year detected")
    SecDay = 29
elif year1 % 4 == 0 & year1 % 400 == 0:
    print("Leap year detected")
    SecDay = 29
else:
    print("The curhowManyMonthsrent year is not a leap year")
    SecDay = 28

print ("Desired year: ",year1)
print ("Current year: ",year2)

# calculating the time until said date

# we need to take the difference between the days months and years

# month1 is the current 
# day1 is the current
# year1 is the current 

DayDiff = day1-day2
MonthDiff = month1-month2
YearDiff = year1-year2

print("Days:",DayDiff,"months:",MonthDiff,"Years:",YearDiff)

# curr day 5
# desire day 6
# 11 = 31-5 = 26+6 (count in the desired days plus the days until the next month) = 32

# we do this to get the next month in order to set a value for "month" in the print out, like 3 months until x
if month1 == 1:
    NextMonthOver=SecDay
elif month1 ==2:
    NextMonthOver=ThirDay
elif month1 == 3:
    NextMonthOver=FourDay
elif month1 == 4:
    NextMonthOver = FiveDay
elif month1 == 5: 
    NextMonthOver= SixDay
elif month1 == 6:
    NextMonthOver= SevenDay
elif month1 == 7: 
    NextMonthOver= EightDay
elif month1 == 8: 
    NextMonthOver = NineDay
elif month1 == 9:
    NextMonthOver = TenDay
elif month1 == 10:
    NextMonthOver = ElevDay
elif month1 == 11:
    NextMonthOver = TwelvDay
elif month1 == 12:
    NextMonthOver = FirDay

print("The next month is" ,NextMonthOver, "days long")

# we need to know which months are in between the two if the months are not the same 
howManyMonths = 0

ListOfMonths = []
if month1 != month2:
    if MonthDiff < 0:
        for i in range (MonthDiff*-1):
            howManyMonths+=1
            print(howManyMonths)
            month1 -= 1
            print(month1)
            if month1 == 1 or month1 == -12:
                ListOfMonths.append("FirDay")
            elif month1 == 2 or month1 == -11:
                ListOfMonths.append("SecDay")
            elif month1 == 3 or month1 == -10:
                ListOfMonths.append("ThirDay")
            elif month1 == 4 or month1 == -9:
                ListOfMonths.append("FourDay")
            elif month1 == 5 or month1 == -8:
                ListOfMonths.append("FiveDay")
            elif month1 == 6 or month1 == -7: 
                ListOfMonths.append("SixDay")
            elif month1 == 7 or month1 == -6:
                ListOfMonths.append("SevenDay")
            elif month1 == 8 or month1 == -5: 
                ListOfMonths.append("EightDay")
            elif month1 == 9 or month1 == -4: 
                ListOfMonths.append("NineDay")
            elif month1 == 10 or month1 == -3:
                ListOfMonths.append("TenDay")
            elif month1 == 11 or month1 == -2:
                ListOfMonths.append("ElevDay")
            elif month1 == 12 or month1 == -1:
                ListOfMonths.append("TwelvDay")
            elif month1 == 0:
                ListOfMonths.append("SecDay")
print(ListOfMonths)   
