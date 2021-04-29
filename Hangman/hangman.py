
import cmath
import math
import random as rn

guesses = set()

def guess_a_letter():
    
    print("\nLetters already used: {}\n".format(guesses))
    guess = input("Guess a letter: ")

    while not(len(guess) == 1) or guesses.issuperset([guess]):

        if len(guess) == 1:
            print("You already used that letter")
        else:
            print("Your guess has to be a single letter")
        guess = input("Try another Letter: ")
    guesses.add(guess)
    return guess


file = open("listofwords.txt","r")
words = []

for word in file:
    words.append(word)
file.close()

words = [new_word[0:len(new_word) - 1] for new_word in words]

choice = input("Play handman? y/n: ")
Play = False
if choice == "y":
    Play = True

while Play:
    keyword = words[rn.randint(0,len(words) - 1)]
    progress = ["--- "] * len(keyword)
    num_tries = 4
    while num_tries >= 1:
        print("*"* 20)
        print("{} tries remaining\n".format(num_tries))
        print("Word: ", progress)
        guess = guess_a_letter()
        index = keyword.find(guess,0)
        if index == -1:
            print("{} is not in the word".format(guess))
            num_tries -= 1
        
        else:
            while not(index == -1):
                progress[index] = guess
                index = keyword.find(guess,index + 1)
            if progress.count("--- ") == 0:
                break
    if num_tries < 1:
        print("Nice try! The word was {}".format(keyword))
    else:
        print("You guessed it!: {}".format(keyword))
    choice = input("Play again: y/n: ")
    if not (choice == "y"):
        Play = False