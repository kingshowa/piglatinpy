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
        self.assertEqual("", result)