from Person import Person

class Player(Person):

    def __init__(self, title, wallet, hand):
        Person.__init__(self, title, wallet, hand)
        self.hasWon = False
        self.bet = 0