units = int(input('Enter electricity units consumed: '))
gross_bill = 0.0

# Check for invalid input
if units<0:
    print('Invalid input!\nUnits consumed must be greater than 0')
    exit(0)

# Bill calculation based on the slab
if units<=100:
    gross_bill = units*1.2
elif units<=200:
    gross_bill = 100*1.2 + (units-100)*2.6
elif units<=300:
    gross_bill = 100*1.2 + 100*2.6 + (units-200)*4.2
elif units<=500:
    gross_bill = 100*1.2 + 100*2.6 + 100*4.2 + (units-300)*5.7
elif units<=1000:
    gross_bill = 100*1.2 + 100*2.6 + 100*4.2 + 200*5.7 + (units-500)*7.0
else:
    gross_bill = 100*1.2 + 100*2.6 + 100*4.2 + 200*5.7 + 500*7.0 + (units-1000)*8.5

# Adding 12% service tax
tax = gross_bill*12/100
net_bill = gross_bill + tax

# Output the final bill
print(f'The electricity bill for {units} units consumed is Rs. {net_bill:.2f}.')
