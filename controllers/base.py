"""define the main controller."""

from typing import List

from models.deck import Deck
from models.player import Player


class Controller:
    """Class representing the main controller."""

    def __init__(self, deck: Deck):
        # Models
        self.deck = deck
        self.players: List[Player] = []
        # Views
        self.view = None

    def get_players(self):
        """Get some players."""
        while len(self.players) < 5:
            name = self.view.prompt_for_player()
            if not name:
                return None
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

        best_player = self.players[0]
        for player in self.players[1:]:
            player_card = player.hand[0]
            best_player_card = best_player.hand[0]
            if player_card > best_player_card:
                best_player = player

        return best_player.name

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
                self.view.show_player_hand(player.name, player.hand)

            self.view.prompt_for_flip_cards()
            for player in self.players:
                for card in player.hand:
                    card.is_up_face = True
                self.view.show_player_hand(player.name, player.hand)

            self.view.show_winner(self.evaluate_game())
            running = self.view.prompt_for_new_game()
            self.rebuild_deck()


