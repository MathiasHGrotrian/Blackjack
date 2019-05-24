from Person import Person

class Player(Person):

    def __init__(self, title, wallet, hand):
        Person.__init__(self, title, wallet, hand)
        self.hasWon = False
        self.bet = 0
        self.is_splitting = False

    def calculate_total_rank(self):
        sum_of_rank = 0
        for card in self.hand[0]:
            sum_of_rank += self.check_rank(card)

        return sum_of_rank

    def calculate_split_rank(self, index):
        sum_of_rank = 0

        for card in self.hand[index]:
            sum_of_rank += self.check_rank(card)

        return sum_of_rank