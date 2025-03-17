import ui as UI


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.hand = []

    def clear_hand(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def hand_value(self):
        value = 0
        aces = 0

        for card in self.hand:
            if card[0] == 1:
                aces += 1
            value += min(card[0], 10)

        while aces > 0 and value + 10 <= 21:
            value += 10
            aces -= 1

        return value

    def show_hand(self):
        return UI.show_hand(self)

    def can_buy(self):
        return self.hand_value() < 21

    def lost(self):
        return self.hand_value() > 21

    def __str__(self):
        return f"{self.name} - Wins: {self.wins}, Hand: {self.hand}, Value: {self.hand_value()}"