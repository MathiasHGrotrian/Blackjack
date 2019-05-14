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
        print('Card dealt - ' + player.title  + ' has: ' + player.hand[0].__str__())
        print('Card dealt - ' + player.title  + ' has a face down card')
    elif player.title == 'Player':
        print('Card dealt - ' + player.title  + ' received: ' + card.__str__())

def add_to_pool(player, dealer,amount):
    player.wallet -= amount
    dealer.wallet += amount

def withdraw_from_pool(player, dealer, amount):
    player.wallet += amount
    dealer.wallet -= amount

def start_game(game_running):
    while game_running:
        deck = make_deck()

        random.shuffle(deck)

        player = Player('Player', 1000, [])
        dealer = Player('Dealer', 1000, [])

        print('Welcome to Blackjack\nPlease choose yor role:\n1. Player\n2. Dealer\n3. Quit Game')
        
        choice = input()

        if choice == '1':
            print("\nPlayer chosen\n")
            start_player_game(player, dealer, deck)
        elif choice == '2':
            print("Dealer chosen")
        elif choice == '3':
            print("Game Quitting...")
            game_running = False
        else:
            print('Wrong')


def start_player_game(player, dealer, deck):
    deal_card(player, deck)
    deal_card(dealer, deck)
    deal_card(player, deck)
    deal_card(dealer, deck)
    print('\n')

    game_in_progress = True

    while game_in_progress:
        player_options(player, deck, dealer, game_in_progress)
        if player.calculate_total_rank() == 'lost':
            game_in_progress = False
    


def hit(player, deck):
    print('\n')
    deal_card(player, deck)

    #if your hit exceeds 21 it should return you lost

def stand(player, deck, dealer, game_in_progress):
    print('\n')
    if player.calculate_total_rank() > dealer.calculate_total_rank():
        print('You won!')
        game_in_progress = False
        #needs to exit the game in progress and not print the options again
    elif player.calculate_total_rank() < dealer.calculate_total_rank():
        print('You lost')
        game_in_progress = False
    elif dealer.calculate_total_rank() > 21:
        print('You won. Dealer bust')
        game_in_progress = False
    else:
        print('Its a tie. You lose')
        game_in_progress = False

def start_dealer_game():
    pass

def player_options(player, deck, dealer, game_in_progress):

    print('Player has ' + str(player.calculate_total_rank()))
    print('Dealer has ' + player.hand[0].__str__())

    print('-Choose an action\n1. Hit\n2. Stand\n3. Split\n4. Surrender\n5. Insurance')
    
    choice = input()

    if choice == '1':
        hit(player, deck)
    elif choice == '2':
        stand(player, deck, dealer, game_in_progress)
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    

if __name__ == "__main__":

    game_running = True

    start_game(game_running)
