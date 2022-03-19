import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_number:
                print('guess again too low')
            elif guess < random_number:
                print('guess again too high')
        except ValueError:
            print("pls type in a number")

    print(f'yay! congrats u have guessed the number {random_number}')
guess(10)

