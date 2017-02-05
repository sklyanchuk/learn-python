# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#
def isLeapYear(year):
    if year % 4:
        return False
    if year % 100:
        return True
    if year % 400:
        return False
    else:
        return True
def countDaysInYear(year):
    if isLeapYear(year):
        return 366
    return 365

def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    days = day2 - day1

    def countDaysInMonth(month1, month2):
        daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = sum(daysOfMonths[month1-1:month2-1])
        return days
    days_in_months = countDaysInMonth(month1, month2)

    def countDaysInYears(year1, year2):
        i = year1
        days = 0
        while i < year2:
            days = days + countDaysInYear(i)
            i = i + 1
        if isLeapYear(year2) and month2 > 2:
                days = days + 1
        return days
    days_in_years = countDaysInYears(year1, year2)

    sum_days = days_in_years + days_in_months + days
    print "Sum days: " + str(sum_days)
    return sum_days

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
