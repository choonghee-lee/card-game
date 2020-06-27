class Player:
    KIND_CPU = 'cpu'
    KIND_PLAYER = 'player'

    def __init__(self, kind, money=10_000_000_000):
        self.kind = kind
        self.money = money