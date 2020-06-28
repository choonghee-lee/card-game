class Player:
    KIND_CPU = 'cpu'
    KIND_PLAYER = 'player'

    def __init__(self, kind, money=10_000_000_000):
        self.kind = kind
        self.money = money
        self.cards = []
    
    def keep_card(self, card):
        self.cards.append(card)

    def return_card(self):
        return self.cards.pop()

    def bet_money(self, bet):
        money = 0            
        if bet == 'ALL-IN' or self.money < bet:
            money = self.money
            self.money = 0
            return money
        else:
            self.money -= bet
            return bet