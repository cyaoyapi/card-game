"""Entry point"""

from models.deck import Deck
from views.player import PlayerView
from views.broadcast import BroadCastView
from views.internet import InternetStreamingView
from views.base import View
from controllers.checkers import CheckerHighRankAndSuitIndex
from controllers.base import Controller


def main():
    """Main program."""

    deck = Deck()
    active_view = PlayerView()
    passive_views = (BroadCastView, InternetStreamingView)
    view = View(active_view, passive_views)
    game = Controller(deck, view, CheckerHighRankAndSuitIndex)
    game.run()


if __name__ == "__main__":
    main()
