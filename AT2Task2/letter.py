class Letter:
    def __init__(self, owner, content):
        self.owner = owner
        self.content = content
        self.read = False

    def read_letter(self):
        if not self.read:
            print(f"The letter has been read")
            self.read = True
        else:
            print("The letter has already been read")

