from src.error import PigLatinError


class PigLatinTranslator:
    VOWELS = 'aeiou'
    def __init__(self, phrase: str):
        """
        Creates a pig latin translator given a phrase.
        :param phrase: the phrase.
        :raise PigLatinError: for any error situation.
        """
        self.phrase = phrase

    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        
        return self.phrase

    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """
        if self.phrase == "":
            return "nil"

        first_letter = self.phrase[0].lower()
        last_letter = self.phrase[-1].lower()
        if first_letter in self.VOWELS:
            if last_letter in self.VOWELS:
                return self.phrase + "yay"
            elif last_letter == 'y':
                return self.phrase + "nay"  # --- IGNORE ---
            else:
                return self.phrase + "ay"
        return ""
