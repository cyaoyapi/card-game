"""Entry point"""

from models.deck import Deck
from views.base import PlayerView
from views.broadcast import BroadCastView
from views.internet import InternetStreamingView
from controllers.checkers import CheckerHighRankAndSuitIndex
from controllers.base import Controller


def main():
    """Main program."""

    deck = Deck()
    views = (PlayerView, BroadCastView, InternetStreamingView)
    game = Controller(deck, views, CheckerHighRankAndSuitIndex)
    game.run()


if __name__ == "__main__":
    main()

