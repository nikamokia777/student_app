def number(n):
    if n == 1 or n == 0:
        return 1
    return n + number(n-1)
print(number(6))
