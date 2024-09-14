units_consumed = int(input('Enter number of units consumed: '))
bill = 0.0

if units_consumed<0:
    print('Invalid input! Please try again...')
    exit(0)
elif units_consumed<=100:
    # First 100 units are free (no charge)
    bill = 0
elif units_consumed<=200:
    # First 100 units are free, then 1.5/unit for next 100 units
    bill = (units_consumed-100)*1.5
elif units_consumed<=500:
    # First 100 units are free, next 100 units at 2/unit, remaining at 3/unit
    bill = 100*2 + (units_consumed-200)*3
else:
    # First 100 units free, next 100 at 3.5/unit, next 300 at 4.6/unit, remaining at 6.6/unit
    bill = 100*3.5 + 300*4.6 + (units_consumed-500)*6.6

print(f'Electricity bill is Rs. {bill} for {units_consumed} units consumed')
