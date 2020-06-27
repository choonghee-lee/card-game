import random
import csv

from card import Card
from rank import Rank
from player import Player

class Game:
    # bet
    BET = 1_000_000_000
    
    # ranks
    def __init__(self):
        self.cards = []
        self.players = []
        self.first = None
        self.bet = None
        self.ranks = []
        self.__init_objects()
        self.__init_status()

    # def loop(self):
    #     while 

    def print(self):
        for card in self.cards:
            print(card.month, card.kind)

        for player in self.players:
            print(player.kind, player.money)

        for rank in self.ranks:
            print(rank.name, rank.ranking, rank.combination)

    def __init_objects(self):
        # initalize cards
        for i in range(1, 11):
            self.cards.append(Card(month=i, kind=Card.CARD_TYPE_YEOL))
            self.cards.append(Card(month=i, kind=Card.CARD_TYPE_PI))

        # initalize players
        for i in range(1, 5):
            self.players.append(Player(kind=Player.KIND_CPU+str(i)))
        self.players.append(Player(kind=Player.KIND_PLAYER))

    def __init_status(self):

        # 선
        random.shuffle(self.players)
        self.first = self.players[0]

        # 판돈
        self.bet = Game.BET

        # 족보
        with open('ranks.csv', 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for l in csv_reader:
                comb = set(zip(l[2::4], l[3::4], l[4::4], l[5::4]))
                self.ranks.append(Rank(name=l[0], ranking=l[1], combination=comb))


        