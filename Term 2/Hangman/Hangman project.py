#Hangman Game
#Isaac Arthur
#11/26

#imports
import random
import time

#constants
HANGMAN = (
"""

__________
|                     |
|                     |
|
|
|
|
|
|
|
|
|
TTTTTTTTTT

""",
"""

__________
|                     |
|                     |
|                   (  )
|                   /+
|                  /  |  
|
|
|
|
|
|
TTTTTTTTTT

""",
"""

__________
|                     |
|                     |
|                   (  )
|                   /+\
|                  /  |  \
|
|
|
|
|
|
TTTTTTTTTT

""",
"""

__________
|                     |
|                     |
|                   (  )
|                   /+\
|                  /  |  \
|                    /  
|                   /   
|
|
|
|
TTTTTTTTTT

""",
"""

__________
|                     |
|                     |
|                   (  )
|                   /+\
|                  /  |  \
|                    / \
|                   /   \
|                  
|
|
|
TTTTTTTTTT

""")



MAX_WRONG =len(HANGMAN)-1
WORDS = ("CODING","PYTHON","CAMERON","BRANDON","LOGANG","","","","","")
word = random.choice(WORDS) #the word to be guessed
so_far = "-"*len(word)
wrong = 0
used = [] #letters already gussed

print("Welcome to Hangman. Good luck!")

while wrong < MAX_WRONG and so_far != word:

    print(HANGMAN[wrong])
    print("\nYou've used the follwoing letters:\n",wrong)
    print("\nso far, the word is:\n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You've already guessed the letter",guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()

    used.append(guess)
    if guess == word:
            print("\nYou guessed it!")
            print("\nThe word was", word)
            exit()

    if guess in word:
        print("\nYes",guess,"is in the word!")

        # create a new so_far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry,",guess,"isn't in the word.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")

else:
    print("\nYou guessed it!")
print("\nThe word was", word)


input("\n\nPress the enter key to exit the game")




