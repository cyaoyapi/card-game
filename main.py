from helpers import SUITS, RANKS, Card, Deck


class Hand(list):
    """Class representing the hand of a player."""

    def append(self, obj):
        if not isinstance(obj, Card):
            raise ValueError("On ne peut ajouter qu'une carte!")
        return super().append(obj)


class Player:
    """Class representing a player."""

    def __init__(self, name):
        self.name = name
        self.hand = Hand()


if __name__ == "__main__":
    player = Player("Cyrille")
    card = Card("diamonds", "valet")
    print(card)
    player.hand.append(card)
    print(player.hand[0])
    player.hand.append(1)

