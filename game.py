import messages as m

selectRange = [1, 1000]
maxIteration = 12

def playGame() :
    m.welcomeMessage()
    m.Rules(maxIteration)

    print("Please select a number between the range: ", selectRange[0], "to", selectRange[1])

    userResponse = input("Please Enter `y` if you have selected the number and ready to begin the game: ")

    if(userResponse == 'y' or userResponse == "Y") :
        startGame()
    m.endMessage()
    m.markLine()
    print("Please rate the experience [1-5]")
    ratings = int(input())
    if(ratings >= 4) :
        print("We glad that you liked the game")
    else :
        print("We are sorry for the bad experience")
        print("Please feel free to provide the feedback so that we can improve!")
        m.takeFeedback()
        print("Thanks for the feedback! We will work on it and try to improve")
    return

def startGame() :

    print("Great! Lets start the game")

    start = selectRange[0]
    end = selectRange[1]
    numberOfSteps = 0

    while start <= end :
        numberOfSteps += 1  
        m.markLine()
        guessedNumber = start + (end - start)//2
        userResponse = m.guessMessage(guessedNumber)
        if userResponse == '1' :
            start = guessedNumber + 1
        elif userResponse == '2' :
            end = guessedNumber - 1
        elif userResponse == '0' :
            m.winMessage(guessedNumber, numberOfSteps)
            return
        else :
            m.unfairMessage()
            return
    m.unfairMessage()
    return