# main class running the program

import random
from Card import Card
from Deck import Deck
from Player import Player

# deals card to a player
# prints the received card and hides a card if player is a dealer
def deal_card(player, deck):

    card = random.choice(deck)

    player.hand.append(card)

    deck.remove(card)

    if player.title == 'Dealer' and len(player.hand) == 2:
        print('Card dealt - ' + player.title  + ' has: ' + player.hand[0].__str__())
        print('Card dealt - ' + player.title  + ' has a face down card')
    elif player.title == 'Player':
        print('Card dealt - ' + player.title  + ' received: ' + card.__str__())

# adds money from a players wallet to a pool
def dealer_wins_pool(player, dealer, current_pool):
    player.wallet -= current_pool
    dealer.wallet += current_pool
    print("You lost $", current_pool, "...\n")
    print("Your total is now: ", player.wallet)

# takes money from a players wallet to a pool
def player_wins_pool(player, dealer, current_pool):
    player.wallet += current_pool
    dealer.wallet -= current_pool
    print("You won $", current_pool, "!\n")
    print("Your total is now: ", player.wallet)


# starts the game, creates and shuffles deck and prompts player to choose a role or quit
def start_game(game_running):

    player = Player('Player', 200, [])
    dealer = Player('Dealer', 1000, [])

    while game_running: 
        
        #Resets for a new round
        player.hand = []
        dealer.hand = []
        current_pool = 0
        deck = Deck([])

        print('Welcome to Blackjack\nPlease choose yor role:\n1. Player\n2. Dealer\n3. Quit Game')
        
        choice = input()

        if choice == '1':
            print("\nPlayer chosen\n")
            start_player_game(player, dealer, deck.cards, current_pool)
        elif choice == '2':
            print("\nDealer chosen\n")
        elif choice == '3':
            print("\nGame Quitting...")
            game_running = False
        else:
            print('\nInvalid choice.\nPlease enter a valid number\n')

# starts the game if player chooses to be a player and deals cards
# keeps game going until player has lost or won
def start_player_game(player, dealer, deck, current_pool):

    current_pool = place_bet(player, current_pool)

    deal_card(player, deck)
    deal_card(dealer, deck)
    deal_card(player, deck)
    deal_card(dealer, deck)
    
    print('\nPlayer has ' + str(player.calculate_total_rank()))

    game_in_progress = True

    while game_in_progress:
        choice = player_options(player, deck, dealer, game_in_progress)
        game_in_progress = evaluate_win_condition(player, dealer, choice)
    
    if(player.hasWon):
        player_wins_pool(player, dealer, current_pool)
    else:
        dealer_wins_pool(player, dealer, current_pool)


# takes card from deck and hand to player
# checks of player has lost or won
def hit(player, deck, game_in_progress):

    deal_card(player, deck)
    print('\nPlayer has ' + str(player.calculate_total_rank()))

    if(player.calculate_total_rank() > 21):
        print('\nYou lost, bust')

    if(player.calculate_total_rank == 21):
        print('\nYou won, exactly 21')
    
# checks if player has won or lost in case of player folding
# always returns false as game should be over when folding, no matter the outcome
def stand(player, dealer):
    if(player.calculate_total_rank() > dealer.calculate_total_rank()):
        print('\nYou won!')
        player.hasWon = True
        return False
    elif(player.calculate_total_rank() < dealer.calculate_total_rank()):
        print('\nYou lost')
        player.hasWon = False
        return False
    elif(player.calculate_total_rank() == dealer.calculate_total_rank()):
        print("\nIt's a tie, you lost")
        player.hasWon = False
        return False
        

def start_dealer_game():
    pass

# players options each turn
def player_options(player, deck, dealer, game_in_progress):

    print('Dealer has ' + dealer.hand[0].__str__())

    print('-Choose an action\n1. Hit\n2. Stand\n3. Split\n4. Surrender\n5. Insurance')
    
    choice = input()

    if choice == '1':
        hit(player, deck, game_in_progress)
        return choice
    elif choice == '2':
        #stand(player, deck, dealer, game_in_progress)
        #stand is called in evaluate_win_condition!
        return choice
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass

# uses players choice and acts accordingly
# returns false if game is over in any way, to break out of loop, else keep game going and return true
def evaluate_win_condition(player, dealer, choice):

    if(choice == '1'):
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

    if(choice == '2'):
        return stand(player, dealer)

# player can place a bet, which will be varified.
# returns current pool  
def place_bet(player, current_pool):
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
            current_pool += bet
            print("Your bet: ", bet)
            print("")
            ongoing_bet = False
            return current_pool



if __name__ == "__main__":

    game_running = True

    start_game(game_running)
