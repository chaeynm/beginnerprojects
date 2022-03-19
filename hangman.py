#author credits to kylie ying

import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the words list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        # letters used
        # .join(used_letters) ['a', 'b', 'cd'] --> 'a b cd'
        print('you\'ve used these letters: ',' '.join(used_letters))

        #what current word is (ie. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        print('you have used these letters')
        user_letter = input('guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('you already used that word')
        else:
            print('invalid word or doesnt exist in this dictionary')

if __name__ == '__main__':
    hangman()