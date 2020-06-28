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
        # self.first = None
        self.current_bet = 0
        self.ranks = []
        self.choices = None
        self.choice = None
        self.__init_objects()
        self.__init_status()

    def loop(self):
        random.shuffle(self.cards)
        self.__distribute_cards()
        self.__retrieve_bet_from_players()
        index = random.randint(0, len(self.choices) - 1)
        self.__check_rank()
        self.__make_players_bet(self.choices[index])
        self.__retrieve_cards()

    def __check_rank(self):
        current_rank = []
        player_comb = None
        for player in self.players:
            if player.cards[0].month < player.cards[1].month:
                player_comb = (
                    str(player.cards[0].month), player.cards[0].kind,
                    str(player.cards[1].month), player.cards[1].kind
                ) 
            else:
                player_comb = (
                    str(player.cards[1].month), player.cards[1].kind,
                    str(player.cards[0].month), player.cards[0].kind
                )
            print(player_comb)
            for rank in self.ranks:
                if player_comb in rank.combination:
                    current_rank.append(rank)
                    print(rank.name, rank.ranking)
                    break
        print(len(current_rank))
        
    # 각 플레이어에게 카드 한 장 분배
    def __distribute_cards(self):
        for player in self.players:
            player.keep_card(self.cards.pop())
            player.keep_card(self.cards.pop())

    # 모든 플레이어로 부터 카드 두 장씩 회수
    def __retrieve_cards(self):
        for player in self.players:
            self.cards.append(player.return_card())
            self.cards.append(player.return_card())

    # 참여금 회수
    def __retrieve_bet_from_players(self):
        for player in self.players:
            player.bet_money(Game.BET)
            self.current_bet += Game.BET

    # 배팅
    def __make_players_bet(self, bet):
        for player in self.players:
            money = player.bet_money(bet)
            self.current_bet += money

    # def print(self):
        # for card in self.cards:
        #     print(card.month, card.kind)

        # for player in self.players:
        #     print(player.kind, player.money)

        # for rank in self.ranks:
        #     print(rank.name, rank.ranking, rank.combination)

    def __init_objects(self):
        # initalize cards
        for i in range(1, 11):
            self.cards.append(Card(month=i, kind=Card.CARD_TYPE_YEOL))
            self.cards.append(Card(month=i, kind=Card.CARD_TYPE_PI))

        # initalize players
        for i in range(1, 5):
            self.players.append(Player(kind=Player.KIND_CPU+str(i)))
        self.players.append(Player(kind=Player.KIND_PLAYER))

        self.choices = [
            Game.BET, Game.BET, Game.BET, Game.BET, Game.BET, 
            Game.BET * 2, Game.BET * 2, Game.BET * 2, Game.BET * 2,
            Game.BET, Game.BET, Game.BET, Game.BET, Game.BET,
            Game.BET * 3, Game.BET * 3, Game.BET * 3, 
            Game.BET, Game.BET, Game.BET, Game.BET, Game.BET,
            Game.BET * 5, Game.BET * 5, 
            Game.BET, Game.BET, Game.BET, Game.BET, Game.BET,
            Game.BET * 10, 
            Game.BET, Game.BET, Game.BET, Game.BET, Game.BET,
            'ALL-IN'
         ] 

    def __init_status(self):

        # 선
        random.shuffle(self.players)
        # self.first = self.players[0]

        # 족보
        with open('ranks.csv', 'r', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for l in csv_reader:
                comb = set(zip(l[2::4], l[3::4], l[4::4], l[5::4]))
                self.ranks.append(Rank(name=l[0], ranking=l[1], combination=comb))

    # import keyboard
    # __selected = 1
    #     def __display_menu(self):
    #     print("Choose an option:")
    #     print("{1} {0}. Start Game {0} {2}".format(1, ">>" if self.__selected == 1 else "  ", "<<" if self.__selected == 1 else "  "))
    #     print("{1} {0}. Exit {0} {2}".format(2, ">>" if self.__selected == 2 else "  ", "<<" if self.__selected == 2 else "  "))

    # def __on_key_pressed_up(self):
    #     if self.__selected == 1:
    #         return
    #     self.__selected -= 1
    #     self.__display_menu()

    # def __on_key_pressed_down(self):
    #     if self.__selected == 2:
    #         return
    #     self.__selected += 1
    #     self.__display_menu()

    # self.__display_menu()
    #     keyboard.add_hotkey('up', self.__on_key_pressed_up)
    #     keyboard.add_hotkey('down', self.__on_key_pressed_down)
    #     keyboard.wait()

        