products = [
    {"cola": {
        "price": 1.5,
        "quantity": 10
    }},
    {"fanta": {
        "price": 2.5,
        "quantity": 5
    }},
    {"snickers": {
        "price": 3.5,
        "quantity": 12
    }},
    {"water": {
        "price": 4.5,
        "quantity": 8
    }},
    {"beer": {
        "price": 6.5,
        "quantity": 5
    }}
]
for i in products:
    for name in i:
        print(name)



total = 0

for product in products:
    for name in product:
        price = product[name]["price"]
        quantity = product[name]["quantity"]
        total += price * quantity
print(total)