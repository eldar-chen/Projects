import random

QandA = [
    'What is the capital of England? ', 'london', #1
    'What is the capital of France? ', 'paris', #2
    'What is the capital of Greece? ', 'athens', #3
    'Who is Bobo? ', 'a good boy', #4
    'Is Yui a good girl? ', 'no', #5
    'What is the capital of Taiwan? ', 'taipei', #6
    'What is the capital of Lithuania? ', 'vilnius', #7
    'What is the capital of the Philippines ', 'Manila', #8
]

points = 0

repeat = input("Do you want to play? (yes/no) ")

while repeat.lower() == "yes":
    # Extract only the questions from the QandA list
    questions = QandA[::2]
    random.shuffle(questions)  # Shuffle the list of questions

    current = 0
    quiz = 1

    while quiz < 9:
        question = input(questions[current])

        # Find the corresponding answer index for the asked question
        answer_index = QandA.index(questions[current]) + 1

        if question.lower() == QandA[answer_index].lower():
            print("That's correct!")
            points += 1
        else:
            print("Sorry, that's wrong!")

        current += 1
        quiz += 1 

    print("Well done! Your score is:", points, "points")
    repeat = input("Do you want to play? (yes/no) ")

print("Thank you for playing! See you next time.")