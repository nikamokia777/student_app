price = 50
while price > 0:
    print('you need to pay', price, 'gel' )
    bill = int(input('input bill(5, 10, 20)'))
    if bill not in [5, 10 ,20]:
        print('please enter valid bill')
        continue

    price -= bill
    print('payement completed')
    if price < 0:
        print('you get a change of', -price, 'gel')
    else:
        print('no change')
    
    