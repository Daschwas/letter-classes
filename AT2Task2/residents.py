from letter import Letter


class Resident:
    def __init__(self, name):
        self.name = name
        self.waiting = False
        self.letters = []

    def write_letter(self, content):
        if not self.waiting:
            new_letter = Letter(self, content)
            self.waiting = True
            self.letters.append(new_letter)
            return new_letter
        else:
            print(f"{self.name} is still waiting for a reply")
            return None

    def open_letters(self):
            self.waiting = False

    def deposit_letters(self, letterbox):
        for letter in self.letters:
            letterbox.add_letter(letter)
        self.letters = []
        self.waiting = True

    def check_letterbox(self, letterbox):
        moved_letters = []
        if letterbox.has_letters():
            for letter in letterbox.letters:
                letter.read_letter()
                self.letters.append(letter)
                moved_letters.append(letter)
                letterbox.empty_letterbox()
            if moved_letters:
                self.open_letters()

