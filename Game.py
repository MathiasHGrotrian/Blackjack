import random
from Card import Card
from Deck import Deck
from Player import Player

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

        deck = Deck([])

        random.shuffle(deck.cards)

        player = Player('Player', 1000, [])
        dealer = Player('Dealer', 1000, [])

        print('Welcome to Blackjack\nPlease choose yor role:\n1. Player\n2. Dealer\n3. Quit Game')
        
        choice = input()

        if choice == '1':
            print("\nPlayer chosen\n")
            start_player_game(player, dealer, deck.cards)
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
    print('Player has ' + str(player.calculate_total_rank()))

    game_in_progress = True


    while game_in_progress:
        choice = player_options(player, deck, dealer, game_in_progress)
        game_in_progress = evaluate_win_condition(player, dealer, choice)

def hit(player, deck, game_in_progress):

    deal_card(player, deck)
    print('\nPlayer has ' + str(player.calculate_total_rank()))

    if(player.calculate_total_rank() > 21):
        print('You lost, bust\n')

    if(player.calculate_total_rank == 21):
        print('You won, exactly 21\n')
    

def stand(player, dealer):
    print('\n')
    if(player.calculate_total_rank() > dealer.calculate_total_rank()):
        print('You won!')
        return False
    elif(player.calculate_total_rank() < dealer.calculate_total_rank()):
        print('You lost')
        return False
    elif(player.calculate_total_rank() == dealer.calculate_total_rank()):
        print("It's a tie, you lost")
        return False
        

def start_dealer_game():
    pass

def player_options(player, deck, dealer, game_in_progress):

    print('Dealer has ' + dealer.hand[0].__str__())

    print('-Choose an action\n1. Hit\n2. Stand\n3. Split\n4. Surrender\n5. Insurance')
    
    choice = input()

    if choice == '1':
        hit(player, deck, game_in_progress)
        return choice
    elif choice == '2':
        #stand(player, deck, dealer, game_in_progress)
        return choice
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass

def evaluate_win_condition(player, dealer, choice):

    if(choice == '1'):
        if(player.calculate_total_rank() > 21):
            return False
        elif(player.calculate_total_rank() == 21):
            return False
        else:
            return True

    if(choice == '2'):
        return stand(player, dealer)
        


    #elif((compare_hands(player, dealer) == 'lost' or compare_hands(player, dealer) == 'won') and ()):
    #    return False

if __name__ == "__main__":

    game_running = True

    start_game(game_running)
