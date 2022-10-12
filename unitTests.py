import unittest
from isSentenceValid import isSentenceValid


class TestStringMethods(unittest.TestCase):

    def test_ensureInvalidSentencesFail(self):

        invalidSentences = [
            'The quick brown fox said "hello Mr. lazy dog".',
            'the quick brown fox said "hello Mr lazy dog".',
            '"The quick brown fox said "hello Mr lazy dog."',
            'One lazy dog is too few, 12 is too many.',
            'Are there 11, 12, or 13 lazy dogs?',
            'There is no punctuation in this sentence']

        for invalidSentence in invalidSentences:
            self.assertFalse(isSentenceValid(invalidSentence))

    def test_ensureValidSentencesPass(self):

        validSentences = [
            'The quick brown fox said "hello Mr lazy dog".',
            'The quick brown fox said hello Mr lazy dog.',
            'One lazy dog is too few, 13 is too many.',
            'One lazy dog is too few, thirteen is too many.',
            'How many "lazy dogs" are there?']

        for validSentence in validSentences:
            self.assertTrue(isSentenceValid(validSentence))


if __name__ == '__main__':
    unittest.main()
