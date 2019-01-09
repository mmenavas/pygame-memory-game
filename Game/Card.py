import random
import string


class Card:

    value = ""
    faceup = False

    def __init__(self, value):
        self.value = value

    def show(self):
        self.faceup = True

    def hide(self):
        self.faceup = False

    def is_faceup(self):
        return self.faceup

    def get_value(self):
        return self.value

    def update_value(self, value):
        self.value = value

