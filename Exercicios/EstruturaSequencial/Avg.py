numbers = input('Type four school grades: ').split()
gradeOne, gradeTwo, gradeThree, gradeFour = list(map(int, numbers))
avg = (gradeOne + gradeTwo + gradeThree + gradeFour) / 4
print('Average:', avg)