print('Hi, Ceren! I am here to help you.')
shape = input('Please tell me whether you want to work with a triangle or a quadrilateral')
if (shape == "triangle"):
  print ('Give me 3 edges')
  a = int(input('Edge 1:'))
  b = int(input('Edge 2:'))
  c = int(input('Edge 3:'))
  # your code here
  # is the triangle valid?
  if (not ((abs(a-c) < b and b < a+c) and (abs(a-b) < c and c < a+b))):
    print('Sorry Ceren, this is an invalid triangle')
  else:
    # equilateral
    if (a == b and a == c):
      print('Equilateral')
    elif (a == b or a == c or b == c):
      print('Isosceles')
    else:
      print('Ordinary triangle')
  
elif (shape == "quadrilateral"):
  print ('Give me 4 edges in order')
  a = int(input('Edge 1:'))
  b = int(input('Edge 2:'))
  c = int(input('Edge 3:'))
  d = int(input('Edge 4:'))
  # your code here
  # all edges equal 
  if (a == b and a == c and a == d):
    print('square')
  elif (a == c and b == d):
    print('rectangle')
  else:
    print('ordinary quadrilateral')
else:
  print("Sorry Ceren, I don't recognize this shape.")
