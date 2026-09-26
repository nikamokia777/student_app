try:
    a = float(input('enter first number'))
    b = float(input('enter second number'))
    c = a/b
except ValueError:
    print('error enter only numbers')
except ZeroDivisionError:
    print('error can not divide by zero')
except Exception:
    print('uknown error')
else:
    print('result', c)
finally:
    print('program finished')