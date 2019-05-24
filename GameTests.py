
import unittest
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

def test_split(player, dealer, deck, exp_result):
    assert Game.split(player, dealer, deck) == exp_result, 'Should be ' + str(exp_result)

if __name__ == "__main__":
    player = Player('Player', 1000, [Card('Hearts', 10),Card('Clubs', 10) ])
    dealer = Dealer('Dealer', 1000, [Card('Spades', 10),Card('Hearts', 2) ])

    #test_evaluate_win_condition(player, dealer, '2', True)
    #test_place_bet(player, 0, 50)
    test_split(player, dealer, dealer.deck.cards, True)