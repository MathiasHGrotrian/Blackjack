
import unittest
import DealerGame
import PlayerGame

from Player import Player
from Dealer import Dealer
import Game
from Card import Card


def test_evaluate_win_condition(player, dealer, choice, exp_bool):
    #assert Game.evaluate_win_condition(player, dealer, choice) == exp_bool, 'Should be ' + str(exp_bool)
    pass

def test_place_bet(player, current_pool, exp_int):
    #assert Game.place_bet(player, current_pool) == exp_int, 'Should be ' + str(exp_int)
    pass

def test_hit(player, dealer, deck):
    myBoolean = Game.hit(player, dealer, deck)

    #Bust
    if player.calculate_total_rank() > 21:
        assert myBoolean == False, 'Should be ' + str(False)
    #perfect
    elif(player.calculate_total_rank() == 21):
        assert myBoolean == True, 'Should be ' + str(True)
    #continue hitting
    else:
        assert myBoolean == True, 'Should be ' + str(True)

def test_stand(player, dealer, deck):
    
    Game.stand(player, dealer, deck)

    myBoolean =  player.hasWon
    if player.calculate_total_rank() > 21:
        assert myBoolean == False, 'Should be ' + str(False)
        return
    elif dealer.calculate_total_rank() > 21:
        assert myBoolean == True, 'Should be ' + str(True)
        return
    elif(player.calculate_total_rank() > dealer.calculate_total_rank()):
        assert myBoolean == True, 'Should be ' + str(True)
        return
    elif(player.calculate_total_rank() < dealer.calculate_total_rank()):
        assert myBoolean == False, 'Should be ' + str(False)
        return
    elif(player.calculate_total_rank() == dealer.calculate_total_rank()):
        assert myBoolean == False, 'Should be ' + str(False)
        return
       

def test_split(player, dealer, deck, exp_result):
    assert Game.split(player, dealer, deck) == exp_result, 'Should be ' + str(exp_result)


#AI Method
def test_ai_moves(player, dealer, deck, exp_result):
    assert DealerGame.ai_choices(player, dealer, deck) == exp_result, 'Should be ' + str(exp_result)

if __name__ == "__main__":

    #setup for test the game´s methods
    player = Player('Player', 1000, [[]])
    dealer = Dealer('Dealer', 1000, [])
    deck = dealer.deck.cards 
    
    '''
    dealer.deal_player_card(player, deck)
    dealer.deal_dealer_card(dealer, deck)
    dealer.deal_player_card(player, deck)
    dealer.deal_dealer_card(dealer, deck)
    '''

    #hit test
    #needs to check in the return if the boolean is correct to continue game!
    #test_hit(player, dealer, dealer.deck.cards)

    #stand test
    #test if winning boolean is set correct when call!
    #test_stand(player, dealer, deck)

    #split test
    #needs to check boolean in return for continue game
    '''
    player = Player('Player', 1000, [[Card('Hearts', 10),Card('Clubs', 10) ]])
    dealer = Dealer('Dealer', 1000, [Card('Spades', 10),Card('Hearts', 2) ])
    test_split(player, dealer, dealer.deck.cards, False)
    '''

    #test_evaluate_win_condition(player, dealer, '2', True)
    #test_place_bet(player, 0, 50)

    #Test AI Split
    '''
    #Split
    player_ai = Player('Player', 1000, [[Card('Hearts', 10),Card('Clubs', 10) ]])
    dealer_ai = Dealer('Dealer', 1000, [Card('Spades', 10),Card('Hearts', 2) ])
    test_ai_moves(player_ai, dealer_ai, deck, False)
    '''

    '''
    #Hit
    player_ai = Player('Player', 1000, [[Card('Hearts', 4),Card('Clubs', 3) ]])
    dealer_ai = Dealer('Dealer', 1000, [Card('Spades', 10),Card('Hearts', 2) ])
    test_ai_moves(player_ai, dealer_ai, deck, True)
    '''

    '''
    #Surrender
    player_ai = Player('Player', 1000, [[Card('Hearts', 10),Card('Clubs', 4)]])
    dealer_ai = Dealer('Dealer', 1000, [Card('Spades', 10),Card('Hearts', 2)])
    test_ai_moves(player_ai, dealer_ai, deck, False)
    '''

    '''
    #Double down
    player_ai = Player('Player', 1000, [[Card('Hearts', 4),Card('Clubs', 5)]])
    dealer_ai = Dealer('Dealer', 1000, [Card('Spades', 10),Card('Hearts', 2)])
    test_ai_moves(player_ai, dealer_ai, deck, False)
    '''

    #Stand
    player_ai = Player('Player', 1000, [[Card('Hearts', 10),Card('Clubs', 9)]])
    dealer_ai = Dealer('Dealer', 1000, [Card('Spades', 10),Card('Hearts', 2)])
    test_ai_moves(player_ai, dealer_ai, deck, False)


    #Test double down