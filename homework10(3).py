def sentence(text):
    amount = {}

    text = text.lower()
    words = text.split()

    for word in words:
        if word in amount:
            amount[word] += 1
        else:
            amount[word] = 1

    return amount


