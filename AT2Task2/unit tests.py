import unittest
from residents import Resident
from letterbox import Letterbox
from letter import Letter

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.alice = Resident("Alice")
        self.bob = Resident("Bob")
        self.alice_letterbox = Letterbox(self.alice)
        self.bob_letterbox = Letterbox(self.bob)

    def test_alice_posts_letter_to_bob(self):
        letter_content = "Hi Bob, how are things?"
        letter = self.alice.write_letter(letter_content)

        self.alice.deposit_letters(self.bob_letterbox)

        self.assertIn(letter, self.bob_letterbox.letters)
        self.assertTrue(self.alice.waiting)

    def test_bob_reads_letter(self):
        letter_content = "Hi Bob, how are things?"
        letter = self.alice.write_letter(letter_content)
        self.alice.deposit_letters(self.bob_letterbox)
        self.bob.check_letterbox(self.bob_letterbox)

        self.assertTrue(letter.read)

    def test_alice_checks_empty_letterbox(self):
        self.alice.waiting = True
        self.alice.check_letterbox(self.alice_letterbox)
        self.assertTrue(self.alice.waiting)

    def test_alice_checks_letterbox_with_unread_letter(self):
        letter_content = "Hi Alice, things are well."
        letter = self.bob.write_letter(letter_content)
        self.bob.deposit_letters(self.alice_letterbox)

        self.alice.check_letterbox(self.alice_letterbox)
        self.assertFalse(self.alice.waiting)

if __name__ == '__main__':
    unittest.main()
