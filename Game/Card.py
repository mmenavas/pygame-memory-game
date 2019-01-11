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
        self.is_faceup = False

    def toggle(self):
        if self.is_faceup:
            self.hide()
        else:
            self.show()

    def get_value(self):
        return self.faceup if self.is_faceup else self.facedown

    def is_on(self):
        return self.is_faceup

    def set_faceup(self, value):
        self.faceup = value

    def get_faceup(self):
        return self.faceup

    def set_facedown(self, value):
        self.facedown = value

    def get_facedown(self):
        return self.facedown

