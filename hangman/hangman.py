#!/usr/bin/python3

import random

# Words to choose from
words = ['javascript', 'python', 'java', 'ruby', 'swift', 'kotlin']
# Choose the word
chosen_word = random.choice(words)
# Display the word
word_display = ['_' for _ in chosen_word] # list comprehension
# Attempts
attempts = 8

print("Welcome to the Hangman Game! Have Fun!")

while attempts > 0 and '_' in word_display:
    print(f"\n{' '.join(word_display)}")
    # Player's guess
    guess = input("Guess a letter: ").lower()
    # Check if the guessed letter is part of the chosen word
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess # reveal the letter

    else:
        print("Sorry! That letter doesn't appear in the chosen word!")
        attempts -= 1

# Conclusion
if '_' not in word_display:
    print("\nYou guessed the word")
    print(' '.join(word_display))
    print("You won!")
else:
    print(f"You ran out of attempts. The word was : {chosen_word}.")
    print("You lost!")


