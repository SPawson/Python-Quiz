def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit Game")

    option = input("Enter option ")
    return option
    
def ask_question():
    questions = []
    answers = []
    
    with open("quiz/questions.txt") as file:
        lines = file.read().splitlines()
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
    
    number_of_questions = len(questions)
    questions_and_answers  = zip(questions, answers)
    
    score = 0
    
    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        
        if guess == answer:
            score += 1
            print("Well done, that was correct!")
            print(score)
        else:
            print("That was the wrong answer")
    print("You got {0} correct, out of {1}".format(score,number_of_questions))
        
        
def add_question():
    print("")
    question = input("Enter a question\n :> ")
    print("")
    print("Please tell me the answer to the question")
    answer = input("{0}\n:>".format(question))
    
    file = open("quiz/questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

def game_loop():
    while True:
        option = show_menu()
        
        if option == "1":
            ask_question()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("invalid option")
        print("")

game_loop()