import unittest
from residents import Resident
from letterbox import Letterbox
from letter import Letter
from postie import Postie
from postoffice import PostOffice

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.alice = Resident("Alice")
        self.bob = Resident("Bob")
        self.alice_letterbox = Letterbox(self.alice)
        self.bob_letterbox = Letterbox(self.bob)
        self.perth = PostOffice("Perth Post Office")
        self.charli = Postie("Charli", self.perth)

    def test_alice_posts_letter_to_bob(self):
        letter_content = "Hi Bob, how are things?"
        letter = self.alice.write_letter(letter_content, self.bob)

        self.alice.deposit_letters(self.perth)
        self.charli.check_postoffice(self.perth)
        self.charli.deposit_letters(self.bob_letterbox)

        self.assertIn(letter, self.bob_letterbox.letters)
        self.assertTrue(self.alice.waiting)

    def test_alice_posts_encrypted_letter_to_bob(self):
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

        self.bob.check_letterbox(self.bob_letterbox,decryption_level=3)
        decrypted_content = encrypted_letter.read_letter(level=3)
        self.assertEqual(decrypted_content, "Test")

    def test_bob_reads_letter(self):
        letter_content = "Hi Bob, how are things?"
        letter = self.alice.write_letter(letter_content, self.bob)

        self.alice.deposit_letters(self.perth)
        self.charli.check_postoffice(self.perth)
        self.charli.deposit_letters(self.bob_letterbox)

        self.bob.check_letterbox(self.bob_letterbox)

        self.assertTrue(letter.read)

    def test_alice_checks_empty_letterbox(self):
        self.alice.waiting = True
        self.alice.check_letterbox(self.alice_letterbox)
        self.assertTrue(self.alice.waiting)

    def test_alice_checks_letterbox_with_unread_letter(self):
        letter_content = "Hi Alice, things are well."
        letter = self.bob.write_letter(letter_content, self.alice)

        self.bob.deposit_letters(self.perth)
        self.charli.check_postoffice(self.perth)
        self.charli.deposit_letters(self.alice_letterbox)

        self.alice.check_letterbox(self.alice_letterbox)
        self.assertFalse(self.alice.waiting)

    def test_alice_checks_letterbox_with_read_by_postie(self):
        letter_content = "Hi Alice, things are well."
        letter = self.bob.write_letter(letter_content, self.alice)

        self.bob.deposit_letters(self.perth)
        self.charli.check_postoffice(self.perth)
        self.charli.read_post(letter)

        self.assertTrue(letter.read)

        self.charli.deposit_letters(self.alice_letterbox)

        self.alice.check_letterbox(self.alice_letterbox)
        self.assertFalse(self.alice.waiting)

if __name__ == '__main__':
    unittest.main()
