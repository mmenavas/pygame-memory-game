class Card:

    faceup = ""
    facedown = ""
    is_faceup = False

    def __init__(self, faceup, facedown):
        self.faceup = faceup
        self.facedown = facedown

    def show(self):
        self.is_faceup = True

    def hide(self):
        self.fais_faceup = False

    def is_faceup(self):
        return self.is_faceup

    def set_faceup(self, value):
        self.faceup = value

    def get_faceup(self):
        return self.faceup

    def set_facedown(self, value):
        self.facedown = value

    def get_facedown(self):
        return self.facedown

