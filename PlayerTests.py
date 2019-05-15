# test module for Player class

import unittest
from Player import Player
from Card import Card



def test_calc_total_rank(player, exp_total):
    
    assert player.calculate_total_rank() == exp_total, 'Should be ' + str(exp_total)

def test_check_rank_aces(player, card, exp_rank):

    assert player.check_rank(card) == exp_rank, 'Should be ' + str(exp_rank)

def test_check_rank_face_cards(player, card, exp_rank):

    assert player.check_rank(card) == exp_rank , 'Should be ' + str(exp_rank)


if __name__ == "__main__":

    ace_card = Card('Heart', 'Ace')
    jack_card = Card('Heart', 'Jack')

    player = Player('Player', 1000, [Card('Heart', 10),Card('Heart', 5) ])

    test_calc_total_rank(player, 15)
    test_check_rank_aces(player, ace_card, 1)
    test_check_rank_face_cards(player, jack_card, 10)
