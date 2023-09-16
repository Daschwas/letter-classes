class Postie:
    """
    This class represents the postman that collects the letters from the post office for delivery.
    """

    def __init__(self, name, workplace):
        """
        Parameters:
             Name - The name of the postman.
             Workplace - The name of the specific post office the postman works for.
             Letters - A list that shows the current letters the postman is holding for distribution.
             On_Shift - This is a state that shows whether the postman is currently working or not. It is not
             currently used for any real function, but could be used in the future if one needs to know that
             information.
        """
        self.name = name
        self.workplace = workplace
        self.letters = []
        self.on_shift = False

    def deposit_letters(self, letterbox):
        """
        This method is a replacement for the resident's deposit_letters function that was previously used to interact
        with letterboxes and represents the interaction between the postman and the letterbox.

        For each letter in the postman's list, the method checks whether the recipient specified matches the current
        letterbox being interacted with. If so, it calls the letterbox's add letter function and adds the letter to the
        letterbox's list. It then also adds an instance of that letter to the moved_letters list in this function (which
        is cleared each time the function is called). After the list has finished being iterated through, all letters in
        the moved_letters list are removed from the regular letters list - this is done at the end so that the list is
        not being modified at the same time it is being iterated through.

        After the function has been called, it will check whether the postman has any more letters for delivery. If
        they do not, the postman's shift ends, and they are now off the clock.
        """
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
        """
        This function allows the postman to read a letter - which they shouldn't do, but this allows them!
        It will then return the content that is read, which is useful for determining if the letter is successfully
        decrypted or not.
        """
        read_content = letter.read_letter()
        return read_content

    def check_postoffice(self, postoffice):
        """
        This function is called to represent the postie starting their workday. They check the has_letters method
        in post office to determine if there are any new letters for delivery - if there are, they iterate over each
        letter by adding those letters to their own letter list, and calling the post office's remove_letter method
        to clear their letter list (effectively, moving the letters from the post office to the postman). The postman's
        on shift state is then turned on - representing they are now on the job.

        If there are no letters for delivery, the user is informed of this.
        """
        if postoffice.has_letters():
            for letter in postoffice.letters:
                self.letters.append(letter)
                postoffice.remove_letters()
            self.on_shift = True
        else:
            print("There are no letters to deliver today")
