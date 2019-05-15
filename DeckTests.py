# test module for Deck class

import unittest
from Deck import Deck

def test_make_suit(deck, suit, exp_suit):
    assert deck.make_suit([], suit)[0].suit == exp_suit, "Should be " + exp_suit


if __name__ == "__main__":
    deck = Deck([])

    deck.cards = []

    test_make_suit(deck, 'Spades', 'Hearts') 