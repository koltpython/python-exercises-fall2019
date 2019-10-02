print('Welcome to BMI Calculator!')

name=str(input('Please enter your name:'))

#kg
weight=float(input('Hi '+name+ ' ! | Can you enter your weight(in kilograms):'))
#cm
height=float(input('Perfect! | Can you also enter your height(in centimeters):'))
# Calculate BMI [weight(kg)*10000/height(cm)^2]
bmi = weight*10000/(height * height)

print(f'Your BMI is {bmi}')