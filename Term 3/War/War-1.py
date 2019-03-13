#Zachary Page, Isaac Arthur, Cody Dzierzon, Jack Pike, Logan Nelson
#02/21/19
#War
#########################################################################################
# imports
import cards, games, random


#########################################################################################
# Classes
class War_Card(cards.Card):
    """Card value used to play war"""
    ace_value = 1

    @property
    def value(self):
        if self.is_face_up:
            v = War_Card.ranks.index(self.rank) + 1
        else:
            v = None
        return v
#########################################################################################
class War_Deck(cards.Deck):
    """Holds all of the war cards, with their suits and ranks"""
    def populate(self):
        for suit in War_Card.suits:
            for rank in War_Card.ranks:
                self.cards.append(War_Card(rank, suit))
#########################################################################################
class War_Hand(cards.Hand):
    """The init overrides the war hand with the super class and provides the name.
        The str takes the name and adds the total with the name
        The total will take the card and add a value to it up to the Ace(which can treated as a 1)
        The busted will return a total value of 0 representing you losing."""
    def __init__(self, name):
        super(War_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(War_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # if a card in the hand has a value of None, then the total is None
        for card in self.cards:
            if not card.value:
                return None
        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
            t += card.value

    @property
    def is_busted(self):
        return self.total == 0
#########################################################################################
class War_Player(War_Hand):
    """This is You and your opponent
    use player.play() to put the top card from your hand into the field
    use player.lose() to make a player lose and clear the hands
    use player.win()  to make a player win
    use player.war(pot) to place 3 cards in the pot"""

    def play(self, hand):
        top_card = self.cards[0]
        self.give(top_card, hand)

    def lose(self):
        print(self.name, "loses.")
        self.cards.clear()

    def win(self):
        print(self.name, "wins.")

    def war(self, pot):
        if len(self.cards) >= 3:
            for i in range(3):
                self.give(self.cards[0], pot)
#########################################################################################
class War_Field(War_Hand):
    """this is the field to see who wins each round
    check_winner to find out who won the round
    use give_to_pot to distribute the cards to the winner"""
    def __str__(self):
        rep = super(War_Field, self).__str__()
        return rep

    @property
    def check_winner(self):
        if self.cards[0].value > self.cards[1].value:
            winner = 0
        elif self.cards[0].value < self.cards[1].value:
            winner = 1
        else:
            winner = None
        return winner

    def give_to_pot(self, pot):
        for i in range(len(self.cards)):
            self.give(self.cards[0], pot)
#########################################################################################
class War_Pot(War_Hand):
    def give_to_winner(self, winner):
        for i in range(len(self.cards)):
            self.give(self.cards[0], winner)
#########################################################################################
class War_Game(object):
    def __init__(self, names):

        self.players = []
        for name in names:
            player = War_Player(name)
            self.players.append(player)

        self.pot = War_Pot("pot")
        self.field = War_Field("Field")
        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def game_over(self):
        for player in self.players:
            x = len(player.cards)

            if x <= 0:
                return True
        return False

    def play(self):
        count = 0
        count2 = 0
        game_over = False
        self.deck.deal(self.players, per_hand=26)
        while not game_over:
            for player in self.players:
                player.play(self.field)

            winner = self.field.check_winner
            print(self.players[0].name + " ", self.field, self.players[1].name)
            self.field.give_to_pot(self.pot)
            if winner == 0 or winner == 1:
                print(self.players[winner].name, "Wins")
                self.pot.give_to_winner(self.players[winner])
            else:
                print("War")
                self.players[0].war(self.pot)
                self.players[1].war(self.pot)
                print(self.pot)
            print("Cards in", self.players[0].name, "deck", len(self.players[0].cards))
            print("Cards in", self.players[1].name, "deck", len(self.players[1].cards))
            game_over = self.game_over()

            count += 1
            count2 += 1
            print(count2)
            if count == 52:
                random.shuffle(self.players[0].cards)
                count = 0
            self.field.give_to_pot(winner)
            input("press enter to play")

            game_over = self.game_over()
#########################################################################################
# Main
def main():
    print("\t\tWelcome to War!\n")
    names = []
    number = 2
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    game = War_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again? (Y/N): ")

main()
input("\n\nPress the enter key to exit: ")