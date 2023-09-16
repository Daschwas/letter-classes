class Letterbox:
    """
    This represents the letterbox owned by a resident.
    """
    def __init__(self, owner):
        """
               Owner is the resident that owns the letterbox.
               Letters are a list that indicate what letters are currently within the letterbox.
        """
        self.owner = owner
        self.letters = []


    def add_letter(self, letter):
        """
        This method is called by other classes to add a letter to the letterbox (via appending it to the existing list).
        """
        self.letters.append(letter)

    def empty_letterbox(self):
        """
        This method is called by the resident class when they check their mailbox.
        It represents the letterbox being emptied of all letters through emptying the "letters" list.
        """
        self.letters = []

    def has_letters(self):
        """
        This replaces the need for a has letters state. It returns a true or false value by checking whether there
        are any items in the letters list. It can be used by other classes to check whether the letterbox currently
        contains any objects.
        """
        return bool(self.letters)
