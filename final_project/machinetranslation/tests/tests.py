import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):

    def test_null_input_french_to_english(self):
        self.assertIsNone(french_to_english(None), None)
    
    def test_null_input_english_to_french(self):
        self.assertIsNone(english_to_french(None), None)

    def test_hello_to_bonjour(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_bonjour_to_hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__=='__main__':
    unittest.main()

