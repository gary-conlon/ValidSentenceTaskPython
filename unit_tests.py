import pytest

from is_sentence_valid import is_sentence_valid


# pytest unitTests.py to run

def test_ensure_invalid_sentences_fail():
    """This ensures that invalid sentences fail"""

    invalid_sentences = [
        'The quick brown fox said "hello Mr. lazy dog".',
        'the quick brown fox said "hello Mr lazy dog".',
        '"The quick brown fox said "hello Mr lazy dog."',
        'One lazy dog is too few, 12 is too many.',
        'Are there 11, 12, or 13 lazy dogs?',
        'There is no punctuation in this sentence',
        'Are there 11,12 lazy dogs?',
        '9,8.','A 9 ?','"13?', 'a13?', '!A13?git ', 'A 13,12,11,13?', '""']

    for invalid_sentence in invalid_sentences:
        assert is_sentence_valid(invalid_sentence) == False


def test_ensure_valid_sentences_pass():
    """This ensures that valid sentences pass"""

    valid_sentences = [
        'The quick brown fox said "hello Mr lazy dog".',
        'The quick brown fox said hello Mr lazy dog.',
        'One lazy dog is too few, 13 is too many.',
        'One lazy dog is too few, thirteen is too many.',
        'How many "lazy dogs" are there?']

    for valid_sentence in valid_sentences:
        assert is_sentence_valid(valid_sentence) == True