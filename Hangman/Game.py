#Hangman
#Author: John Botonakis
#Built with help from youtube.com/@TokyoEdTech

import os
import random
import time
from HangedMan import HANGMANPICS as hm
import Helpers

#Clear the screen
os.system("Clear")

#Intialize the Game

active_word = Helpers.wordbank[random.randint(0, len(Helpers.wordbank) - 1)]
guess = len(active_word)
hanged_state = hm[0]

name = input("Enter your name: ")
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
# Print the initial state of the hangman and the word in underscores
print(hanged_state)

# Create and display the underscores for the word to be guessed
word_display = "_ " * len(active_word)
print(word_display.strip())  # Use .strip() to remove the trailing space

playerguess = input(f"GUESS: ")


#MAIN LOOP
# while true:
#     print (f"Current Guess: {guess}")
#     print("Enter a ")
