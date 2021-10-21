"""Define the view used for Internet streaming."""


class InternetStreamingView:
    """Class representing view used for Internet streaming."""

    def show_player_hand(name, hand):
        """Show the player hand."""

        print(f"[Internet] [Joueur {name}]")
        for card in hand:
            if card.is_up_face:
                print(card)
            else:
                print("(Carte face cachée.)")

        return None

    show_player_hand = staticmethod(show_player_hand)

    def show_winner(name):
        """Show the winner."""
        print(f"[Internet] Bravo {name}, tu as gagné(e)!")
        return None

    show_winner = staticmethod(show_winner)
