x = 1
while x <= 100:
  keyword = ''
  if x % 3 == 0:
    keyword += 'Fizz'
  if x % 5 == 0:
    keyword += 'Buzz'
  if keyword != '':
    print(keyword)
  else:
    print (x)
  ''' an alternative solution
  if x%15 == 0:
    print('FizzBuzz')
  elif x%3 == 0:
    print('Fizz')
  elif x%5 == 0:
    print('Buzz')
  else:
    print(x)
  '''  
  x += 1
