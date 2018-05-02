def leapCheck(year):
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap = True
    if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        leap = False

    return(leap)

year = int(input())
leapCheck(year)
