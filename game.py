import random
from player import Player
import ui as UI


full_deck = [(1, chr(9829)), (1, chr(9830)), (1, chr(9824)), (1, chr(9827)),
             (2, chr(9829)), (2, chr(9830)), (2, chr(9824)), (2, chr(9827)),
             (3, chr(9829)), (3, chr(9830)), (3, chr(9824)), (3, chr(9827)),
             (4, chr(9829)), (4, chr(9830)), (4, chr(9824)), (4, chr(9827)),
             (5, chr(9829)), (5, chr(9830)), (5, chr(9824)), (5, chr(9827)),
             (6, chr(9829)), (6, chr(9830)), (6, chr(9824)), (6, chr(9827)),
             (7, chr(9829)), (7, chr(9830)), (7, chr(9824)), (7, chr(9827)),
             (8, chr(9829)), (8, chr(9830)), (8, chr(9824)), (8, chr(9827)),
             (9, chr(9829)), (9, chr(9830)), (9, chr(9824)), (9, chr(9827)),
             (10, chr(9829)), (10, chr(9830)), (10, chr(9824)), (10, chr(9827)),
             (10, chr(9829)), (10, chr(9830)), (10, chr(9824)), (10, chr(9827)),
             (10, chr(9829)), (10, chr(9830)), (10, chr(9824)), (10, chr(9827)),
             (10, chr(9829)), (10, chr(9830)), (10, chr(9824)), (10, chr(9827))]


class Game:
    def __init__(self, name):
        self.players = [Player(name), Player('Dealer')]

    def __repr__(self):
        return UI.scoreboard(self.players)

    def start_round(self):
        self.deck = full_deck.copy()
        random.shuffle(self.deck)

        for player in self.players:
            player.clear_hand()
            self.give_card(self.players.index(player))  # Give an initial card

    def give_card(self, player_id):
        if self.deck:
            self.players[player_id].add_card(self.deck.pop())
        return self.players[player_id].can_buy()

    def dealer_needs_buy(self):
        return (self.players[0].hand_value() < 21 and
                not self.players[0].lost() and
                not self.players[1].lost() and
                self.players[0].hand_value() <= self.players[1].hand_value())

    def dealer_won(self):
        player, dealer = self.players
        if player.hand_value() == dealer.hand_value():
            return None  # Tie

        if player.lost() or (not dealer.lost() and player.hand_value() < dealer.hand_value()):
            dealer.wins += 1
            return True

        player.wins += 1
        return False
