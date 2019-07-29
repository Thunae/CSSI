#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []
def parseList(itemName):
    for j in range(0, len(shopping_list)):
        if(itemName == shopping_list[j]):
            return True

while choice.lower() != "e":
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")

    choice = raw_input("Enter your choice [a|b|c|d|e]:")
    if(choice == 'a'):
        newItem = raw_input("What item would you like to add?")
        if(parseList(newItem)):
            print("This item is already on the list")
        else:
            shopping_list.append(newItem)
    elif(choice == 'b'):
        removeItem = raw_input("What item would you like to remove")
        itemExist = False
        for j in range(0, len(shopping_list)):
            if(removeItem == shopping_list[j]):
                itemExist = True
                break
        if (itemExist == False):
            print("That is not a valid item")
        else:
            checkSure = raw_input("Are you sure you want to remove: " + removeItem + " from the list?")
            if(checkSure == 'yes'):
                shopping_list.remove(removeItem)
                print("Successfully Removed")
            else:
                print("Item will not be removed")
    elif(choice == 'c'):
        checkItem = raw_input("What item would you like to check for?")
        itemIsThere = False
        for j in range(0, len(shopping_list)):
            if(checkItem == shopping_list[j]):
                itemIsThere = True
                break
        if itemIsThere:
            print(checkItem + " is on the shopping list")
        else:
            print("This item is NOT on the shopping list")

    elif(choice == 'd'):
        for j in range(0, len(shopping_list)):
            print(shopping_list[j])
    elif(choice == 'e'):
        break

    # elif(choice == 'c'):

    # Your code below! Handle the cases when the user chooses a, b, c, d, or e
