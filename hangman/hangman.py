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

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    # Player's guess
    guess = input("Guess a letter: ").lower()
    # Check if the guessed letter is part of the chosen word
    if attempts > 0 and '_' in word_display:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess # reveal the letter

    else:
        print("Sorry! That letter doesn't appear in the chosen word!")
        attempts -= 1

# Conclusion
if '_' not in word_display:
    print("You guessed the word")
    print(' '.join(word_display))
    print("You won!")
else:
    print(f"You ran out of attempts. The word was : {chosen_word}.")
    print("You lost!")


# # List of words to guess
# words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']

# # Randomly choose a word from the list
# chosen_word = random.choice(words)
# word_display = ['_' for _ in chosen_word]  # Create a list of underscores
# attempts = 8  # Number of allowed attempts

# print("Welcome to Hangman!")

# while attempts > 0 and '_' in word_display:
#     print("\n" + ' '.join(word_display))
#     guess = input("Guess a letter: ").lower()

#     # Check if the guessed letter is in the chosen word
#     if guess in chosen_word:
#         for index, letter in enumerate(chosen_word):
#             if letter == guess:
#                 word_display[index] = guess  # Reveal the letter
#     else:
#         print("That letter doesn't appear in the word.")
#         attempts -= 1

#     # Check for repeated guesses or invalid input
#     # Note: This simple version does not handle repeated guesses or validate input.
#     # Consider adding these features for a more complete game experience.

# # Game conclusion
# if '_' not in word_display:
#     print("You guessed the word!")
#     print(' '.join(word_display))
#     print("You survived!")
# else:
#     print("You ran out of attempts. The word was: " + chosen_word)
#     print("You lost!")