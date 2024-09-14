marks = int(input('Enter marks obtained: '))
grade = ''

if marks<0:
    print('Invalid marks entered!\nMarks should be greater than 0.')
    exit(0)
elif marks<50:
    grade = 'F'
elif marks<55:
    grade = 'E'
elif marks<60:
    grade = 'D'
elif marks<70:
    grade = 'C'
elif marks<80:
    grade = 'B'
elif marks<90:
    grade = 'A'
elif marks<=100:
    grade = 'S'
else:
    print('Invalid marks entered!\nMarks should be less than 100.')
    exit(0)

print(f'{grade} Grade obtained for scoring {marks} Marks')