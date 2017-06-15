import calendar
import time

_leap_months = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31,
                9:30, 10:31, 11:30, 12:31}
_months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31,
           9:30, 10:31, 11:30, 12:31}

def days_in_month(month, year):
    if calendar.isleap(year):
        return _leap_months[month]
    else:
        return _months[month]

def total_months(m1, y1, m2, y2):
    years = y2 - y1
    first, last = 12 - m1, 12 - m2
    rest = years * 12
    return [m1+1, first - last + rest - 1]

def days_bw_dates(d1=14, m1=1, y1=2016, d2=28, m2=4, y2=2017):
    total, count = 0, 0
    initial_month_days = days_in_month(m1, y1)
    initial_month_days = initial_month_days - d1
    if (y1 == y2 and m1 == m2):
        return d2 - d1
    month, no_months = total_months(m1, y1, m2, y2)
    for i in range(1, no_months+1):
        count = count+1
        if month>12:
            month = month-12
            y1+=1
        total += days_in_month(month, y1)
        month +=1
    return initial_month_days + total + d2

if __name__ == "__main__":
    start_time = time.time()
    print("days:", days_bw_dates(5, 5, 2017, 14, 6, 2017))
    print("days:", days_bw_dates(23, 4, 2017, 24, 8, 2017))
    print("days:", days_bw_dates(26, 8, 1993, 11, 1, 2021))
    print("days:", days_bw_dates(26, 8, 1993, 15, 6, 2017))
    print("days:", days_bw_dates())
    print("avg time: {:.6f}".format(time.time() - start_time))
