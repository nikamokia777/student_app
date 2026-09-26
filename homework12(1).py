def fee_decorator(func):
    def wrapper(balance, amount):
        fee = 1
        
        if balance < amount + fee:
            return "error: not enough money on balance"
        
        balance -= fee
        return func(balance, amount)
    
    return wrapper


@fee_decorator
def transaction(balance, amount):
    balance -= amount
    return f"transaction completed: your balance:{balance} gel"


print(transaction(12,6))