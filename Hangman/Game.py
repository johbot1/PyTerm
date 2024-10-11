#Hangman
#Author: John Botonakis
#Built with help from youtube.com/@TokyoEdTech
#ChatGPT used strictly for code comments only

import os
import random
import time

from HangedMan import HANGMANPICS as hm
import Helpers
from Hangman.Helpers import gameOver

#Clear the screen
os.system("Clear")

#Intialize the Game Parts

#Choose a random word from the wordbank
active_word = Helpers.wordbank[random.randint(0, len(Helpers.wordbank) - 1)].lower()
#Initialize the guessing field that is the same length as the active word
guess_field = len(active_word)

#Creates a list of underscores for every letter in that active word
progress = ['_'] * guess_field

#The state of the current hangman before a guess
hanged_state = 0
#Responsible for the hangman drawing
gallows = hm[hanged_state]


#Name Input With Validation
while True:
    name = input("Enter your name: ")
    if name.isalpha():
        print(f"Welcome to Hangman {name.capitalize()}!")
        break
    else:
        print("Whoops! Please enter a valid name using only the alphabet; No numbers.")

#Understanding the Rules with Validation
while True:
    try:
        rulecheck = int(input("Do you know the rules of Hangman? 1) Yes 2) No  "))
        #If the rulecheck is 1, Player knows the rules and we can break
        if rulecheck == 1:
            break
        elif rulecheck == 2:
                #If the rulecheck is 2, display the rules
                Helpers.rules()
                while True:
                    try:
                        rulecheck2 = int(input("Shall I repeat these instructions? 1) Yes 2) No "))
                        #If we don't need to repeat the instructions, continue with the game
                        if rulecheck2 == 2:
                            break
                        else:
                            print("Please enter 1 for Yes, repeat the instructions; 2 for No, do not repeat the instructions..")
                    except ValueError:
                        print("Please enter 1 for Yes, repeat the instructions; 2 for No, do not repeat the instructions.")
                break #Breaks out of the outermost loop to continue to the game
        else:
            print("Please select 1 for Yes and 2 for No.")
    except ValueError:
        print("Please enter 1 for Yes, 2 for No.")


print("Great!")
input("\nPress Enter to begin...")
playing = True

#MAIN LOOP
while playing:
    # Print the initial state of the hangman and the word in underscores
    print(gallows)

    # Create and display the current underscore progress for the word to be guessed
    print(" ".join(progress))

    #Player input validation (Only letters, nothing else)
    while True:
        playerguess = input(f"GUESS: ").lower()
        if len(playerguess) == 1 and playerguess.isalpha():
            break
        else:
            print("Whoops! Please enter a valid guess. That's one letter at a time!")

    #Guess is RIGHT
    if playerguess.lower() in active_word and playerguess not in progress:
        #Update the progress in the GUESS field with the letter in the correct position
        for index, letter in enumerate(active_word):
            if letter == playerguess:
                progress[index] = playerguess #Replaces the underscores with the letter guessed
        if "_" not in progress:
            print(f"Woo-hoo! You did it! You've guessed the word: {active_word.upper()} in {hanged_state} guesses!")
            playing = False
            break
    elif playerguess in progress:
        print("You already guessed that letter! Try again")

    #Guess is WRONG
    if playerguess.lower() not in active_word.lower():
        # Increment the hanged state to reflect bad guess
        hanged_state += 1

        #Check if we have reached the end of the drawings:
        if hanged_state <len(hm)-1:
            gallows = hm[hanged_state] #Update the hangman
            time.sleep(0.5)
            # If this is the last guess, inform the player and wait a second so they understand this is the last guess
            if hanged_state == len(hm)-2:
                print("ONE GUESS LEFT! Make it count!!")
                time.sleep(2)

        #But if that was the last guess, kill em.
        elif hanged_state == len(hm)-1:
            print(hm[hanged_state])
            print("GAME OVER!")
            playing = False
            break
            #Game over!