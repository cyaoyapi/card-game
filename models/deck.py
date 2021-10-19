import random
from .card import SUITS, RANKS, Card


class Deck(list):
    """Class representing the deck of cards."""

    def __init__(self):
        for rank in RANKS:
            for suit in SUITS:
                card = Card(suit, rank)
                self.append(card)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self)

    def draw_card(self):
        try:
            return self.pop()
        except IndexError:
            return None


if __name__ == "__main__":
    deck = Deck()
    print(deck)
    print(len(deck))
