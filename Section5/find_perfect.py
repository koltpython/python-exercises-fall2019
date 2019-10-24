print("This program finds the perfect numbers between 1 and 10000.")

def is_perfect(n):
    """ returns boolean that is given number perfect or not. """
     ## Your code starts here
     # Hint: you may want to use sum_of_proper_divisors function
    return sum_of_proper_divisors(n) == n
    ## Your code ends here
        
def sum_of_proper_divisors(n):
    """ Returns the sum of proper divisors of the given number excluding itself."""
    ## Your code starts here
    sum = 1 
    for div in range(2, n):
      if n%div == 0:
        sum += div
    return sum
    ## Your code ends here

for i in range(1, 10000):
    if is_perfect(i):
        print(i)


