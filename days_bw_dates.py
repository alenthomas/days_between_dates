import datetime as dt
import calendar

_leap_months = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31,
                9:30, 10:31, 11:30, 12:31}
_months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31,
           9:30, 10:31, 11:30, 12:31}

d1, m1, y1 = map(int, input().split(' '))
d2, m2, y2 = map(int, input().split(' '))

# initial, final = dt.date(y1, m1, d1), dt.date(y2, m2, d2)

# print("days :", (final-initial).days)

def is_leap_year(year):
    return calendar.isleap(year)

def days_in_month(month, is_leap):
    if is_leap:
        return _leap_months[month]
    else:
        return _months[month]

def total_months(m1, y1, m2, y2):
    """excluding m1 and m2
    """
    years = y2 - y1
    first = 12 - m1
    last = 12 - m2
    rest = years * 12
    return [m1+1, first - last + rest - 1]

def days_bw_dates(d1=14, m1=1, y1=2016, d2=28, m2=4, y2=2017): # delta 470
    total = 0

    # calculate days in first month
    initial_month_days = days_in_month(m1, is_leap_year(y1))
    initial_month_days = initial_month_days - d1
    if (y1 == y2 and m1 == m2):
        return d2 - d1

    # calculate days in rest_of_the_months
    month, no_months = total_months(m1, y1, m2, y2)
    for i in range(1, no_months+1):
        if month>12:
            month = month-12
            y1+=1
        total += days_in_month(month, is_leap_year(y1))
        month +=1

    # calculate days in last month ie d2
    return initial_month_days + total + d2

if __name__ == "__main__":
    #print(days_bw_dates(5, 5, 2017, 14, 6, 2017))
    #print(days_bw_dates(23, 4, 2017, 24, 8, 2017))
    print("no of days: ", days_bw_dates(d1, m1, y1, d2, m2, y2))
    #print(days_bw_dates())
