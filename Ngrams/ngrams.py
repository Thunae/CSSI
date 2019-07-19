import re
import random
def read_process_data():
    with open('res/hamlet.txt') as f:
        # the following line
        # - joins each line in the file into one big string
        # - removes all newlines and carriage returns
        # - converts everything to lowercase
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content

content = read_process_data()
content = (re.sub(' +', ' ',content))
words = content.split(" ")

map = {}
window = []
g = raw_input("Pick the number of n")
n = int(g)
for j in range(0, (n-1)):
    window.append(words[j])
for k in range((n-1), len(words)):
    tup1 = tuple(window)
    if tup1 in map:
        currentWord = words[k]
        map[tup1].append(currentWord)
        window.append(currentWord)
        window.pop(0)
    else:
        currentWord = [words[k]]
        map[tup1] = currentWord
        window.append(words[k])
        window.pop(0)
print(map)
startPoint = random.randint(0, len(words))
k = startPoint
sentence = []
printString = ""
while k < (startPoint + (n-1)):
    sentence.append(words[k])
    k += 1
for p in range(0, len(sentence)):
    printString = printString + " " + sentence[p]
numberOfWords = raw_input("How many words do you want to display?")
rr = int(numberOfWords)
for i in range(0, rr -(n-1)):
    tuple2 = tuple(sentence)
    newString = map[tuple2][random.randint(0, len(map[tuple2])-1)]
    printString = printString + " " + newString
    sentence.append(newString)
    sentence.pop(0)
print(printString)
