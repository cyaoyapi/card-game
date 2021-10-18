import random
SUITS = ("diamonds", "coeurs", "piques", "carreaux")
RANKS = (
    "deux",
    "trois",
    "quatre",
    "cinq",
    "six",
    "sept",
    "huit",
    "neuf",
    "dix",
    "valet",
    "reine",
    "roi",
    "ace",
)


class Card:
    """Class representing cards."""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.is_up_face = False
        self._suit_score = SUITS.index(self.suit)
        self._rank_score = RANKS.index(self.rank)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.rank} de {self.suit}"

    def __lt__(self, other: "Card"):
        if self._rank_score != other._rank_score:
            return self._rank_score < other._rank_score
        return self._suit_score < other._suit_score


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
            self.pop()
        except IndexError:
            return None


if __name__ == "__main__":
    card1 = Card("diamonds", "cinq")
    card2 = Card("coeurs", "cinq")
    card3 = Card("coeurs", "valet")
    print(card1 < card2)
    print(card3 > card2)
    deck = Deck()
    print(deck)
    print(len(deck))

