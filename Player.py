
class Player:

    def __init__(self, title, wallet, hand):
        self.title = title
        self.wallet = wallet
        self.hand = hand

    
    def calculate_total_rank(self):
        sum_of_rank = 0
        for card in self.hand:
            sum_of_rank += self.check_rank(card)

        if sum_of_rank > 21:
            return 'lost'
        
        if sum_of_rank == 21:
            return 'won'

        return sum_of_rank

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
    