# Hangman
# Author: John Botonakis
# Built with help from youtube.com/@TokyoEdTech

import os
import random
import time

import Helpers
from HangedMan import HANGMANPICS as hm

global special_characters
special_characters = "!@#$%^&*()-+?_=,<>/;:{}\|=+`~''"""
#FEEDBACK
#DONE  While replaying just start the game not enter name/learn to play
#DONE   Numbers and incorrect feedback handled by the input
#DONE   Put all previously guessed letters alphabetically on the screen with every input
#DONE   Clean up github (.gitignore should be top level, remove .idea)
#DONE   Instructions on running in terminal on README

#start_preamble()
#This function plays before the game to ask for a name, as well as
#introduce how to play Hangman for those unfamiliar
def start_preamble():
    preamble_state = True
    # Player Name input with validation for only alphabetical characters
    while preamble_state:
        name = input("Enter your name: ")
        if name.isalpha():
            print(f"Welcome to Hangman {name.capitalize()}!")
            break
        elif name.isnumeric():
            print("Whoops! Please enter a valid name without numbers")
        elif any(c in special_characters for c in name):
            print("Looks like you got some funky characters. Only letters please.")

    while preamble_state:
        try:
            rulecheck = int(input("Do you know the rules of Hangman?:\n1) Yes 2) No  "))
            if rulecheck == 1:
                break
            elif rulecheck == 2:
                Helpers.rules()
                while True:
                    try:
                        rulecheck2 = int(input("Shall I repeat these instructions?:\n1) Yes 2) No "))
                        if rulecheck2 == 2:
                            break
                        elif rulecheck2 == 1:
                            Helpers.rules()
                        else:
                            print(
                                "Please enter:\n1 for Yes, repeat the instructions; 2 for No, do not repeat the "
                                "instructions ")
                    except ValueError:
                        print(
                            "Please enter:\n1 for Yes, repeat the instructions; 2 for No, do not repeat the "
                            "instructions.")
            else:
                print("Please select:\n1 for Yes and 2 for No ")
        except ValueError:
            print("Please enter:\n1 for Yes, 2 for No ")


# Initializes the entire game
def playgame():
    # Randomly select a word from a word bank as the active word to guess for
    active_word = Helpers.wordbank[random.randint(0, len(Helpers.wordbank) - 1)].lower()

    # Create a field that is the same length as the active word
    guess_field_length = len(active_word)

    # Populates the guess_field_length with underscores to represent each letter of active_word
    progress_field = ['_'] * guess_field_length

    # Current hangman state; references the drawings in HangedMan.py
    hanged_state_index = 0
    # Area for storing/displaying the hangman ascii art
    gallows = hm[hanged_state_index]

    # Amount of total guesses the player has made
    total_guesses = 0

    #Keep track of previous guesses
    prev_guessed_letters = []

    print("Great!\n")
    input("Press Enter to begin...")
    playing = True

    # MAIN LOOP
    while playing:
        # Prints the gallows and underscores for visual display
        print(gallows)
        print(" ".join(progress_field))
        prev_guessed_letters.sort()
        print('PREVIOUS:', *prev_guessed_letters)

        # Input validation to ensure the player guess is only alphabetical
        while True:
            playerguess = input('GUESS: ').lower()
            if playerguess.isnumeric():
                print("Sorry, this is a letters only game. No numbers!")

            elif any(c in special_characters for c in playerguess):
                print("Looks like you got some funky characters. Only letters please!")

            elif playerguess in progress_field or playerguess in prev_guessed_letters:
                print("You already guessed that letter! Try again")

            elif len(playerguess) >1:
                    print("Appreciate your enthusiasm partner, but one letter at a time!")
            elif len(playerguess) == 1 and playerguess.isalpha():
                total_guesses += 1
                prev_guessed_letters.append(playerguess)
                break


        # If the guess is correct, it will update the field with the correct letter, in the correct position
        if playerguess.lower() in active_word and playerguess not in progress_field:
            for index, letter in enumerate(active_word):
                if letter == playerguess:
                    progress_field[index] = playerguess  # Replaces the underscores with the letter guessed
            # Once there are no more spaces to put corrected letters, the game infers you have won
            # displaying your word, and the amount of guesses it took you to solve it.
            if "_" not in progress_field:
                print(
                    f"Woo-hoo! You did it! You've guessed the word: {active_word.upper()} in {total_guesses} guesses!")
                playing = False
                break



        # If the guess is incorrect, the state of the hanged man will increase.
        # If the state reaches it's second to last drawing, it will warn the player
        # before making their final guess. If the final guess is wrong, kill the hangman.
        if playerguess.lower() not in active_word.lower():
            hanged_state_index += 1
            if hanged_state_index < len(hm) - 1:
                gallows = hm[hanged_state_index]
                time.sleep(0.5)
                if hanged_state_index == len(hm) - 2:
                    print("ONE GUESS LEFT! Make it count!!")
                    time.sleep(2)
            elif hanged_state_index == len(hm) - 1:
                print(hm[hanged_state_index])
                print("GAME OVER!")
                print("You've killed a man. How could you?")
                time.sleep(2)
                # playing = False
                break


# main:
# Sets up the game in a playing loop. Once the loop is exited
# from either winning or losing, it prompts the user to play again or quit out.
# Printouts confirm each choice, along with input validation.
def main():
    os.system('clear')
    start_preamble()
    while True:
        # Clear the screen
        os.system('clear')
        playgame()
        while True:
            tryagain = input("Would you like to try again?:\n1) Yes! 2) No! ")
            if tryagain == '1':
                break
            elif tryagain == '2':
                print("Hope you had fun, Partner! See ya when I see ya!")
                return  # Exit
            else:
                print("Please enter:\n1 for Yes, 2 for No ")


# Start the game
if __name__ == "__main__":
    main()
