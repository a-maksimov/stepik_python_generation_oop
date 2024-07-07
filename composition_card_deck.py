from itertools import product
from random import shuffle


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'


class Deck:
    __suits = ("♣", "♢", "♡", "♠")
    __ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __init__(self):
        self.deck = [Card(*pair) for pair in product(self.__suits, self.__ranks)]

    def shuffle(self):
        if not len(self.deck) == 52:
            raise ValueError('Перемешивать можно только полную колоду')
        shuffle(self.deck)

    def deal(self):
        if not self.deck:
            raise ValueError('Все карты разыграны')
        return self.deck.pop()

    def __str__(self):
        return f'Карт в колоде: {len(self.deck)}'


deck = Deck()
pass
