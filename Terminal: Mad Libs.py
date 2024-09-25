import time
from tkinter import messagebox, simpledialog

from numpy import number

#LoadStory Function:
#Takes the .txt file and loads it in.
#Then prompts the user for each variable,
#and stores them in the newly created story
def loadstory(title):
    run = True
    while run:
        with open(title, "r") as file:
            story = file.read()
        varstart = "{"
        varend = "}"

        entstart = "\\"
        entend = "n"

        words = []
        start = -1

        for i, char in enumerate(story):
            if char == varstart:
                start = i

            if char == varend and start != -1:
                word = story[start:i + 1]
                words.append(word)
                start = -1
        inputs = {}
        for word in words:
            displayword = word.strip("{")
            displayword = displayword.strip("}")
            if word not in inputs:
                answer = input("Can you give me " + displayword + ": ")
                try:
                    assert answer.isalpha()
                except AssertionError:
                    print("Invalid input. Only letters please")

        #         if displayword == "a name" or "another name":
        #             answer = answer.capitalize()
        #         inputs[word] = answer
        #
        # for word in words:
        #     story = story.replace(word, inputs[word])
        #
        # print(story)

def evencheck(number):
    if number % 2 == 0:
        return True

def saypause(string, t):
    print(string)
    time.sleep(t)
def medmayhem():
    noun1 = input("Let's get started! Please give me a noun: ")
    verb1 = input("Please give me a verb: ")
    saypause("Oh this is already turning into a fun story...",2)
    noun2 = input("Please give me another noun: ")
    adjective2 = input("Please give me a adjective: ")
    verb2 = input("Please give me a verb: ")
    adverb1 = input("Please give me a adverb: ")
    saypause("Interesting choice. You sure about that one?",2)
    saypause( "You know what, nevermind, let's keep going.",1)
    adjective1 = input("Please give me a adjective: ")
    adverb2 = input("Please give me a adverb: ")
    verbly1 = input("Please give me a verb ending with -ly: ")
    verbly2 = input("Please give me a verb ending with -ly: ")
    pnoun1 = input("Please give me a Proper noun: ")

