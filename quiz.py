def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit Game")

    option = input("Enter option ")
    return option
    
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
            print("You selected 'Ask questions'")
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("invalid option")
        print("")

game_loop()