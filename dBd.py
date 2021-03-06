import calendar
import time

_months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31,
           9:30, 10:31, 11:30, 12:31}

def days_in_month(month, year, leap=False):
    if month == 2:
        if calendar.isleap(year):
            return 29
    return _months[month]

def find(d1, m1, y1, d2, m2, y2, count=0):
    if (y1 == y2 and m1 == m2):
        return count + d2 - d1
    count += days_in_month(m1, y1) - d1 + 1
    if (m1 == 12):
        y1 += 1
        m1 = 1
    else:
        m1 += 1
    return find(1, m1, y1, d2, m2, y2, count)

if __name__ == "__main__":
    start_time = time.time()
    print("days:", find(5, 5, 2017, 14, 6, 2017))
    print("days:", find(23, 4, 2017, 24, 8, 2017))
    print("days:", find(26, 8, 1993, 11, 1, 2021))
    print("days:", find(26, 8, 1993, 15, 6, 2017))
    print("days:", find(24, 11, 1986, 21, 9, 2017))
    print("avg time: {:.6f}".format(time.time() - start_time))
