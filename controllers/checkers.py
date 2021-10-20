"""Classes evaluations scenarios"""

from models.card import SUITS, RANKS


class CheckerHighRankAndSuitIndex:

    def checker(players):
        """Evaluate the best player."""

        best_player = players[0]

        for player in players[1:]:
            player_card = player.hand[0]
            player_scores = (
                RANKS.index(player_card.rank),
                SUITS.index(player_card.suit)
            )

            best_player_card = best_player.hand[0]
            best_player_scores = (
                RANKS.index(best_player_card.rank),
                SUITS.index(best_player_card.suit)
            )

            if player_scores[0] != best_player_scores[0]:
                if player_scores[0] > best_player_scores[0]:
                    best_player = player
            elif player_scores[1] > best_player_scores[1]:
                best_player = player

        return best_player.name

    checker = staticmethod(checker)
