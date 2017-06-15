import calendar

_leap_months = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31,
                9:30, 10:31, 11:30, 12:31}
_months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31,
           9:30, 10:31, 11:30, 12:31}

def is_leap_year(year):
    return calendar.isleap(year)

def days_in_month(month, year):
    if is_leap_year(year):
        return _leap_months[month]
    else:
        return _months[month]

def find(d1, m1, y1, d2, m2, y2, count=0):
    if (y1 == y2 and m1 == m2):
        return count + d2 - d1
    count = count + days_in_month(m1, y1) - d1 + 1
    d1 = 1
    if (m1 == 12):
        y1 = y1 + 1
        m1 = 1
    else:
        m1 = m1 + 1
    return find(d1, m1, y1, d2, m2, y2, count)


if __name__ == "__main__":
    print(find(5, 1, 2017, 30, 1, 2017))
    print(find(26, 8, 1993, 15, 6, 2017))
