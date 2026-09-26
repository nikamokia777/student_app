import random
secretnum =random.randint(1,100)
lives = 5
while lives > 0:
    guess=int(input('enter number'))

    if guess == secretnum:
        print('you won')
        break
    lives -= 1
    if guess < secretnum:
        print('your number is lower')
    if guess > secretnum:
        print('your number is higher')
    print('lives left', lives)
    if lives == 0:
        print('you lost')
        print('number was', secretnum)