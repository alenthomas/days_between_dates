def find(d1, m1, y1, d2, m2, y2, count=0):
    if (d1 == d2 and m1 == m2 and y1 == y2):
        return count
    if (y1 == y2 and m1 == m2):
        return find(d1+1, m1, y1, d2, m2, y2, count+1)
    if (y1 == y2):
        days = 30 - d1 + 1
        d1 = 1
        return find(d1, m1+1, y1, d2, m2, y2, count + days)

if __name__ == "__main__":
    print(find(5, 1, 2017, 30, 2, 2017))
