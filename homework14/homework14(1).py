count  = 1
with open('names txt', 'a') as file:


    while True:
        firstname = input('enter your name:')
        if firstname == 'stop':
            break
        lastname = input('enter your last name')

        file.write(f'{count}. {firstname} {lastname}\n')
        count += 1