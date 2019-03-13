import random

class Card(object):
    """a playing card"""
    RANKS = ["A","2","3","4","5","6","7",
             "8","9","10","J","Q","K"]
    SUITS = ["♣","♢","♡","♠"]
    def __init__(self,rank,suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    """This class creates a players hand of cards and interact with that hand.
        You can clear your hand which removes all the cards from that hand
        You can add a card to your hand
        You can also give a card from your hand to another player's hand"""
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card)+" "
        else:
            rep = "<empty>"
        return rep


    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)



class Deck(Hand):
    """This is your deck with your deck you can do all the methods of Hand and populate, shuffle, and deal
        to populate do deck.populate()
        to shuffle deck.shuffle()
        to deal you do deck.deal(where you want to deal to,the ammount of cards you want to deal to these hands
        """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card,hand)

                else:
                    print("Can't contuinue deal. We be out of cards up in this, homie")



if __name__ =="__main__":
    print("Your ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit")








