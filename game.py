from card import Card
from player import Player

class Game:
    # first
    # bet
    # ranks

    def __init__(self):
        self.cards = []
        self.players = []
        self.__init_objects()

    def __init_objects(self):
        
        # initalize cards
        for i in range(1, 11):
            self.cards.append(Card(month=i, kind=Card.CARD_TYPE_YEOL))
            self.cards.append(Card(month=i, kind=Card.CARD_TYPE_PI))

        # initalize players
        for i in range(1, 5):
            self.players.append(Player(kind=Player.KIND_CPU+str(i)))
        self.players.append(Player(kind=Player.KIND_PLAYER))

    def print(self):
        for card in self.cards:
            print(card.month, card.kind)

        for player in self.players:
            print(player.kind, player.money)