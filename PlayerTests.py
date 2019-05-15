
import unittest
from Player import Player
from Card import Card



def test_calc_total_rank(player):
    
    assert player.calculate_total_rank() == 21, 'Should be 21'


if __name__ == "__main__":
    player = Player('Player', 1000, [Card("h",10),Card("h",1) ])

    test_calc_total_rank(player)