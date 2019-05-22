
import unittest
from Player import Player
import Game
from Card import Card


def test_evaluate_win_condition(player, dealer, choice, exp_bool):
    assert Game.evaluate_win_condition(player, dealer, choice) == exp_bool, 'Should be ' + str(exp_bool)

def test_place_bet(player, current_pool, exp_int):
    assert Game.place_bet(player, current_pool) == exp_int, 'Should be ' + str(exp_int)


if __name__ == "__main__":
    player = Player('Player', 1000, [Card('Hearts', 10),Card('Hearts', 5) ])
    dealer = Player('Dealer', 1000, [Card('Spades', 10),Card('Hearts', 2) ])

    test_evaluate_win_condition(player, dealer, '2', True)
    test_place_bet(player, 0, 50)