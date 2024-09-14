hardness_of_steel = int(input('\nEnter Hardness of Steel: '))
carbon_content_in_steel = float(input('Enter Carbon content in Steel: '))
tensile_strength_of_steel = int(input('Enter Tensile strength of Steel: '))

# Check for invalid input
if hardness_of_steel<=0 or carbon_content_in_steel<=0 or tensile_strength_of_steel<=0:
    print('Invalid input!\nValues must be greater than 0')
    exit(0)

# Condition checks
hardness_check = hardness_of_steel > 60
carbon_check = carbon_content_in_steel < 0.9
tensile_strength_check = tensile_strength_of_steel > 6000

# Determine the grade of steel
grade_of_steel = 0
if hardness_check and carbon_check and tensile_strength_check:
    grade_of_steel = 10
elif hardness_check and carbon_check:
    grade_of_steel = 9
elif carbon_check and tensile_strength_check:
    grade_of_steel = 8

print(f'\nGrade of the Steel: {grade_of_steel}\n')