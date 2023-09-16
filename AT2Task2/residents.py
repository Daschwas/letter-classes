from letter import Letter


class Resident:
    """
    This represents a person living in the town that mails letters to other residents.
    """
    def __init__(self, name):
        """
        Parameters:
             Name - This is the resident's name.
             Waiting state - This indicates whether the resident is waiting for a letter or not. This is important as
             the brief specifies they cannot write a new letter if they are still awaiting a reply.
             Written letters - This is a list that holds any new letters created after the resident uses the write
             letter method.
             Owned letters - This is a separate list that holds any letters intended to be read by this resident (ie;
             letters addressed to them). This is to make it easier to write functions that operate differently on each
             type of letter.
        """
        self.name = name
        self.waiting = False
        self.written_letters = []
        self.owned_letters = []

    def encrypt_letter(self, message, level):
        """
        This (optional) method can be called when the resident is writing a letter to encrypt it, making it more
        difficult for unintended recipients to read the contents of the message.

        It does this using a simple substitution cipher iterated over each character in the letter's content.
        Each character is converted to its ASCII code (e.g. "A" is "65"), offsets the letter by a level specified
        by the user, and then coverts into back into alphanumeric characters. The message "Test" with an offset level
        three places would produce the phrase "Whvw". The encrypted message is then returned.

        This only works with alphanumeric characters, however. Other character types will appear in the message
        as normal. For example, "Te$t" with an offset level of 3 places would produce "Wh$w".
        """
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
        """
        This method represents the writing of a letter by the resident. They need to specify the content that will
        comprise the letter and who (ie; what resident) the letter is addressed to. If they (optionally) choose to
        encrypt the letter, they can also specify the level they want the characters to be shifted by - but by default,
        encryption is turned off otherwise (at the method level).

        If the resident tries to write a letter while they are still waiting for a reply, they are prevented from
        doing so and a print message reminds the user of this.
        """
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
        """
        This function is called by other methods and simply indicates that the resident has opened a new letter and
        thus is no longer waiting for a reply (changing their state).
        """
        self.waiting = False

    def deposit_letters(self, postoffice):
        """
        This replaces the previous deposit letters method by changing where they can deposit the letter - now, they
        deposit it at the post office, rather than directly at the letterbox, and it calls the post office's add
        letter method. Although the resident currently can only write one letter at a time regardless, this forces
        them to deposit all letters they have written, then wipes the written letters list blank and sets their state
        to be waiting for new letters.
        """
        if self.written_letters:
            for letter in self.written_letters:
                postoffice.add_letter(letter)
            self.written_letters = []
            self.waiting = True

    def check_letterbox(self, letterbox, decryption_level=0):
        """
        This allows the resident to check a (not specifically theirs) letterbox for new letters. It does this by
        looking at the bool value of has_letters, which shows whether the letterbox contains any letters or not.

        Moved letters (which is reset each time this function is called) is used to keep track of the letters that are
        being transferred from the letterbox to the resident's owned letters, as the owned letters list may have letters
        that they previously retrieved already present.

        If the letterbox does have letters, each letter is read (via letter's read letter method), with the user able to
        optionally specify a level of decryption if they believe the letter is encrypted. The letters are then appended
        both to the moved letters list and the owned letters list. The empty letterbox method from the letterbox
        class is called to then clear the letterbox. If the method detects any letters in the transitory moved letters
        list, it will then call the resident's open_letters method to mark them as no longer waiting for a letter.
        """
        moved_letters = []
        if letterbox.has_letters():
            for letter in letterbox.letters:
                letter.read_letter(level=decryption_level)
                self.owned_letters.append(letter)
                moved_letters.append(letter)
                letterbox.empty_letterbox()
            if moved_letters:
                self.open_letters()
