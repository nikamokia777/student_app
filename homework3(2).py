text = input('write a sentence')
words=text.split()
longest= max(words, key=len)
print(longest)