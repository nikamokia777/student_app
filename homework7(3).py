import random

list_1 = []
for i in range(-50, 51):   
    list_1.append(i)

print(list_1)

result = random.sample(list_1, 20)
print(result)
even = []
even = []
for x in result:
    if x % 2 == 0:
        even.append(x)

print(even)