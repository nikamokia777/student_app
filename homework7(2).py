list2= ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
result=[]
for char in list2:
    if list2.count(char) == 1:
        result.append(char)
print(result)