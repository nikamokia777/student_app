fruits = {}
while True:
    a = input('enter fruit: ')
    
    if a == 'stop':
        break
    if a in fruits:
        fruits[a]+= 1
    else:
        fruits[a]= 1
print(fruits)