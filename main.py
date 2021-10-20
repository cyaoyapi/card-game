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
    active_view = PlayerView()
    views = (BroadCastView, InternetStreamingView)
    game = Controller(deck, active_view, views, CheckerHighRankAndSuitIndex)
    game.run()


if __name__ == "__main__":
    main()

