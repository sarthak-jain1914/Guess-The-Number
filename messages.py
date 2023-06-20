def takeFeedback() :
    feedback = input()
    return

def welcomeMessage() :
    print("Welcome to the Game!!")
    return

def winMessage(number, numberOfSteps) :
    print("Bingo, we have guessed your number in", numberOfSteps, "steps", "\nIt is ", number)
    return

def unfairMessage() :
    print("It seems that you are unfairly playing the game!")
    return

def endMessage() :
    print("We are sorry to see you go! Game Ended.")
    return
        
def Rules(maxIteration) :
    print("Every game has rules which make is more interesting so does we have for you :)")
    print("\t1. To start with this game you can consider a number between the range that is provided and then we will guess your number in less than ", maxIteration, " steps")
    print("\t2. You will be asked few questions that you will required to answer fairly to help us find your number")
    print("\t3 At any point of time if you enter an undesired input as a response, then we will end up the game")

def guessMessage(number) :
    print("\tIf the number is greater than ", number, ": please select 1")
    print("\tIf the number is less than ", number, " :please select 2")
    print("\tIf the number is correct then please select 0")
    inputFromUser = input()
    return inputFromUser

def markLine() :
    print("\n****---------------------------------------------------------------****\n")
    return
