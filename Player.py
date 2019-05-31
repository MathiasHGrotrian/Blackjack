from Person import Person

class Player(Person):

    def __init__(self, title, wallet, hand):
        Person.__init__(self, title, wallet, hand)
        self.hasWon = False
        self.splitWon = False
        self.bet = 0
        self.is_splitting = False
        self.is_surrendering = False

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

    # player can place a bet, which will be varified.
    # returns current pool  
    def place_bet(self):
        print("\nYou currently have ", self.wallet)
        print("\nPlace your bets:")

        ongoing_bet = True
        
        while(ongoing_bet):
            
            #makes sure that bet is numeric
            checkdigits = True
            while(checkdigits):
                bet = input()
                if(bet.isdigit()):
                    bet = int(bet)
                    checkdigits = False
                else:
                    print("Please enter numbers, not letters\n")

            

            if(bet <= 0):
                print("Please place a valid amount\n")
                
            elif(bet > self.wallet):
                print("You don't have enough money to place that bet\n")
                
            else:
                self.bet += bet
                print("Your bet: ", bet)
                print("")
                ongoing_bet = False
