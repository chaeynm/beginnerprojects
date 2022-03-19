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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low!= high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high bc low = high

        feedback = input(f'is guess {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'yay! the computer guessed your number, {guess}, correctly!')

computer_guess(9999)



