"""Define the wrapper of views"""


class View:
    """Class representing a wrapper of views."""

    def __init__(self, active_view, passive_views):
        self.active_view = active_view
        self.passive_views = passive_views

    def prompt_for_player(self):
        """Prompt for a name."""
        return self.active_view.prompt_for_player()

    def show_player_hand(self, name, hand):
        """Show the player hand."""
        self.active_view.show_player_hand(name, hand)
        for passive_view in self.passive_views:
            passive_view.show_player_hand(name, hand)

    def prompt_for_flip_cards(self):
        """Request to return the cards."""
        return self.active_view.prompt_for_flip_cards()

    def show_winner(self, name):
        """Show the winner."""
        self.active_view.show_winner(name)
        for passive_view in self.passive_views:
            passive_view.show_winner(name)

    def prompt_for_new_game(self):
        """Request to replay."""
        return self.active_view.prompt_for_new_game()








