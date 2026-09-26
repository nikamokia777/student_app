a = float(input('Enter your weight in kg: '))
b = float(input('Enter your height in meters: '))

bmi = a / b**2

if bmi < 19:
    print('You are underweight')
elif bmi < 25:
    print('You are normal weight')
else:
    print('You are overweight')