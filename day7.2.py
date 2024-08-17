#user input 
y = int(input("Input a year: "))
m = int(input("Input a month [1-12]: "))
d = int(input("Input a day [1-31]: "))

if m == 4 or m == 6 or m == 9 or m == 11:
    # 30 day month
    if d >= 1 and d <= 29:
        d = d + 1
    elif d == 30:
        d = 1
        m = m + 1
elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    # 31 day month
    if d >= 1 and d <= 30:
        d = d + 1
    elif d == 31 and m == 12:
        d = 1
        m = 1
        y = y + 1
    elif d == 31 and m != 12:
        d = 1
        m = m + 1
elif m == 2:
    # 28/29 days
    # check if leap year
    if (y % 100 == 0 and y % 400 == 0) or (y % 100 != 0 and y % 4 == 0):
        # leap year
        if d >= 1 and d <= 28:
            d = d + 1
        elif d == 29:
            d = 1
            m = m + 1
    else:
        # non-leap year
        if d >= 1 and d <= 27:
            d = d + 1
        elif d == 28:
            d = 1
            m = m + 1

print("The next date is [yyyy-mm-dd] ", y, "-", m, "-", d)
