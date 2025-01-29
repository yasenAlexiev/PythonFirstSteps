import random
from enum import Enum

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values_for_war = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
                  'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
values_for_blackjack = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
                        'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Game(Enum):
    WAR = 1,
    BLACKJACK = 2


class Card:

    def __init__(self, suit, rank, game):
        self.suit = suit
        self.rank = rank
        if game == Game.WAR:
            self.value = values_for_war[rank]
        elif game == Game.BLACKJACK:
            self.value = values_for_blackjack[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self, game):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank, game))

    def shuffle_cards(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.player_cards = []

    def remove_one(self):
        return self.player_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.player_cards.extend(new_cards)
        else:
            self.player_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.player_cards)} cards."


class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner:   {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print("Withdrawal Accepted")
