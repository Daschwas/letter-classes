class PostOffice:
    def __init__(self, name):
        self.name = name
        self.letters = []

    def add_letter(self, letter):
        self.letters.append(letter)

    def remove_letters(self):
        self.letters = []

    def has_letters(self):
        return bool(self.letters)
