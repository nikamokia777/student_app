import math
a = int(input("enter length of a leg:"))
b = int(input('enter lenght of second leg:'))
hypotenuse=math.sqrt(a**2+b**2)
area = (a*b)/2
print('Hypotenuse', hypotenuse)
print('Area', area)