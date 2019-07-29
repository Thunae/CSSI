import random
for roundNumber in range(1, 6):
    print("Round " + str(roundNumber))
    invalidInput = True
    while (invalidInput):
        userChoice = raw_input("Rock, Paper or Scissors?")
        if (userChoice == "Rock") or (userChoice == "Paper") or (userChoice == "Scissors"):
            invalidInput = False;
        elif(userChoice == "Exit"):
            break
        else:
            print("Enter a valid option")
    if userChoice == "Exit":
        break
    uWinner = "You win!"
    cWinner = "Computer wins!"
    computer = random.randint(0, 2)
    choiceList = ["Paper", "Scissors", "Rock"]
    computerChoice = choiceList[computer]
    print("Computer chose " + str(computerChoice))
    if userChoice == choiceList[computer - 1]:
        print(cWinner)
    elif userChoice == computerChoice:
        print("It's a tie!")
    else:
        print(uWinner)



    # if computerChoice == "Rock" and userChoice == "Scissors":
    #     print(cWinner)
    # elif computerChoice == "Rock" and userChoice == "Paper":
    #     print(uWinner)
    # elif computerChoice == "Paper" and userChoice == "Scissors":
    #     print(uWinner)
    # elif computerChoice == "Paper" and userChoice == "Rock":
    #     print(cWinner)
    # elif computerChoice == "Scissors" and userChoice == "Rock":
    #     print(uWinner)
    # elif computerChoice == "Scissors" and userChoice == "Paper":
    #     print(cWinner)
    # elif computerChoice == userChoice:
    #     print("It's a tie!")
