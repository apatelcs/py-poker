import random

class Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

    def __str__(self):
        return f'{self.val} of {self.suit}'


class Deck:
    def __init__(self):
        self.cards = []
        self.make_deck()

    def make_deck(self):
        for suit in ['spade', 'heart', 'clover', 'diamond']:
            for val in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']:
                self.cards.append(Card(val, suit))
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop(0)

    def __str__(self):
        output = ''

        for card in self.cards:
            output += str(card) + '\n'
        
        return output


class Player:
    def __init__(self, money, is_small, is_big):
        self.money = money
        self.is_small = is_small
        self.is_big = is_big

    def set_small(self):
        self.is_big = False
        self.is_small = True

    def set_big(self):
        self.is_big = True
        self.is_small = False

    def set_no_blind(self):
        self.is_big = False
        self.is_small = False

    def bet(self, amt):
        self.money = self.money - amt

    def win_amt(self, amt):
        self.money = self.money + amt