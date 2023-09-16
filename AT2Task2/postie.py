class Postie:
    def __init__(self, name, workplace):
        self.name = name
        self.workplace = workplace
        self.letters = []
        self.on_shift = False

    def deposit_letters(self, letterbox):
        for letter in self.letters:
            if letter.recipient == letterbox:
                letterbox.add_letter(letter)
                self.letters.remove(letter)
                if not self.letters:
                    self.on_shift = False

    def read_post(self, letter):
        letter.read_letter()

    def check_postoffice(self, postoffice):
        if postoffice.has_letters():
            for letter in postoffice.letters:
                self.letters.append(letter)
                postoffice.remove_letters()
            self.on_shift = True
        else:
            print("There are no letters to deliver today")
