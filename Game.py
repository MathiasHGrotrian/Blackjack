import random
from Card import Card


def makeSuit(deck, suit):
   
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
        
    
        deck.append(card)
        

    return deck

def make_deck():
    deck = []

    deck = deck + makeSuit([], 'Hearts')
    deck = deck + makeSuit([], 'Clubs')
    deck = deck + makeSuit([], 'Spades')
    deck = deck + makeSuit([], 'Diamonds')

    return deck

if __name__ == "__main__":
    
    deck = make_deck()

    random.shuffle(deck)

    for card in deck:
        print(card.__str__())
    
    
