class Letterbox:
    def __init__(self, owner):
        self.owner = owner
        self.letters = []

    def add_letter(self, letter):
        self.letters.append(letter)

    def empty_letterbox(self):
        self.letters = []

    def has_letters(self):
        return bool(self.letters)
