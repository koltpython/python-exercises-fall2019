a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

# print the maximum
# max = a
if ((a >= b) and (a >= c)): 
  mx = a
# max = b
elif ((b >= a) and (b >= c)):
  mx = b
# max = c
else:
  mx = c
print(mx)
