import random
from Card import Card
from Player import Player


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

def deal_card(deck, player):

    card = random.choice(deck)

    player.hand.append(card)

    deck.remove(card)

    print(player.title  + ' received: ' + card.__str__())

def check_rank(card):
    if card.rank == 'Ace':
        return 1
    elif card.rank == 'Jack':
        return 10
    elif card.rank == 'Queen':
        return 10
    elif card.rank == 'King':
        return 10
    return card.rank

def add_to_pool(player, dealer,amount):
    player.wallet -= amount
    dealer.wallet += amount

def withdraw_from_pool(player, dealer, amount):
    player.wallet += amount
    dealer.wallet -= amount


if __name__ == "__main__":
    
    deck = make_deck()

    #random.shuffle(deck)

    player = Player('Player', 1000, [])
    dealer = Player('Dealer', 1000, [])

    deal_card(deck, player)
    deal_card(deck, dealer)
    deal_card(deck, player)
    deal_card(deck, dealer)

    for card in deck:
        print(card.__str__())

    print(len(deck))

    

        
    
    
