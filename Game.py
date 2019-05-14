import random
from Card import Card
from Player import Player

def make_suit(deck, suit):
   
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

    deck = deck + make_suit([], 'Hearts')
    deck = deck + make_suit([], 'Clubs')
    deck = deck + make_suit([], 'Spades')
    deck = deck + make_suit([], 'Diamonds')

    return deck

def deal_card(player, deck):

    card = random.choice(deck)

    player.hand.append(card)

    deck.remove(card)

    if player.title == 'Dealer' and len(player.hand) == 2:
        print(player.title  + ' has: ' + player.hand[0].__str__())
        print(player.title  + ' has a face down card')
    elif player.title == 'Player':
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

def start_game():
    deck = make_deck()

    random.shuffle(deck)

    player = Player('Player', 1000, [])
    dealer = Player('Dealer', 1000, [])

    print('Welcome to Blackjack\nPlease choose yor role:\n1. Player\n2. Dealer\n3. Quit Game')
    
    choice = input()

    if choice == '1':
        print("Player chosen")
        start_player_game(player, dealer, deck)
    elif choice == '2':
        print("Dealer chosen")
    elif choice == '3':
        print("Game Quitting...")
        return False
    else:
        print('Wrong')

    #continue

def calculate_total_rank(player):
    sum_of_rank = 0
    for card in player.hand:
        sum_of_rank += check_rank(card)

    if sum_of_rank > 21:
        return 'lost'
    
    return sum_of_rank

def start_player_game(player, dealer, deck):
    deal_card(player, deck)
    deal_card(dealer, deck)
    deal_card(player, deck)
    deal_card(dealer, deck)

    game_in_progress = True

    while game_in_progress:
        player_options(player, deck)
        if calculate_total_rank(player) == 'lost':
            game_in_progress = False
    


def hit(player, deck):
    deal_card(player, deck)
    print('Player has ' + str(calculate_total_rank(player)))

def start_dealer_game():
    pass

def player_options(player, deck):

    print('Choose an action\n1. Hit\n2. Stand\n3. Split\n4. Surrender\n5. Insurance')

    choice = input()

    if choice == '1':
        hit(player, deck)
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    

if __name__ == "__main__":

    game_running = True

    while game_running:
        game_running = start_game()
        

    

        
    
    
