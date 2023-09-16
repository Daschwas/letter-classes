class Letter:

    """
    This class represents the letter written by the resident, delivered by the postie and read by another resident.
    """
    def __init__(self, owner, content, recipient, encryption=False):
        """
        Parameters:
            Owner - the resident that was the author of the letter.
            Content - the body of the message itself (ie; what the resident wrote).
            Recipient - the intended reader of the letter (ie; who it is addressed to).
            Encryption - whether the letter has been encrypted or not.
            Read - a state flag that indicates whether anyone but the owner has read the letter.
        """
        self.owner = owner
        self.content = content
        self.recipient = recipient
        self.encryption = encryption
        self.read = False

    def read_letter(self, level=0):
        """
        This function is used by other classes like the resident and postie classes to read the content of a letter.
        If the letter has encryption, the user is optionally able to specify a level which is then used when the
        decrypt_letter method is called to attempt to decrypt it.

        Either way, regardless of whether the decryption was successful or not, the letter is then marked as "read"
        through the read state.
        """
        if not self.read:
            self.read = True
            if self.encryption:
                decrypted_content = self.decrypt_letter(self.content, level)
                print(decrypted_content)
                return decrypted_content
            else:
                print(self.content)
                return self.content
        else:
            print("Note: The letter has already been read")
            if self.encryption:
                decrypted_content = self.decrypt_letter(self.content, level)
                print(decrypted_content)
                return decrypted_content

            else:
                print(self.content)
                return self.content

    def decrypt_letter(self, encrypted_message, level=0):
        """"
        This decrypts the letter if it has been encrypted by shifting the characters back an amount specified by the
        level parameter. If no level is specified, it just leaves the message as decrypted (as the default level is 0).
        The end result string is then returned as a value.

        """
        decrypted_message = ""

        for char in encrypted_message:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - ascii_offset - level) % 25 + ascii_offset)
                decrypted_message += decrypted_char
            else:
                decrypted_message += char

        return decrypted_message
