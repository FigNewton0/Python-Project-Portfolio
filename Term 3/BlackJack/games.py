import cards, random
def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def roll(self):

    die1 = random.randrange(1,6)
    roll = die1
    print("You rolled a",die1 )
    return roll


def random_num_gen():
    x = input("What is the lowest number in the range?\n")
    if x.isdigit():
        x = int(x)
    else:
        print("That is not a valid input, stupid.\n\n\n")
        random_num_gen()
    y = input("What is the highest number in the range?\n")
    if y.isdigit():

        y = int(y)
    else:
        print("That is not a valid input, stupid.\n\n\n")
        random_num_gen()
    if x >= y:
        random_num_gen()
    else:
        print("")

    secret_number = str(random.randrange(x, y))

    print(secret_number)


class Player(object):
    """a player for your game"""
    def __init__(self,name):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name
        rep = rep +" "+str(score)
        return rep

if __name__ == "__main__":
    print("Your ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit")



















































































































































