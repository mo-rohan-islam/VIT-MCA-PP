year = int(input('Enter a year: '))
leap_year = False
if year%4==0:
    if year%100!=0:
        leap_year = True
    elif year%400==0:
            leap_year = True
print(f'{year} is a Leap year? {leap_year}')