
#Number Guess Game
#Isaac Arthur and Cameron Murphy
#11/2018
#To start type if you end the code menu() + Enter
import random

#This is the main hub for the difftent gamemodes
def menu():
    play = input("Would you like to \n1 Play The Number Guessing Game\n2 Play Custom Game\n3 Play Coin Flip Game\n4 Read The Credits\n5 Exit?\n")
    if play == "1":
        main_game()
    elif play == "4":
        print("""Number Guessing Game
By Isaac Arthur
And Cameron Murphy
Made 11/2/2018\n\n\n""")
        menu()
        
    elif play == "5":
        exit()
    elif play == "2":
        alt_game()
    elif play == "3":
        coin_game()
    else:
        print( play ,"is not a valid option please type 1, 2, or 3.")
        menu()
    
#this is the basic game with no alterations 
def main_game():
    guess = 0
    guess_amount = 5
    secret_number = str(random.randint(1,100))
    while guess_amount > 0:
        guess = input("Guess the number 1 to 100: ")
        if guess.isdigit():
            print("")
        else:
            print("That is not a valid input, stupid.\n\n\n")
            main_game()
            
        if guess == 100010001:
            print("YOU WIN!\n\n\n")
            menu()
        if guess == secret_number:
            print("YOU WIN!")
            menu()
        elif guess > secret_number:
            guess_amount -= 1
            print("Your guess was too high guess lower")
        elif guess < secret_number:
            guess_amount -= 1
            print("Your guess was too low guess higher")
    else:
        print("You ran out of guesses\nthe number was",secret_number,"\nYou Lose\n\n\n")
        menu()




def alt_game():
    x = input("What is the lowest number in the range?\n")
    if x.isdigit():
        print("")
        x = int(x)
    else:
        print("That is not a valid input, stupid.\n\n\n")
        alt_game()
    y = input("What is the highest number in the range?\n")
    if y.isdigit():
        print("")
        y = int(y)
    else:
        print("That is not a valid input, stupid.\n\n\n")
        alt_game()
    if x>= y:
        alt_game
    else:
        print("")
        
    z = input("How Many guesses do you want to have?\n")
    if z.isdigit():
        print("")
        z = int(z)
    else:
        print("That is not a valid input, stupid.\n\n\n")
        alt_game()
    guess = 0
    guess_amount = z
    secret_number = str(random.randrange(x,y))
    while guess_amount > 0:
        guess = input("guess the number between {} to {} ".format(x,y))
        if guess.isdigit():
            print("")
        else:
            print("That is not a valid input, stupid.\n\n\n")
        if guess == 100010001:
            print("YOU WIN!\n\n\n")
            menu()
        if guess == secret_number:
            print("YOU WIN!\n\n\n")
            menu()
        elif guess > secret_number:
            guess_amount -= 1
            print("Your guess was too high guess lower")
        elif guess < secret_number:
            guess_amount -= 1
            print("Your guess was too low guess higher")
    else:
        print("You ran out of guesses\nthe number was",secret_number,"\nYou Lose\n\n\n")
        menu()
            



def coin_game():
    guess = 0
    guess_amount = 1
    secret_number = str(random.randrange(1,3))
    while guess_amount > 0:
        guess = input("The coin has been flipped\n1 Heads\n2 Tails \n")
        if guess.isdigit():
            print("")
        else:
            print("That is not a valid input, stupid.\n\n\n")
            coin_game()
        if guess == 100010001:
            print("YOU WIN!\n\n\n")
            menu()
        if secret_number == "1":
            coin = "Heads"
        elif secret_number == "2":
            coin = "Tails"
        if guess == secret_number:
            print("YOU WIN!\n\n\n")
            menu()
        else:
            print("Wrong the result was",coin)
            menu()



menu()
