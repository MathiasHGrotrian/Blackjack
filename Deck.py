from Card import Card
import random

class Deck:

    def __init__(self, cards):
        self.cards = self.make_deck()

    # creates a list of cards with the given suit
    # only used in make_deck()
    def make_suit(self, cards, suit):
        for rank in range(13):
            if rank == 0:
                card = Card(suit, 'Ace')
            elif rank == 10:
                card = Card(suit, 'Jack')
            elif rank == 11:
                card = Card(suit, 'Queen')
            elif rank == 12:
                card = Card(suit, 'King')
            else:
                card = Card(suit, rank + 1)
            
            cards.append(card)
        

        return cards

    # create a full deck with all suits
    def make_deck(self):
        cards = []

        cards = cards + self.make_suit([], 'Hearts')
        cards = cards + self.make_suit([], 'Clubs')
        cards = cards + self.make_suit([], 'Spades')
        cards = cards + self.make_suit([], 'Diamonds')

        random.shuffle(cards)

        return cards