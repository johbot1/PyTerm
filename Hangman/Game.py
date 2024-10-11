#Hangman
#Author: John Botonakis
#Built with help from youtube.com/@TokyoEdTech
#ChatGPT used strictly for code comments only

import os
import random
import time

from HangedMan import HANGMANPICS as hm, finalchance as finalchance
import Helpers


#Clear the screen
os.system("Clear")

#Intialize the Game
active_word = Helpers.wordbank[random.randint(0, len(Helpers.wordbank) - 1)]
guess_field = len(active_word)
hanged_state = 0
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
input("Press Enter to begin...")
playing = True


#MAIN LOOP
while playing:
    # Print the initial state of the hangman and the word in underscores
    print(gallows)

    # Create and display the underscores for the word to be guessed
    word_display = "_ " * guess_field
    print(word_display.strip())

    #Player input validation (Only letters, nothing else)
    while True:
        playerguess = input(f"GUESS: ")
        if len(playerguess) == 1 and playerguess.isalpha():
            break
        else:
            print("Whoops! Please enter a valid guess. That's one letter at a time!")

   #Guess is WRONG
    if playerguess.lower() not in active_word.lower():
        # Increment the hanged state to reflect bad guess
        hanged_state += 1

        #Check if we have reached the end of the drawings:
        if hanged_state <len(hm)-2:
            gallows = hm[hanged_state] #Update the hangman
            time.sleep(0.5)
            if hanged_state == finalchance:
                print("ONE GUESS LEFT! Make it count!!")
                time.sleep(2)
        elif hanged_state == len(hm)-1:
            print(hm[hanged_state])
            break
            #Game over!