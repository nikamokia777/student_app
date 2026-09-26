def count_calls(func):
    count = 0
    
    def wrapper():
        nonlocal count
        count += 1
        func()
        return f'function called {count} times'
    
    return wrapper


@count_calls
def next():
    print(input('write something and wait'))


print(next())