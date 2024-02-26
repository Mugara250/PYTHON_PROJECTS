#!/usr/bin/python3

questions = [
    {
        'question' : 'What is the capital city of Gabon?',
        'options' : ['A. Gaborone', 'B. Yamoussokro', 'C. Douala', 'D. Libreville'],
        'correct_answer': 'D'
    },
    {
        'question' : 'Who was the first European explorer to arrive in Rwanda?',
        'options' : ['A. David Livingstone', 'B. Mungo Park', 'C. Christopher Columbus', 'D. Oscar Bourman'],
        'correct_answer' : 'D'
    },
    {
        'question' : 'Where are the headquarters of the United Nations?',
        'options' : ['A. Addis Ababa', 'B. New York', 'C. The Hague', 'D. Geneva'],
        'correct_answer' : 'B'
    },
    {
        'question' : 'When did the second world war end?',
        'options' : ['A. 1936', 'B. 1939', 'C. 1945', 'D. 1948'],
        'correct_answer' : 'C'
    },
    {
        'question' : 'Which country colonised Equatorial Guinea?',
        'options' : ['A. Spain', 'B. Britain', 'C. Portugal', 'D. Belgium'],
        'correct_answer' : 'A'
    },
]

print("Welcome to our quiz game! Have fun!")
def run_quiz():
    """ A quiz game that asks users questions while tracking their score """
    score = 0 # Track the score
    for question in questions:
        print(f"\n{question['question']}")
        for option in question['options']:
            print(option)
        answer = input('Enter the correct answer among A, B, C, D (Enter "q" to quit): ')
        # Quitting the quiz
        if answer == 'q':
            break
        # Compare the user's answer with the correct answer
        elif answer.upper() == question['correct_answer']:
            print("You got it correct!")
            score += 1
        else:
            print(f"Oops! You got it wrong! The correct answer is {question['correct_answer']}.")
    
    percentage = int((score)/len(questions) * 100)
    print(f"\nYou got {score} answers correct out of {len(questions)} questions ({percentage}%).\nYou can try again if you want to increase your score.")

run_quiz()