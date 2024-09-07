"""
Author: Samantha Erickson
Date:   September 7th, 2024
"""
import random

def set():
    mySet = {"Black", "Red", "Pink", "Orange", "Yellow", "Green", "Teal", "Blue", "Purple", "White"}
    
    print("\nA set cannot be searched by it's index but it can search for a specified value.")
    print("Is Pink in the set?","Pink" in mySet)
    print("Is Pink not in the set?","Pink" not in mySet,"\n")
    
    print("A set is unordered so by nature it shuffles it's self each time the program starts...\n", mySet,"\n")
    
    print("A set cannot change a existing item however it can add a new item. Brown has now been added to the list.")
    mySet.add("Brown")
    print("However we cannot control where the new item's placement within the list because it is unordered...\n",mySet,"\n")
    
    print("A item can be removed from the list however it cannot be removed by it's index only by it's specified value.")
    mySet.remove("Black")
    print("You will find that Black has now been removed from the list...\n",mySet,"\n")

def list():
    myList = ["White", "Purple", "Blue", "Teal", "Green", "Yellow", "Orange", "Pink", "Red", "Black"]
    print("\nOriginal list...",myList,"\n")
    print("3rd element...",myList[2],"\n")
    random.shuffle(myList)
    print("Shuffle list...",myList,"\n")
    myList.append("Brown")
    print("Brown was added...",myList,"\n")
    myList.pop(0)
    print("1st element removed...",myList,"\n")
    myList.remove("Black")
    print("Black was removed...",myList,"\n")

set()
list()