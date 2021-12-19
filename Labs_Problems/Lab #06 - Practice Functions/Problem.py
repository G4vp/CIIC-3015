# Write a function called Span() which takes six integer arguments (start_year, start_month, start_day, end_year, end_month, end_day) that represent two dates. Return the number of days separating those two dates. Assume the Gregorian calendar to be perfectly regular for all positive years.

# Years are any value above zero.
# Months are specified as we usually see them, with January=1 and December=12.
# Days range from 1 to 31, depending on the month and year.
# Leap years are a thing.

# This problem can be tricky! While it is certainly possible to solve it with a small number of relatively simple Python statements, finding a correct solution is going to require a lot of precision in both reasoning and implementation. There may be many frustrating, failed attempts which are only off by a day or two. Keep at it.

# Also, unlike other lab problems so far, this one awards partial credit! The more test cases you can solve, the more points you will score. However, DO NOT use hardwired answers to fool the tester. We will be inspecting all solutions manually and any which try to game the system in this manner will receive a score of zero.

# And no, you may NOT import any date/time libraries to do the work for you.

def YearsToDays(start_year,end_year):
    days = 0
    for i in range(start_year,end_year):
        if(IsLeapYear(i)):
            days += 366
        else:
            days += 365
    return days

def MonthToDays(year,Month):
    Days = -1
    
    x = (31,28,31,30,31,30,31,31,30,31,30,31)
    for i in range(Month-1):
        Days+= x[i]
    if(IsLeapYear(year)):
        return 366-Days
    return 365-Days

def IsLeapYear(year):
    if year%4 == 0 and year%400 == 0 and year%100 == 0:
        return True
    elif year%4 == 0 and year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    return False

def Span(start_year,start_month,start_day,end_year,end_month,end_day):
    Start = MonthToDays(start_year,start_month)-start_day
    End = MonthToDays(end_year,end_month)-end_day
    if(IsLeapYear(start_year)):
        if(end_month > 2 or end_month == 2 and end_day > 28):
            End += 2
        if(start_month < 2 or start_month == 2 and end_day < 28):
            End += 1
    if(IsLeapYear(end_year)):
        End = 366 - End
        if(end_month > 2 or end_month == 2 and end_day > 28):
            End += 1
        if(start_month < 2 or start_month == 2 and end_day < 28):
            End += 2
    else:
        End = 365 - End
    
    
    total = (Start + End) + YearsToDays(start_year,end_year)
    return total  - 365