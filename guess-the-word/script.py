#Guess the Word game
import sys
import time
import random
wordsList = ['programming', 'google', 'adventure', 'cat', 'olympic', 'brick', 'picture', 'photograph', 'person',
'jungle', 'monkey', 'alphabet']
designatedWord = wordsList[random.randint(0, len(wordsList))]
gameOver = False
l = list(designatedWord)
guessArray = []
printString = ""
for j in range(0, len(l)):
    guessArray.append('-')
def initializeString():
    printString = ""
    for item in guessArray:
        printString = printString + item
    print(printString)
def delay():
    time.sleep(0.2)
    print(".")
    time.sleep(0.2)
    print(".")
    time.sleep(0.2)
    print(".")
    time.sleep(0.2)
def parseArray(array, name):
    for item in array:
        if name == item:
            return 1

guessString = "Guesses: "
mistakes = 0
while (gameOver == False):
    initializeString()
    print(guessString)
    print("Mistakes: " + str(mistakes))
    guess = raw_input("Guess a letter: ")
    correctGuess = False
    if(parseArray(guessArray, guess) == 1):
        print("You already guessed this")
    else:
        guessString = guessString + guess + " "
        for j in range(0, len(l)):
            if(l[j] == guess):
                guessArray[j] = l[j]
                correctGuess = True
        if(correctGuess == False):
            mistakes = mistakes + 1

    if(mistakes >= 5):
        print("Too Many Mistakes!")
        gameOver = True
        print("The correct answer was: " + designatedWord)
    if(l == guessArray):
        initializeString()
        print("Congrats you guessed correctly!")
        gameOver = True
    delay()
