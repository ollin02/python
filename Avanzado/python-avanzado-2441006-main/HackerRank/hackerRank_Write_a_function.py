def is_leap(year):
    leap=False
    if 1900<=year<10**5:
        if year%4==0:
            if year % 100 != 0 or year % 400 == 0:
                leap = True
    return leap

year=int(input("Introduzca el año: "))
print(is_leap(year))