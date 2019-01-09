import random
import string
from Game import Card


class Cards:

    cards = []
    matched = set()
    active = 0

    def __init__(self, count):

        # Generate values for cards
        alphabet = list(string.ascii_uppercase)
        items = alphabet[0:count]
        items += items
        random.shuffle(items)
        cards = {}
        position = 1

        for item in items:
            cards[position] = Card.Card(item)
            position += 1

        self.cards = cards

    def get_cards(self):
        return self.cards

    # TODO: Break function into two functions: play() and check()
    # TODO: Replace self.active with self.card_1 and self.card_2.
    #  Then use check() to find out if cards match or if game is over.
    # TODO: Add validation to prevent faceup cards from being chosen.
    def play(self, position):
        is_won = False;
        self.cards[position].show()
        self.print()
        if not self.active:
            self.active = position
        else:
            if self.cards[self.active].get_value() == self.cards[position].get_value():
                # TODO: return keys instead of printing messages
                print("It's a match!")
                self.matched.add(self.active)
                self.matched.add(position)
                if len(self.matched) == len(self.cards):
                    is_won = True
            else:
                print("It's not a match.")
                self.cards[position].hide()
                self.cards[self.active].hide()
            self.active = 0
        return is_won

    def print(self):
        output = ""
        for position, card in self.cards.items():
            if card.is_faceup():
                output += "{} ".format(card.value)
            else:
                output += "{} ".format(position)
        print(output)

    def print_values(self):
        output = ""
        for position, card in self.cards.items():
            output += "{} ".format(card.value)
        print(output)

