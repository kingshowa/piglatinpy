from unittest import TestCase
from src.translator import PigLatinTranslator

class TestPigLatinTranslator(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_get_phrase(self):
        # Arrange
        phrase = "hello world"
        translator = PigLatinTranslator(phrase)
        # Act
        result = translator.get_phrase()
        # Assert
        self.assertEqual(phrase, result)

    def test_translate_empty_phrase(self):
        # Arrange
        phrase = ""
        translator = PigLatinTranslator(phrase)
        # Act
        result = translator.translate()
        # Assert
        self.assertEqual("nil", result)

    def test_translate_phrase_starts_with_vowel_end_with_y(self):
        # Arrange
        phrase = "any"
        translator = PigLatinTranslator(phrase)
        # Act
        result = translator.translate()
        # Assert
        self.assertEqual("anynay", result)
        
    def test_translate_phrase_starts_with_vowel_ending_with_vowel(self):    
        # Arrange
        phrase = "apple"
        translator = PigLatinTranslator(phrase)
        # Act
        result = translator.translate()
        # Assert
        self.assertEqual("appleyay", result)        