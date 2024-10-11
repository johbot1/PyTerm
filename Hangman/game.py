#Hangman
#Author: John Botonakis
#Built with help from youtube.com/@TokyoEdTech

import os
import random
import time
from HangedMan import HANGMANPICS as hm

#Clear the screen
os.system("Clear")

#Intialize the Game
wordbank = ['Macintosh', 'Linux', 'Windows','Malware','Python','Java','Technology',
            'Manjaro','Binary','Algorithm','Xenon','MOFSET','Debug']
active_word = wordbank[random.randint(0,len(wordbank)-1)]
guess = len(active_word)
hanged_state = hm[0]



name = input("Enter your name: ")
print(f"Welcome to Hangman {name.capitalize()}!")
rulecheck = int(input("Do you know the rules of Hangman? 1) Yes 2) No  "))
while rulecheck != 1:
        print("No problem! Here's how to play...")
        time.sleep(2)
        print("The object of this game is to guess a word letter by letter")
        time.sleep(2)
        print("Every wrong guess will draw another piece onto the gallows!")
        time.sleep(2)
        print("If you miss 5 guesses in a row, you lose and the man is hung")
        time.sleep(2)
        print("Solve the word before running out of guesses and you win!")
        time.sleep(2)
        rulecheck2 = int(input("Shall I repeat these instructions? 1) Yes 2) No "))
        if rulecheck2 == 2:
            rulecheck = 1
        else:
            rulecheck = 2

print("Great!")
input("Press Enter to begin...")
print(hanged_state)
playerguess = input(f"GUESS: ")

#MAIN LOOP
# while true:
#     print (f"Current Guess: {guess}")
#     print("Enter a ")