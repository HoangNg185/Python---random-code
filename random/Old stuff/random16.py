import random

nums = list(range(1, 101))
guess = random.randint(1, 100)


def guessinggame():
    while True:
        myguess = int(input('ur guess is: '))
        if myguess < guess:
            print('higher')
        elif myguess > guess:
            print('lower')
        else:
            print('that right, ur number is correct')
            break


guessinggame()
