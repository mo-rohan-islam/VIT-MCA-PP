# Define the slab ranges and rate 
slabs = [
    (100, 1.2),     # First 100 units @ Rs. 1.2/unit    --- upto 100
    (100, 2.6),     # Next 100 units @ Rs. 2.6/unit     --- 101 to 200
    (100, 4.2),     # Next 100 units @ Rs. 4.2/unit     --- 201 to 300
    (200, 5.7),     # Next 200 units @ Rs. 5.7/unit     --- 301 to 500
    (500, 7.0)      # Next 599 units @ Rs. 7.0/unit     --- 501 to 1000
]

last_slab_rate = 8.5    # Rate beyond 1000 units consumed

# Input electricity units consumed
units_consumed = int(input('Enter units consumed: '))

# Check for invalid input
if units_consumed<0:
    print('Invalid input!\nUnits consumed should be greater than 0')
    exit(0)

remaining_units = units_consumed
gross_bill = 0.0

# Calculate gross electricity bill based on slab rates
for slab, rate in slabs:
    if remaining_units > slab:
        gross_bill += slab*rate
        remaining_units -= slab
    else:
        gross_bill += remaining_units*rate
        remaining_units = 0
        break

# If units consumed exceeds 1000 units
if remaining_units > 0:
    gross_bill += remaining_units*last_slab_rate

# Calculate service tax of 12%
service_tax = gross_bill*.12
net_bill = gross_bill + service_tax

# Output the electricity bill
print(f'The Electricity bill for {units_consumed} units consumed is Rs. {net_bill:.2f}.')