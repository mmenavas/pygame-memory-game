import random
from random import shuffle
import string
from Game import Card


class Cards:

    cards = []
    matched = set()
    active = 0
    unmatched = 0, 0

    def __init__(self, count, facedown = "?"):

        # Generate values for cards
        alphabet = list(string.ascii_uppercase)
        shuffle(alphabet)
        items = alphabet[0:count]
        items += items
        random.shuffle(items)
        cards = {}
        position = 1

        for item in items:
            cards[position] = Card.Card(item, facedown)
            position += 1

        self.cards = cards

    def get_cards(self):
        return self.cards

    def play(self, position):
        status_code_list = {
            0: "invalid_card",
            1: "pick_next_card",
            2: "not_a_match",
            3: "match",
            4: "winner",
        }

        # Invalid card.
        if self.cards[position].is_on():
            print(status_code_list[0])
            return status_code_list[0];

        # Picking first card
        if not self.active:
            self.active = position
            self.cards[position].show()
            print(status_code_list[1])
            return status_code_list[1];

        # Picking second card.
        self.cards[position].show()
        if self.cards[self.active].get_value() == self.cards[position].get_value():
            # It's a match.
            self.matched.add(self.active)
            self.matched.add(position)
            if len(self.matched) == len(self.cards):
                # Game over.
                print(status_code_list[4])
                return status_code_list[4];
            self.active = 0
            print(status_code_list[3])
            return status_code_list[3];
        else:
            # Not a match. Use self.hide_cards() to flip cards back.
            self.unmatched = self.active, position
            self.active = 0
            print(status_code_list[2])
            return status_code_list[2];

    def hide_cards(self):
        for i in self.unmatched:
            if i > 0:
                self.cards[i].hide()

    def print(self):
        output = ""
        for position, card in self.cards.items():
            if card.is_on():
                output += "{} ".format(card.get_value())
            else:
                output += "{} ".format(position)
        print(output)

    def print_values(self):
        output = ""
        for position, card in self.cards.items():
            output += "{} ".format(card.get_faceup())
        print(output)

