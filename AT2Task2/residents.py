from letter import Letter


class Resident:
    def __init__(self, name):
        self.name = name
        self.waiting = False
        self.written_letters = []
        self.owned_letters = []

    def encrypt_letter(self, message, level):
        encrypted_message = ""

        for char in message:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted_char = chr((ord(char) - ascii_offset + level) % 25 + ascii_offset)
                encrypted_message += encrypted_char
            else:
                encrypted_message += char

        return encrypted_message

    def write_letter(self, content, recipient, encrypt=False, level=5):
        if not self.waiting:
            if encrypt:
                content = self.encrypt_letter(content, level)
                new_letter = Letter(self, content, recipient, encryption=True)
                self.waiting = True
                self.written_letters.append(new_letter)
            else:
                new_letter = Letter(self, content, recipient)
                self.waiting = True
                self.written_letters.append(new_letter)
            return new_letter
        else:
            print(f"{self.name} is still waiting for a reply")
            return None

    def open_letters(self):
        self.waiting = False


    def deposit_letters(self, postoffice):
        if self.written_letters:
            for letter in self.written_letters:
                postoffice.add_letter(letter)
            self.written_letters = []
            self.waiting = True

    def check_letterbox(self, letterbox):
        moved_letters = []
        if letterbox.has_letters():
            for letter in letterbox.letters:
                letter.read_letter()
                self.owned_letters.append(letter)
                moved_letters.append(letter)
                letterbox.empty_letterbox()
            if moved_letters:
                self.open_letters()
