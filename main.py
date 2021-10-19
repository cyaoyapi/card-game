"""Entry point"""

from models.deck import Deck
from views.base import View
from controllers.base import Controller


def main():
    """Main program."""

    deck = Deck()
    view = View()
    game = Controller(deck, view)
    game.run()


if __name__ == "__main__":
    main()

