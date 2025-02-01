# Hangman
# Author: John Botonakis
# Built with help from youtube.com/@TokyoEdTech

import os
import random
import time

import Helpers
from HangedMan import HANGMANPICS as hm


#FEEDBACK
#   While replaying just start the game not enter name/learn to play
#   Numbers and incorrect feedback handled by the input
#   Put all previously guessed letters alphabetically on the screen with every input
#   Clean up github (.gitignore should be top level, remove .idea)
#DONE   Instructions on running in terminal on README

# Initializes the entire game
def playgame():
    # Randomly select a word from a word bank as the active word to guess for
    active_word = Helpers.wordbank[random.randint(0, len(Helpers.wordbank) - 1)].lower()

    # Create a field that is the same length as the active word
    guess_field = len(active_word)

    # Populates the guess_field with underscores to represent each letter of active_word
    progress = ['_'] * guess_field #TODO: Change to Guess_field_length

    # Current hangman state; references the drawings in HangedMan.py
    hanged_state = 0 #TODO: Hanged_state_index opposed to just "state"
    # Area for storing/displaying the hangman ascii art
    gallows = hm[hanged_state]

    # Amount of total guesses the player has made
    total_guesses = 0

    # Player Name input with validation for only alphabetical characters
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            print(f"Welcome to Hangman {name.capitalize()}!")
            break
        else:
            print("Whoops! Please enter a valid name using only the alphabet; No numbers.") #TODO: Edit for !@#%#$^$&!

    # Displaying the rules via a dialogue tree. Each section has its own
    # validation to ensure the player does not enter anything aside from numbers.
    while True:
        try:
            rulecheck = int(input("Do you know the rules of Hangman? 1) Yes 2) No  ")) #TODO: Consistency with ":"
            if rulecheck == 1:
                break
            elif rulecheck == 2:
                Helpers.rules()
                while True:
                    try:
                        rulecheck2 = int(input("Shall I repeat these instructions? 1) Yes 2) No ")) #TODO: Consistency with ":"
                        if rulecheck2 == 2:
                            break
                        elif rulecheck2 == 1:
                            Helpers.rules()
                        else:
                            print(
                                "Please enter 1 for Yes, repeat the instructions; 2 for No, do not repeat the instructions..")
                    except ValueError:
                        print(
                            "Please enter 1 for Yes, repeat the instructions; 2 for No, do not repeat the instructions.")
                break
            else:
                print("Please select 1 for Yes and 2 for No.")
        except ValueError:
            print("Please enter 1 for Yes, 2 for No.")

    print("Great!\n")
    input("Press Enter to begin...")
    playing = True

    # MAIN LOOP
    while playing:
        # Prints the gallows and underscores for visual display
        print(gallows)
        print(" ".join(progress))

        # Input validation to ensure the player guess is only alphabetical
        while True:
            playerguess = input(f"GUESS: ").lower() #TODO: fString sometimes? FIX
            if len(playerguess) == 1 and playerguess.isalpha():
                total_guesses += 1
                break
            else:
                print("Whoops! Please enter a valid guess. That's one letter at a time!")

        # If the guess is correct, it will update the field with the correct letter, in the correct position
        if playerguess.lower() in active_word and playerguess not in progress:
            for index, letter in enumerate(active_word):
                if letter == playerguess:
                    progress[index] = playerguess  # Replaces the underscores with the letter guessed
            # Once there are no more spaces to put corrected letters, the game infers you have won
            # displaying your word, and the amount of guesses it took you to solve it.
            if "_" not in progress:
                print(
                    f"Woo-hoo! You did it! You've guessed the word: {active_word.upper()} in {total_guesses} guesses!")
                playing = False
                break
        elif playerguess in progress:
            print("You already guessed that letter! Try again")

        # If the guess is incorrect, the state of the hanged man will increase.
        # If the state reaches it's second to last drawing, it will warn the player
        # before making their final guess. If the final guess is wrong, kill the hangman.
        if playerguess.lower() not in active_word.lower():
            hanged_state += 1
            if hanged_state < len(hm) - 1:
                gallows = hm[hanged_state]
                time.sleep(0.5)
                if hanged_state == len(hm) - 2:
                    print("ONE GUESS LEFT! Make it count!!")
                    time.sleep(2)
            elif hanged_state == len(hm) - 1:
                print(hm[hanged_state])
                print("GAME OVER!")
                print("You've killed a man. How could you?")
                time.sleep(2)
                playing = False
                break


# Main Function:
# Sets up the game in a playing loop. Once the loop is exited
# from either winning or losing, it prompts the user to play again or quit out.
# Printouts confirm each choice, along with input validation.
def main():
    while True:
        # Clear the screen
        os.system('clear') #TODO: Fix
        playgame()

        while True:
            tryagain = input("Would you like to try again? 1) Yes! 2) No!\n")
            if tryagain == '1':
                break
            elif tryagain == '2':
                print("Hope you had fun, Partner! See ya when I see ya!")
                return  # Exit
            else:
                print("Please enter 1 for Yes, 2 for No.")


# Start the game
if __name__ == "__main__":
    main()
