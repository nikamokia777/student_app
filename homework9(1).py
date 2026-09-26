def name(sentence):
    count = 0

    for a in sentence:
        if a.isupper():
            count += 1

    print(count)
    print(sentence.upper())
