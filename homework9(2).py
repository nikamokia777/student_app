def word(camel_case):
    result = ''
    for a in camel_case:
        if a.isupper():
            result += '_' + a.lower()
        else:
            result += a
    return result


