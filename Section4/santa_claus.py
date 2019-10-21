while True:
  isPrime = True
  age = int(input("Yes kiddo: "))
  if age <= 0:
    break 
  
  for i in range(2, int(age/2)):
    if age % i == 0:
      isPrime=False
      break
  if isPrime:
    print('There you go')
  else:
    print('Sorry, kid')
