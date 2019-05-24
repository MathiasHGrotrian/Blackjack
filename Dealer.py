import random
from Person import Person
from Deck import Deck

class Dealer(Person):

    def __init__(self, title, wallet, hand):
        Person.__init__(self, title, wallet, hand)
        self.deck = Deck([])

    # deals card to a player
    # prints the received card and hides a card if player is a dealer
    def deal_player_card(self, player, deck):

        card = random.choice(deck)

        player.hand[0].append(card)

        deck.remove(card)

        print('Card dealt - ' + player.title  + ' received: ' + card.__str__())

    # deals card to dealer
    def deal_dealer_card(self, dealer, deck):
        
        card = random.choice(deck)

        dealer.hand.append(card)

        deck.remove(card)

        if len(dealer.hand) == 2:
            print('Card dealt - ' + dealer.title  + ' has: ' + dealer.hand[0].__str__())
            print('Card dealt - ' + dealer.title  + ' has a face down card')

    def deal_split(self, player, deck, index):

        card = random.choice(deck)

        player.hand[index].append(card)

        deck.remove(card)
        print('Card dealt - ' + player.title  + ' received: ' + card.__str__())
        