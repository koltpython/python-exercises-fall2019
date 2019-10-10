print('Welcome to grade statistics calculator')

grade = float(input('The first grade: '))
sum = 0
counter = 0
max = grade
min = grade

while grade >= 0 and grade <= 100:
  sum += grade
  counter += 1
  if max < grade:
    max = grade
  if min > grade:
    min = grade
  grade = float(input('Next grade'))
if (counter > 0): # I dont want to divide by 0!
  print(f'The average is {sum/counter}')
  print (f'The max grade is {max} and the min grade is {min}')
