class Letter:
    def __init__(self, owner, content, recipient, encryption=False):
        self.owner = owner
        self.content = content
        self.recipient = recipient
        self.encryption = encryption
        self.read = False

    def read_letter(self, level=5):
        if not self.read:
            if self.encryption:
                decrypted_content = self.decrypt_letter(self.content, level)
                print(decrypted_content)
            else:
                print(self.content)
            self.read = True
        else:
            print("Note: The letter has already been read")
            print(self.content)

    def decrypt_letter(self, encrypted_message, level):
        decrypted_message = ""

        for char in encrypted_message:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_char = chr((ord(char) - ascii_offset + level) % 25 + ascii_offset)
                decrypted_message += decrypted_char
            else:
                decrypted_message += char

        return decrypted_message
