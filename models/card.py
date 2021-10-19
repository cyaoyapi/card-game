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

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.rank} de {self.suit}"


if __name__ == "__main__":
    card1 = Card("diamonds", "cinq")
    card2 = Card("coeurs", "cinq")
    card3 = Card("coeurs", "valet")
    print(card1 < card2)
    print(card3 > card2)
