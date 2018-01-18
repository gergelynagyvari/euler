# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def getNumberOfDays(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if year % 400 == 0:
            return 29
        elif year % 100 == 0:
            return 28
        elif year % 4 == 0:
            return 29
        else:
            return 28
    else:
        print 'What?'




def main():
    totalSundays = 0
    weekday = 6

    for year in range(1900, 2001):
        for month in range(1, 13):
            for day in range(1, getNumberOfDays(year, month) + 1):
                weekday = (weekday + 1) % 7
                if year > 1900 and day == 1 and weekday == 6:
                    totalSundays += 1
                    print('{}. {}. {} is a Sunday'.format(year, month, day))

    print('Last {}. {}. {}'.format(year, month, day))
    print(totalSundays)

if __name__ == '__main__':
    main()
