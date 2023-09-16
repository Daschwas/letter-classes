class Postie:
    def __init__(self, name, workplace):
        self.name = name
        self.workplace = workplace
        self.letters = []
        self.on_shift = False

    def deposit_letters(self, letterbox):
        moved_letters = []

        for letter in self.letters:
            if letter.recipient == letterbox.owner:
                letterbox.add_letter(letter)
                moved_letters.append(letter)
        for letter in moved_letters:
                self.letters.remove(letter)

        if not self.letters:
                self.on_shift = False

    def read_post(self, letter):
        read_content = letter.read_letter()
        return read_content



    def check_postoffice(self, postoffice):
        if postoffice.has_letters():
            for letter in postoffice.letters:
                self.letters.append(letter)
                postoffice.remove_letters()
            self.on_shift = True
        else:
            print("There are no letters to deliver today")