def woewedding():
    loadstory("WeddingWoes")




    # name1 = input("Please give me a name: ")
    # name2 = input("Please give me a second name: ")
    # name1.capitalize()
    # name2.capitalize()
    # adjective1 = input("Please give me a adjective: ")
    # adjective2 = input("Please give me a adjective: ")
    # verb1 = input("Please give me a verb: ")
    # verbing1 = input("Please give me a verb ending in -ing: ")
    # noun1 = input("Please give me a noun: ")
    # verb2 = input("Please give me a verb ending in -ly: ")
    # noun2 = input("Please give me a noun: ")
    # noun3 = input("Please give me a noun: ")
    # noun4 = input("Please give me a theme: ")
    # adjective3 = input("Please give me an adjective: ")
    # adverb1 = input("Please give me a adverb: ")
    # noun4 = input("Please give me a noun: ")
    # noun5 = input("Please give me a noun: ")
    # adjective4 = input("Please give me a adjective: ")
    # adjective5 = input("Please give me a adjective: ")
    # verb3 = input("Please give me a verb: ")
    # noun6 = input("Please give me a noun: ")
    # noun7 = input("Please give me a noun: ")
    # adjective6 = input("Please give me a adjective: ")
    # verb4 = input("Please give me a verb: ")
    # adjective7 = input("Please give me a adjective: ")
    # adjective8 = input("Please give me a adjective: ")
    # adjective9 = input("Please give me a adjective: ")
    # noun8 = input("Please give me a noun: ")
    # verb5 = input("Please give me a verb: ")
    # verbed1 = input("Please give me a verb ending in -ed: ")
    # noun9 = input("Please give me a noun: ")
    # noun10 = input("Please give me a noun: ")
    # verbed2 = input("Please give me a verb ending in -ed: ")
    # verbed3 = input("Please give me a verb ending in -ed: ")
    # adjective10 = input("Please give me a adjective: ")
    # adjective11 = input("Please give me a adjective: ")
    # adjective12 = input("Please give me a adjective: ")
    # adjective13 = input("Please give me a adjective: ")
    # adjective14 = input("Please give me a adjective: ")
    # verb6 = input("Please give me a verb: ")
    # verb7 = input("Please give me a verb: ")
    # verb8 = input("Please give me a verb: ")
    # verb9 = input("Please give me a verb: ")
    # adverb2 = input("Please give me a adverb: ")
    # noun11 = input("Please give me a noun: ")
    # verb10 = input("Please give me a verb: ")
    # verb11 = input("Please give me a verb: ")
    # verb12 = input("Please give me a verb: ")
    # verb13 = input("Please give me a verb: ")
    # adjective11 = input("Please give me a adjective: ")
    # adjective12 = input("Please give me a adjective: ")
    # adjective13 = input("Please give me a adjective: ")
    # adjective14 = input("Please give me a adjective: ")
    # adjective15 = input("Please give me a adjective: ")
    # noun12 = input("Please give me a noun: ")
    # noun13 = input("Please give me a noun: ")
    # noun14 = input("Please give me a noun: ")
    # noun15 = input("Please give me a noun: ")
    # noun16 = input("Please give me a noun: ")
    # verbed4 = input("Please give me a verb ending in -ed: ")
    # print(f"""
    # It was the day of {name1} and {name2}’s wedding, and it was {adjective1} outside. {name1} woke up feeling
    # {adjective2}, but nothing could stop them today. {name1} {verb1} out of their room to greet their bridal party, but
    # they were busy {verbing1} {noun1}! {name1} {verb2} at their friends, reminding them that it was time to
    # prepare for the wedding.\n
    # Once the bridal party was gathered, it was time to get ready. Their maid of honor wore {noun2} while
    # the bridal party opted for {noun3}. The wedding had a theme of {noun4}, so they each put on
    # {adjective3} makeup to match. {name1} waited {adverb1} as their hair stylist put their locks up into a {noun4}
    # hairdo, finishing the style with a {noun5} in their hair. Finally, it was time for them to put on the dress.\n
    # {name1} remembered their dress being {adjective4}, but as they put it on, they realized it was a lot more
    # {adjective5} than they remembered. Their bridal party {verb3} around them, making sure that all of
    # the {noun6} and {noun7} were ready for the big day. As {name1} gazed in the mirror, their mother
    # {verb4} up behind them. “You look {adjective6},” she told {name1}, with tears in her eyes. {name1} studied
    # themselves in the mirror. Their dress was {adjective7}, their hair was {adjective8}, and even their makeup was
    # {adjective9}. {name1} felt a swell of {noun8}, and {verb5} their mom into a tight hug.\n
    #
    # It was time for the wedding to begin. {name2} {verbed1} at the altar, looking {adjective10}. The music
    # started, filling the air with sounds of {noun9} and {noun10}. The bridal party and groomsmen
    # {verb6} {verb7} down the aisle, and the crowd watched {adverb2}. A gasp rumbled through
    # the crowd when {name1} began to {verb8} down the aisle. They looked absolutely {adjective11}. They were
    # as {adjective12} as a {noun11}. {name2} {verbed2} at the sight of their {adjective13} bride. The bride and
    # groom joined hands and {verbed3} together.\n
    #
    # {name2}’s vows were {adjective14}, causing {name1} to {verb9} with emotion. {name1}’s vows were
    # {adjective15}, and {name2} couldn’t help but {verb10}. “With the {noun12} vested in me,
    # I now pronounce you {noun13} and {noun14},” the officiant said proudly. “You may now
    # {verb11} the bride.”\n
    # {name2} and {name1} shared their first {verb12} as a married couple, and {verbed4} back down the aisle
    # together to the {verb13} of the crowd. {noun15} and {noun16} were tossed in the air in
    # celebration. It was time for a party!\n
    # """)

print("Welcome to Mad Libs!")
print("Please choose your MadLib:\n1) Medieval Mayhem\n2) Woeful Wedding\n3) Airplane Pandemonium\n5) Quit")
choice = int(input("I choose number: "))

if choice == 1:
    print("You have chosen Medieval Mayhem!")
    medmayhem()
elif choice == 2:
    print("You have chosen Woeful Wedding!")
    woewedding()
elif choice == 3:
    print("You have chosen Airplane Pandemonium!")
elif choice == 5:
    print("Thanks for playing! C ya!")
