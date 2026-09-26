def numbers(*args):
    args = [int(x) for x in args]   
    even = []
    odd = []

    for i in args:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return odd, even

