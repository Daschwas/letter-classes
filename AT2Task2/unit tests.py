import unittest
from residents import Resident
from letterbox import Letterbox
from postie import Postie
from postoffice import PostOffice


class UnitTests(unittest.TestCase):
    def setUp(self):
        """
        This sets up instances of all the classes that are used throughout the unit tests.
        """
        self.alice = Resident("Alice")
        self.bob = Resident("Bob")
        self.daniel = Resident("Daniel")
        self.alice_letterbox = Letterbox(self.alice)
        self.bob_letterbox = Letterbox(self.bob)
        self.perth = PostOffice("Perth Post Office")
        self.charli = Postie("Charli", self.perth)

    def test_alice_posts_letter_to_bob(self):
        """
        This tests whether the postal program works from start to finish - beginning with a resident writing a letter
        and ending with the letter being deposited by the postie in the letter box.
        """
        letter_content = "Hi Bob, how are things?"
        letter = self.alice.write_letter(letter_content, self.bob)

        self.alice.deposit_letters(self.perth)
        self.charli.check_postoffice(self.perth)
        self.charli.deposit_letters(self.bob_letterbox)

        self.assertIn(letter, self.bob_letterbox.letters)
        self.assertTrue(self.alice.waiting)

    def test_alice_posts_encrypted_letter_to_bob(self):
        """
        This unit test tests the encryption function. It ensures that a user does not get the correct message when
        they decrypt unsuccessfully and that the correct message is relayed when the appropriate level amount is
        specified. It also makes sure that even if decryption fails, the letter is still marked as read.
        """
        letter_content = "Test"
        encrypted_letter = self.alice.write_letter(letter_content, self.bob, encrypt=True, level=3)

        self.assertTrue(encrypted_letter.encryption)

        self.alice.deposit_letters(self.perth)
        self.charli.check_postoffice(self.perth)
        decrypted_message = self.charli.read_post(encrypted_letter)

        self.assertTrue(encrypted_letter.read)
        self.assertNotEqual(decrypted_message, "Test")

        self.charli.deposit_letters(self.bob_letterbox)
        self.assertIn(encrypted_letter, self.bob_letterbox.letters)
        self.assertTrue(self.alice.waiting)

        self.bob.check_letterbox(self.bob_letterbox, decryption_level=3)
        decrypted_content = encrypted_letter.read_letter(level=3)
        self.assertEqual(decrypted_content, "Test")

    def test_bob_reads_letter(self):
        """
        This unit test ensures that the check letterbox method correctly works and the letter is marked read.
        """
        letter_content = "Hi Bob, how are things?"
        letter = self.alice.write_letter(letter_content, self.bob)

        self.alice.deposit_letters(self.perth)
        self.charli.check_postoffice(self.perth)
        self.charli.deposit_letters(self.bob_letterbox)

        self.bob.check_letterbox(self.bob_letterbox)

        self.assertTrue(letter.read)

    def test_alice_checks_empty_letterbox(self):
        """
        This unit test ensures that if a resident checks an empty letterbox, they are still marked as waiting for a
        letter.
        """
        self.alice.waiting = True
        self.alice.check_letterbox(self.alice_letterbox)
        self.assertTrue(self.alice.waiting)

    def test_alice_checks_letterbox_with_unread_letter(self):
        """
        This unit test ensures that when the resident reads a letter, they are correctly marked as no longer
        waiting for a letter.
        """
        letter_content = "Hi Alice, things are well."
        self.bob.write_letter(letter_content, self.alice)

        self.bob.deposit_letters(self.perth)
        self.charli.check_postoffice(self.perth)
        self.charli.deposit_letters(self.alice_letterbox)

        self.alice.check_letterbox(self.alice_letterbox)
        self.assertFalse(self.alice.waiting)

    def test_alice_checks_letterbox_with_read_by_postie(self):
        """
        This unit test makes sure that if the postman reads the letter en-route, the letter is successfully
        marked as already read when the intended resident opens it.
        """
        letter_content = "Hi Alice, things are well."
        letter = self.bob.write_letter(letter_content, self.alice)

        self.bob.deposit_letters(self.perth)
        self.charli.check_postoffice(self.perth)
        self.charli.read_post(letter)

        self.assertTrue(letter.read)

        self.charli.deposit_letters(self.alice_letterbox)

        self.alice.check_letterbox(self.alice_letterbox)
        self.assertFalse(self.alice.waiting)

    def test_alice_opens_multiple_letters(self):
        """
        This tests whether a resident successfully retrieves and reads each letter in instances where there are
        multiple letters in the letterbox.
        """
        letter_content1 = "Hi Alice"
        letter1 = self.daniel.write_letter(letter_content1, self.alice)
        self.daniel.deposit_letters(self.alice_letterbox)

        letter_content2 = "Hey Alice"
        letter2 = self.bob.write_letter(letter_content2, self.alice)
        self.bob.deposit_letters(self.alice_letterbox)

        self.alice.check_letterbox(self.alice_letterbox)

        self.assertTrue(letter1.read)
        self.assertTrue(letter2.read)


if __name__ == '__main__':
    unittest.main()
