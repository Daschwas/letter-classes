class PostOffice:
    """
    This class represents the post office where residents send their letters for distribution.
    The relevant postie then collects and delivers the letters.
    It acts very similar to the letterbox class - but is interacted with by different classes.
    """
    def __init__(self, name):
        """
        Parameters:
             Name - This is the name of the post office specified.
             Letters - This list, much like the letters list in letterbox, shows what letters are currently contained
             within the post office.
        """
        self.name = name
        self.letters = []

    def add_letter(self, letter):
        """
        This method is called by other classes to add a letter to the post office (via appending it to the existing
        list).
        """
        self.letters.append(letter)

    def remove_letters(self):
        """
               This method is called by the postie class when they check their mailbox.
               It represents the post office being emptied of all letters through emptying the "letters" list.
        """
        self.letters = []

    def has_letters(self):
        """
               This replaces the need for a "has letters" state. It returns a true or false value by checking whether
               there are any items in the letters list. It can be used by other classes to check whether the letterbox
               currently  contains any objects.
        """
        return bool(self.letters)
