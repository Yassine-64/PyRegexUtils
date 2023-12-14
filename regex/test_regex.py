import unittest
from regex_functions import recherche_mot, verifie_chaine, remplace_espace, verifie_numero, verifie_email

class TestRegexFunctions(unittest.TestCase):

    def test_recherche_mot(self):
        self.assertTrue(recherche_mot("apple", "I love apples"))
        self.assertFalse(recherche_mot("banana", "I love apples"))

    def test_verifie_chaine(self):
        self.assertTrue(verifie_chaine("123"))
        self.assertFalse(verifie_chaine("abc"))

    def test_remplace_espace(self):
        self.assertEqual(remplace_espace("hello world"), "hello-world")
        self.assertEqual(remplace_espace("   spaces   "), "---spaces---")

    def test_verifie_numero(self):
        self.assertTrue(verifie_numero("12-345-6789"))
        self.assertFalse(verifie_numero("123-4567-890"))

    def test_verifie_email(self):
        self.assertTrue(verifie_email("test@example.com"))
        self.assertFalse(verifie_email("invalid.email@"))

    def test_custom_examples(self):
        # Add your custom examples and assertions here
        self.assertTrue(recherche_mot("world", "Hello, world!"))
        self.assertFalse(verifie_chaine("abc"))
        self.assertEqual(remplace_espace("python is fun"), "python-is-fun")
        self.assertTrue(verifie_numero("99-888-7777"))
        self.assertTrue(verifie_email("user@example.org"))

if __name__ == '__main__':
    unittest.main()
