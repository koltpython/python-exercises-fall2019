# ValueError, ask for input until the user enters a valid number
while True:
  try:
    a = float(input("Performance of CPUA:"))
    break
  except ValueError as valError:
    print("Value Error ", valError)
while True:
  try:
    b = float(input("Performance of CPUB:"))
    # Be careful when dividing, make sure that you don't divide by zero
    # If you don't have control over the input make sure you protect you program
    performance_rate = a/b
    print(f"A's performance is {performance_rate}*B's.")
    break
  except ValueError as valError:
    print("Value Error, enter a float or an integer.", valError)
  except ZeroDivisionError:
    print("Oh no b shouldn't be 0")
 

# NameError occurs when you try to call an unresolved variable
try:  
  print(f'I have been living here for {years} years')
except NameError as name_error:
  print(f"Something unknown, {name_error}")
  
try:
  faculties = ["Case", "Ce", "Cs", "Ssch", "Med"]
  faculties_tuple = ("Case", "Ce", "Cs", "Ssch", "Med")
  index = int(input(f'These are the faculties {faculties} which index do you want to use?'))
  print(f'You chose {faculties[index]}')
  faculties_tuple[2] = "Nursing"
except IndexError:
  print(f'KU hopes to open more faculties in the future')
except TypeError as type_error:
    print(f'Be careful with tuples, {type_error}')

try:
  print(2 + '2')
except TypeError:
  print('Invalid types')
# Oh no, they also attacked inside our program


while True:
    print("Hahahaha")
    break