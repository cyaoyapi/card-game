"""Define the view used for TV."""


class BroadCastView:
    """Class representing view used for TV."""

    def prompt_for_player():
        """Prompt for a name."""
        None

    prompt_for_player = staticmethod(prompt_for_player)

    def show_player_hand(name, hand):
        """Show the player hand."""

        print(f"[TV] [Joueur {name}]")
        for card in hand:
            if card.is_up_face:
                print(card)
            else:
                print("(Carte face cachée.)")

        return None

    show_player_hand = staticmethod(show_player_hand)

    def prompt_for_flip_cards():
        """Request to return the cards."""
        return None

    prompt_for_flip_cards = staticmethod(prompt_for_flip_cards)

    def show_winner(name):
        """Show the winner."""
        print(f"[TV] Bravo {name}, tu as gagné(e)!")
        return None

    show_winner = staticmethod(show_winner)

    def prompt_for_new_game():
        """Request to replay."""

        return True

    prompt_for_new_game = staticmethod(prompt_for_new_game)








