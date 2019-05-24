import random
from Person import Person
from Deck import Deck

class Dealer(Person):

    def __init__(self, title, wallet, hand):
        Person.__init__(self, title, wallet, hand)
        self.deck = Deck([])

    # deals card to a player
    # prints the received card and hides a card if player is a dealer
    def deal_card(self, player, deck):

        card = random.choice(deck)

        player.hand.append(card)

        deck.remove(card)

        if player.title == 'Dealer' and len(player.hand) == 2:
            print('Card dealt - ' + player.title  + ' has: ' + player.hand[0].__str__())
            print('Card dealt - ' + player.title  + ' has a face down card')
        elif player.title == 'Player':
            print('Card dealt - ' + player.title  + ' received: ' + card.__str__())