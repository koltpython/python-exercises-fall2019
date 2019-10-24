def gcd(a, b):
  # elegant solution
  remainder = a%b 
  while remainder > 0:
    a = b
    b = remainder
    remainder = a%b 
  return remainder
  
  #a brute force approach
  gcd = 1
  possible_divisor = 2
  while a > 1 and b > 1:
    while a%possible_divisor == 0 and b%possible_divisor == 0:
      gcd *= possible_divisor
      a /= possible_divisor
      b /= possible_divisor
    while a% possible_divisor == 0:
      a/= possible_divisor
    while b % possible_divisor == 0:
      b /= possible_divisor
    possible_divisor += 1
  return gcd

def lcm(a, b):
  return a*b/gcd(a, b)
  
while True:
 a = int(input("a: "))
 b = int(input("b: "))
 
 print(f'gcd of {a} and {b} is {gcd(a, b)}')
 print(f'lcm of {a} and {b} is {lcm(a,b)}')
