class Letter:
    def __init__(self, owner, content, recipient, encryption=False):
        self.owner = owner
        self.content = content
        self.recipient = recipient
        self.encryption = encryption
        self.read = False

    def read_letter(self, level=0):
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
        decrypted_message = ""

        for char in encrypted_message:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - ascii_offset - level) % 25 + ascii_offset)
                decrypted_message += decrypted_char
            else:
                decrypted_message += char

        return decrypted_message
