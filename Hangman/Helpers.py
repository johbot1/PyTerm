# Helpers
# Author: John Botonakis
# Description: A separate file for functions and the word bank

import time

# Word Bank
wordbank = ['Macintosh', 'Linux', 'Windows', 'Malware', 'Python', 'Java', 'Technology',
            'Manjaro', 'Binary', 'Algorithm', 'Xenon', 'MOFSET', 'Debug']


# Rules:
# This is a terminal based "cutscene" to describe to the players how to play
def rules():
    print("No problem! Here's how to play...")
    time.sleep(2)
    print("The object of this game is to guess a word letter by letter.")
    time.sleep(2)
    print("Every wrong guess will draw another piece onto the gallows!")
    time.sleep(2)
    print("If you miss 5 guesses in a row, you lose and the man is hung.")
    time.sleep(2)
    print("Solve the word before running out of guesses and you win!")
    time.sleep(2)
