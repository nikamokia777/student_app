a = float(input('enter first number'))
b = float(input('enter second number'))
c= float(input('enter third number'))
if a == b:
    print('enter different number')
elif a == c:
    print('enter different number')
elif b == c:
    print('enter different number')
elif a > b and a > c:
    print('biggest number is ' , a)
elif b > a and b > c:
    print('biggest number is ' , b)
elif c > a and c > b:
    print('biggest number is' , c)
