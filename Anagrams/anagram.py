import collections
def read_process_data():
    with open('res/'+ currentDic + ".txt") as f:
        # the following line
        # - joins each line in the file into one big string
        # - removes all newlines and carriage returns
        # - converts everything to lowercase
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content
currentDic = raw_input("Which dictionary? dict1, dict2, dict3...")
content = read_process_data()
content = content.split(" ")
anagram_word = raw_input("What word do you want to anagram?")
anagram_word = anagram_word.replace(" ", "").lower()

finalWords = []


# def anagramSolver():


def countLetters(word):
    listedWord = list(word)
    return collections.Counter(listedWord)

def compareStringandDict(word, dictionary):
    countedString = word
    valWords = []
    for i in range(0, len(dictionary)):
        countedDictionary = countLetters(dictionary[i])
        successful = True
        for key in list(countedDictionary.keys()):
            if key in list(countedString.keys()):
                if countedString[key] < countedDictionary[key]:
                    successful = False
                    break
            else:
                successful = False
                break
        if successful == True:
            valWords.append(dictionary[i])
    return valWords

def subtractLetters(word1, word2):
    countedString = word1
    otherString = countLetters(word2)
    for key in list(otherString.keys()):
        countedString[key] = countedString[key] - otherString[key]
        if countedString[key] == 0:
            del countedString[key]
    return countedString


def anagramSolver2(anagramSoFar, string, dictionary):
    print(string)
    print(anagramSoFar)
    if len(string) == 0:
        finalWords.append(anagramSoFar)
        return
    for word in dictionary:
        newString = subtractLetters(string, word)
        newDict = compareStringandDict(newString, dictionary)
        print(newDict)
        anagramSoFar = list(anagramSoFar)
        anagramSoFar.append(word)
        anagramSolver2(anagramSoFar, newString, newDict)
    # return string + anagramSolver()
def anagramSolver(string, dictionary):
    return anagramSolver2([], string, dictionary)

wordToFind = countLetters(anagram_word)
firstDict = compareStringandDict(wordToFind, content)
anagramSolver(wordToFind, firstDict)
print(finalWords)


































# def isPrefix(prefix, dictionary, start, end):
#     while start <= end:
#         if len(dictionary) % 2 == 0:
#             middle = (len(dictionary) / 2) - 1
#         else:
#             middle = (len(dictionary) - 1) / 2
#
#         if prefix in dictionary[middle]:
#             if prefix == dictionary[middle]:
#                 valWords.append(prefix)
#             return True
#         elif prefix > middle:
#             start = middle + 1
#         elif prefix < middle:
#             end = middle - 1
#         isPrefix(prefix, dictionary, start, end)
#         #1. find the middle word in range
#         #2 compare prefix to middle word
#         #3a. if prefix is equal to middle word then return True
#         #3b. if prefix is less than middle word then end =  middle - 1
#         #3c. if prefix is greater than middle word start = middle + 1
# def isPrefix(prefix, dictionary):
#     return isPrefix(prefix, dictionary, 0, len(dictionary)-1)
# def isWord(word):
#     if word in content:
#         return True
#     else:
#         return False
