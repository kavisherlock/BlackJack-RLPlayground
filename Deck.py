import random


class Deck:
    def __init__(self, seed=9000):
        random.seed(seed)

        self.deck = []
        for number in range(1, 14):
            for suit in ['S', 'C', 'H', 'D']:
                self.deck.append(Card(suit, number))

        self.shuffle_deck()

    def add_card(self, card):
        self.deck.append(card)

    def remove_card(self, card):
        self.deck.remove(card)

    def pop_card(self):
        return self.deck.pop()

    def shuffle_deck(self):
        random.shuffle(self.deck)


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def get_value(self):
        return min(self.number, 10)

    def get_suit(self):
        return self.suit

    def get_color(self):
        if self.suit == 'S' or self.suit == 'C':
            return 'black'

        return 'red'