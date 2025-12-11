from numpy import random 
import hangmanart as hangman

tech = ['python', 'java','javascript', 'ruby', 'html', 'css', 'react', 'angular']
fruits = ['apple', 'banana', 'orange', 'grape', 'mango', 'peach', 'pear', 'kiwi']
animals = ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'monkey', 'panda', 'kangaroo']
categories = {'tech': tech, 'fruits': fruits, 'animals': animals}

def get_random_word():
    user_choice = input("Choose a category (tech, fruits, animals): ").lower()
    while user_choice not in categories:
        user_choice = input("Invalid category. Please choose from (tech, fruits, animals): ").lower()
    return random.choice(categories[user_choice])


def word_guess():
    word = get_random_word()
    word_length = len(word)
    guessed = ['_'] * word_length
    attempts = 6
    print(f"\nThe word has {word_length} letters")
    print(  ' '.join(guessed))
    while attempts > 0 and '_' in guessed:
        guess = input("\nGuess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("\nPlease enter a valid alphabetical character.")
            continue
        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed[index] = guess
            print("\nCORRECT GUESS!")
        else:
            attempts -= 1
            print(f"\nWRONG GUESS! You have {attempts} attempts left.")
            hangman_stage = hangman.hangman_art[6 - attempts]
            for line in hangman_stage:
                print(line)
        print(' '.join(guessed))
        
    if '_' not in guessed:
        print(f"CONGRATULATIONS! \nYou've guessed the word: {word}")
    else:
        print(f"Sorry, you've run out of attempts. \nThe word was: {word}")

word_guess()

