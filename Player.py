
class Player:

    def __init__(self, title, wallet, hand):
        self.title = title
        self.wallet = wallet
        self.hand = hand
        self.hasWon = False

    # calculates the current total on a players hand
    def calculate_total_rank(self):
        sum_of_rank = 0
        for card in self.hand:
            sum_of_rank += self.check_rank(card)

        return sum_of_rank

    # converts a cards rank to a number
    def check_rank(self, card):
        if card.rank == 'Ace':
            return 1
        elif card.rank == 'Jack':
            return 10
        elif card.rank == 'Queen':
            return 10
        elif card.rank == 'King':
            return 10
        return card.rank
    