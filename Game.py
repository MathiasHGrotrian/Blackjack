# main class running the program

import random

from Player import Player
from Dealer import Dealer

# adds money from a players wallet to a pool
def dealer_wins_pool(player, dealer):
    player.wallet -= player.bet
    dealer.wallet += player.bet
    print("You lost $", player.bet, "...\n")
    print("Your total is now: ", player.wallet)

# takes money from a players wallet to a pool
def player_wins_pool(player, dealer):
    player.wallet += player.bet
    dealer.wallet -= player.bet
    print("You won $", player.bet, "!\n")
    print("Your total is now: ", player.wallet)


# starts the game, creates and shuffles deck and prompts player to choose a role or quit
def start_game(game_running):

    player = Player('Player', 200, [])
    dealer = Dealer('Dealer', 1000, [])

    while game_running: 
        
        #Resets for a new round
        player.hand = []
        dealer.hand = []
        player.bet = 0
        deck = dealer.deck

        print('Welcome to Blackjack\nPlease choose yor role:\n1. Player\n2. Dealer\n3. Quit Game')
        
        choice = input()

        if choice == '1':
            print("\nPlayer chosen\n")
            start_player_game(player, dealer, deck.cards)
        elif choice == '2':
            print("\nDealer chosen\n")
        elif choice == '3':
            print("\nGame Quitting...")
            game_running = False
        else:
            print('\nInvalid choice.\nPlease enter a valid number\n')

# starts the game if player chooses to be a player and deals cards
# keeps game going until player has lost or won
def start_player_game(player, dealer, deck):

    place_bet(player)

    dealer.deal_card(player, deck)
    dealer.deal_card(dealer, deck)
    dealer.deal_card(player, deck)
    dealer.deal_card(dealer, deck)
    
    print('\nPlayer has ' + str(player.calculate_total_rank()))

    game_in_progress = True

    while game_in_progress:
        game_in_progress = player_options(player, deck, dealer)
    
    if(player.hasWon):
        player_wins_pool(player, dealer)
    else:
        dealer_wins_pool(player, dealer)


# takes card from deck and hand to player
# checks of player has lost or won
def hit(player, dealer, deck):

    dealer.deal_card(player, deck)
    print('\nPlayer has ' + str(player.calculate_total_rank()))

    return evaluate_hit_win_condition(player)

def stand(player, dealer, deck):
    print('\nPlayer has ' + str(player.calculate_total_rank()))
    print('\nDealers hidden card is: ' + dealer.hand[1].__str__())
    print('Dealer has ' + str(dealer.calculate_total_rank()))

    while(dealer.calculate_total_rank() < 17):
        dealer.deal_card(dealer, deck)
        print('\nDealer received ' + dealer.hand[len(dealer.hand) - 1].__str__())
        print('Dealer has ' + str(dealer.calculate_total_rank()) + '\n')

    return evaluate_stand_win_condition(player, dealer)
    
# checks if player has won or lost in case of player folding
# always returns false as game should be over when folding, no matter the outcome
# is also called when double down is selected
def evaluate_stand_win_condition(player, dealer):
    if player.calculate_total_rank() > 21:
        player.hasWon = False
        return False
    elif dealer.calculate_total_rank() > 21:
        player.hasWon = True
        return False
    elif(player.calculate_total_rank() > dealer.calculate_total_rank()):
        player.hasWon = True
        return False
    elif(player.calculate_total_rank() < dealer.calculate_total_rank()):
        player.hasWon = False
        return False
    elif(player.calculate_total_rank() == dealer.calculate_total_rank()):
        print("\nIt's a tie")
        player.hasWon = False
        return False

def double_down(player, dealer, deck):
    if(player.bet * 2 > player.wallet):
        print("You don't have enough money to double down with this bet")
    else:
        player.bet *= 2
        dealer.deal_card(player, deck)
        stand(player, dealer, deck)


def start_dealer_game():
    pass

# players options each turn
def player_options(player, deck, dealer):

    print('Dealer has ' + dealer.hand[0].__str__())

    print('-Choose an action\n1. Hit\n2. Stand\n3. Double Down\n4. Split\n5. Surrender\n 6. Insurance')
    
    choice = input()

    if choice == '1':
        return hit(player, dealer, deck)
    elif choice == '2':
        return stand(player, dealer, deck)
    elif choice == '3':
        return double_down(player, dealer, deck)
    elif choice == '4':
        pass
    elif choice == '5':
        pass

# uses players choice and acts accordingly
# returns false if game is over in any way, to break out of loop, else keep game going and return true
def evaluate_hit_win_condition(player):
    #bust
    if(player.calculate_total_rank() > 21):
        player.hasWon = False
        return False

    #perfect
    elif(player.calculate_total_rank() == 21):
        player.hasWon = True
        return False

    #continue hitting
    else:
        return True


# player can place a bet, which will be varified.
# returns current pool  
def place_bet(player):
    print("\nYou currently have ", player.wallet)
    print("\nPlace your bets:")

    ongoing_bet = True
    
    while(ongoing_bet):
        
        #makes sure that bet is numeric
        checkdigits = True
        while(checkdigits):
            bet = input()
            if(bet.isdigit()):
                bet = int(bet)
                checkdigits = False
            else:
                print("Please enter numbers, not letters\n")

        

        if(bet <= 0):
            print("Please place a valid amount\n")
            
        elif(bet > player.wallet):
            print("You don't have enough money to place that bet\n")
            
        else:
            player.bet += bet
            print("Your bet: ", bet)
            print("")
            ongoing_bet = False



if __name__ == "__main__":

    game_running = True

    start_game(game_running)
