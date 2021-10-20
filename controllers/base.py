"""define the main controller."""

from typing import List

from models.deck import Deck
from models.player import Player

MAX_NUMBER_OF_PLAYERS = 5


class Controller:
    """Class representing the main controller."""

    def __init__(self, deck: Deck, views, checker_scenario):
        # Models
        self.deck = deck
        self.players: List[Player] = []
        # Views
        self.views = views
        # Scenario of Checking
        self.checker_scenario = checker_scenario()

    def get_players(self):
        """Get some players."""
        while len(self.players) < MAX_NUMBER_OF_PLAYERS:
            names = []
            for view in self.views:
                printed_name = view.prompt_for_player()
                names.append(printed_name)

            if not any(names):
                return None

            for name in names:
                if name:
                    player = Player(name)
                    self.players.append(player)

    def start_game(self):
        """Shuffle the deck and makes the players draw a card."""
        self.deck.shuffle()
        for player in self.players:
            card = self.deck.draw_card()
            if card:
                player.hand.append(card)

    def evaluate_game(self):
        """Evaluate the best player."""

        return self.checker_scenario.checker(self.players)

    def rebuild_deck(self):
        """Rebuild the deck."""

        for player in self.players:
            while player.hand:
                card = player.hand.pop()
                card.is_up_face = False
                self.deck.append(card)

        self.deck.shuffle()

    def run(self):
        """Run the game."""

        self.get_players()
        running = True
        while running:
            self.start_game()
            for player in self.players:
                for view in self.views:
                    view.show_player_hand(player.name, player.hand)

            for view in self.views:
                view.prompt_for_flip_cards()

            for player in self.players:
                for card in player.hand:
                    card.is_up_face = True

                for view in self.views:
                    view.show_player_hand(player.name, player.hand)

            for view in self.views:
                view.show_winner(self.evaluate_game())

            for view in self.views:
                running = view.prompt_for_new_game()
                if not running:
                    return None

            self.rebuild_deck()


