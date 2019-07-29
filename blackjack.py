import random
import time
print("Welcome to Blackjack!")
def delay():
    time.sleep(1)
    print("...")
    time.sleep(1)
def newRound():
    print("...")
    print("...")
    print("...")
def makeNum(a, b, c):
    if((a == "Jack") or (a == "Queen") or (a == "King")):
        return 10
    elif(a == "Ace"):
        if(b + 11 <= 21):
            return 11
        else:
            return 1
    else:
        return int(deck[c])
for roundNumber in range(1, 3):
    deck = ["2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5",
    "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10",
    "10", "10", "10", "Jack", "Jack", "Jack", "Jack", "Queen", "Queen", "Queen", "Queen",
    "King", "King", "King", "King", "Ace", "Ace", "Ace", "Ace"]
    print("Round Number " + str(roundNumber))
    userTotal = 0
    computerTotal = 0
    while(userTotal <= 21):
        length = len(deck)
        randomNum = random.randint(0, (length-1))
        generatedNum = deck[randomNum]
        generatedNum = makeNum(generatedNum, userTotal, randomNum)
        print("You drew a " + deck[randomNum])
        deck.remove(deck[randomNum])
        delay()
        userTotal = userTotal + generatedNum
        print("Your current hand is worth " + str(userTotal) + " points")
        delay()
        if userTotal > 21:
            print("You busted!")
            break;
        choice = raw_input("Would you like to hit or stay?")
        if choice == "stay":
            break
    if(userTotal > 21):
        print("Sorry you lost!")
        newRound()
        continue
    else:
        print("Now it's the computers turn: ")
        while (computerTotal < 17 and computerTotal < userTotal):
            newLength = len(deck)
            randNum = random.randint(0, (newLength-1))
            comNum = deck[randNum]
            comNum = makeNum(comNum, computerTotal, randNum)
            computerTotal = computerTotal + comNum
            print("Computer got a " + deck[randNum] + "............ computer total is now: " + str(computerTotal))
            delay()
            deck.remove(deck[randNum])
        if(computerTotal > 21):
            print("Computer busted, you win!!!")
        elif(computerTotal >= userTotal):
            print("Computer finished with " + str(computerTotal) + " and you finished with " + str(userTotal))
            print("Computer wins!")
        else:
            print("Computer finished with " + str(computerTotal) + " and you finished with " + str(userTotal))
            print("You win!")
