"""Define the view used by players."""


class PlayerView:
    """Class representing the card game view."""

    def prompt_for_player():
        """Prompt for a name."""

        name = input("Entrez le nom d'un joueur : ")
        if not name:
            return None
        return name

    prompt_for_player = staticmethod(prompt_for_player)

    def show_player_hand(name, hand):
        """Show the player hand."""

        print(f"[Joueur {name}]")
        for card in hand:
            if card.is_up_face:
                print(card)
            else:
                print("(Carte face cachée.)")

        return None

    show_player_hand = staticmethod(show_player_hand)

    def prompt_for_flip_cards():
        """Request to return the cards."""

        print()
        print("Prêts à retourner les cards ....")
        return None

    prompt_for_flip_cards = staticmethod(prompt_for_flip_cards)

    def show_winner(name):
        """Show the winner."""
        print(f"Bravo {name}, tu as gagné(e)!")
        return None

    show_winner = staticmethod(show_winner)

    def prompt_for_new_game():
        """Request to replay."""
        print("Souhaitez-vous refaire une partie ? ")
        choice = input("Tapez Y (Oui) ou N (Non) : ")
        if choice.upper() == "N":
            print("Fin du jeu. Au revoir!")
            return False
        return True

    prompt_for_new_game = staticmethod(prompt_for_new_game)
