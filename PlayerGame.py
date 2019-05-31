import Game

# starts the game if player chooses to be a player and deals cards
# keeps game going until player has lost or won
def start_player_game(player, dealer, deck):

    player.place_bet()

    dealer.deal_player_card(player, deck)
    dealer.deal_dealer_card(dealer, deck)
    dealer.deal_player_card(player, deck)
    dealer.deal_dealer_card(dealer, deck)
    
    print('\nPlayer has ' + str(player.calculate_total_rank()))

    game_in_progress = True

    while game_in_progress:
        game_in_progress = player_options(player, dealer, deck)

    
    if (player.is_splitting):
        print('\nPlayer has second hand ' + str(player.calculate_split_rank(1)))
        if(player.splitWon):
            Game.player_wins_pool(player, dealer)
            player.is_splitting = False
            print("You won $", player.bet, " on second hand!\n")
        else:
            Game.dealer_wins_pool(player, dealer)
            player.is_splitting = False
            print("You lost $", player.bet, " on second hand...\n")


    # print('\nPlayer has fist hand ' + str(player.calculate_split_rank(0)))

    if(player.hasWon):
        Game.player_wins_pool(player, dealer)
        print("You won $", player.bet, "!\n")
        print("Player total is now: ", player.wallet)
        print("Dealer total is now: ", dealer.wallet, "\n")

    elif(player.is_surrendering):
        player.wallet -= player.bet / 2
        dealer.wallet += player.bet / 2
        player.is_surrendering = False

    else:
        Game.dealer_wins_pool(player, dealer)
        print("You lost $", player.bet, "...\n")
        print("Player total is now: ", player.wallet)
        print("Dealer total is now: ", dealer.wallet, "\n")

# players options each turn
def player_options(player, dealer, deck):

    print('Dealer has ' + dealer.hand[0].__str__())

    print('-Choose an action\n1. Hit\n2. Stand\n3. Double Down\n4. Split\n5. Surrender')
    
    choice = input()

    if choice == '1':
        return Game.hit(player, dealer, deck)
    elif choice == '2':
        return Game.stand(player, dealer, deck)
    elif choice == '3':
        return Game.double_down(player, dealer, deck)
    elif choice == '4':
        return Game.split(player, dealer, deck)
    elif choice == '5':
        return Game.surrender(player, dealer)
    else:
        print("Please select a valid option")
        return True
