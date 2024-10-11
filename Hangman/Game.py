#Hangman
#Author: John Botonakis
#Built with help from youtube.com/@TokyoEdTech
#ChatGPT used strictly for code comments only

import os
import random
from HangedMan import HANGMANPICS as hm
import Helpers

#Clear the screen
os.system("Clear")

#Intialize the Game
active_word = Helpers.wordbank[random.randint(0, len(Helpers.wordbank) - 1)]
guess_field = len(active_word)
hanged_state = 0

#Name Input With Validation
while True:
    name = input("Enter your name: ")
    if name.isalpha():
        break
    else:
        print("Whoops! Please enter a valid name using only the alphabet; No numbers.")

print(f"Welcome to Hangman {name.capitalize()}!")
rulecheck = int(input("Do you know the rules of Hangman? 1) Yes 2) No  "))
while rulecheck != 1:
    Helpers.rules()
    rulecheck2 = int(input("Shall I repeat these instructions? 1) Yes 2) No "))
    if rulecheck2 == 2:
        rulecheck = 1
    else:
        rulecheck = 2

print("Great!")
input("Press Enter to begin...")
playing = True


#MAIN LOOP
while playing:
    # Print the initial state of the hangman and the word in underscores
    print(hanged_state)

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
    if playerguess not in active_word:
        hanged_state + 1