#!/usr/bin/python3

import random

words = [
    {"french": "bonjour", "english": "hello"},
    {"french": "merci", "english": "thank you"},
    {"french": "au revoir", "english": "goodbye"},
    {"french": "s'il vous plaît", "english": "please"},
    {"french": "excusez-moi", "english": "excuse me"},
    {"french": "pardon", "english": "sorry"},
    {"french": "oui", "english": "yes"},
    {"french": "non", "english": "no"},
    {"french": "comment ça va", "english": "how are you"},
    {"french": "ça va bien", "english": "I'm fine"},
    {"french": "je t'aime", "english": "I love you"},
    {"french": "merde", "english": "shit"},
    {"french": "bienvenue", "english": "welcome"},
    {"french": "de rien", "english": "you're welcome"},
    {"french": "c'est la vie", "english": "that's life"},
    {"french": "ça marche", "english": "it works"},
    {"french": "à bientôt", "english": "see you soon"},
    {"french": "pas de problème", "english": "no problem"},
    {"french": "je suis désolé", "english": "I'm sorry"},
    {"french": "excuse-moi", "english": "excuse me"},
    {"french": "qu'est-ce que c'est", "english": "what is it"},
    {"french": "comment tu t'appelles", "english": "what's your name"},
    {"french": "j'ai faim", "english": "I'm hungry"},
    {"french": "j'ai soif", "english": "I'm thirsty"},
    {"french": "je ne sais pas", "english": "I don't know"},
    {"french": "il pleut", "english": "it's raining"},
    {"french": "il fait chaud", "english": "it's hot"},
    {"french": "il fait froid", "english": "it's cold"},
    {"french": "il est tard", "english": "it's late"},
    {"french": "c'est bon", "english": "it's good"},
    {"french": "c'est beau", "english": "it's beautiful"},
    {"french": "c'est drôle", "english": "it's funny"},
    {"french": "c'est facile", "english": "it's easy"},
    {"french": "c'est difficile", "english": "it's difficult"},
    {"french": "c'est important", "english": "it's important"},
    {"french": "c'est vrai", "english": "it's true"},
    {"french": "c'est faux", "english": "it's false"},
    {"french": "c'est cher", "english": "it's expensive"},
    {"french": "c'est gratuit", "english": "it's free"},
    {"french": "c'est bien", "english": "it's good"},
    {"french": "c'est mauvais", "english": "it's bad"},
    {"french": "c'est étrange", "english": "it's strange"},
    {"french": "c'est normal", "english": "it's normal"},
    {"french": "c'est possible", "english": "it's possible"},
    {"french": "c'est impossible", "english": "it's impossible"},
    {"french": "c'est différent", "english": "it's different"},
    {"french": "c'est pareil", "english": "it's the same"},
    {"french": "c'est mieux", "english": "it's better"},
    {"french": "c'est pire", "english": "it's worse"},
    {"french": "c'est grand", "english": "it's big"},
    {"french": "c'est petit", "english": "it's small"},
    {"french": "c'est rapide", "english": "it's fast"},
    {"french": "c'est lent", "english": "it's slow"},
    {"french": "c'est fort", "english": "it's loud"},
    {"french": "c'est doux", "english": "it's soft"},
    {"french": "c'est dur", "english": "it's hard"},
    {"french": "c'est beau", "english": "it's beautiful"},
    {"french": "c'est laid", "english": "it's ugly"},
    {"french": "c'est chaud", "english": "it's hot"},
    {"french": "c'est froid", "english": "it's cold"},
    {"french": "c'est long", "english": "it's long"},
    {"french": "c'est court", "english": "it's short"},
    {"french": "c'est haut", "english": "it's high"},
    {"french": "c'est bas", "english": "it's low"},
    {"french": "c'est profond", "english": "it's deep"},
    {"french": "c'est superficiel", "english": "it's shallow"},
    {"french": "c'est propre", "english": "it's clean"},
    {"french": "c'est sale", "english": "it's dirty"},
    {"french": "c'est sec", "english": "it's dry"},
    {"french": "c'est mouillé", "english": "it's wet"},
    {"french": "c'est clair", "english": "it's clear"},
    {"french": "c'est sombre", "english": "it's dark"},
    {"french": "c'est fort", "english": "it's strong"},
    {"french": "c'est faible", "english": "it's weak"},
    {"french": "c'est simple", "english": "it's simple"},
    {"french": "c'est complexe", "english": "it's complex"},
    {"french": "c'est léger", "english": "it's light"},
    {"french": "c'est lourd", "english": "it's heavy"},
    {"french": "c'est vide", "english": "it's empty"},
    {"french": "c'est plein", "english": "it's full"},
    {"french": "c'est neuf", "english": "it's new"},
    {"french": "c'est vieux", "english": "it's old"},
    {"french": "c'est moderne", "english": "it's modern"},
    {"french": "c'est traditionnel", "english": "it's traditional"},
    {"french": "c'est tranquille", "english": "it's quiet"},
    {"french": "c'est bruyant", "english": "it's noisy"},
    {"french": "c'est confortable", "english": "it's comfortable"},
    {"french": "c'est inconfortable", "english": "it's uncomfortable"},
    {"french": "c'est facile", "english": "it's easy"},
    {"french": "c'est difficile", "english": "it's difficult"}
]

def quiz_user():
    random.shuffle(words)
    score = 0

    for word in words:
        answer = input(f"What is the correct English translation of the word {word['french']}?\n(Enter 'q' to quit) ")
        correct_answer = word['english']

        if answer == 'q':
            break
        elif answer == correct_answer:
            print(f"Correct!{answer} is the correct English translation of {word['french']}.")
            score += 1
        else:
            print(f"Wrong!The correct English translation of {word['french']} is {correct_answer}.")
    
    # print(f"Your score is {score}/{len(words)}.")

def main():
    print("Welcome to the Language Learning App! Enjoy!")
    print(input("Press Enter to start learning..."))
    quiz_user()

if __name__ == '__main__':
    main()