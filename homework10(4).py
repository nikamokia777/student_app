products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]
higherthan100 = list(filter(lambda product: product["price"] >= 100, products))

print(higherthan100)

namesprices = list(map(lambda product: (product["name"], product["price"]), products))

print(namesprices)

sortbyprices = sorted(products, key= lambda product: (product['price']))
print(sortbyprices) 

from functools import reduce
total = reduce(lambda a,b: a+b['price'],products, 0 )
print(total)
