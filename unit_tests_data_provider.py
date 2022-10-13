import pytest
import allure

from is_sentence_valid import is_sentence_valid

invalid_sentences = [
    'The quick brown fox said "hello Mr. lazy dog".',
    'the quick brown fox said "hello Mr lazy dog".',
    '"The quick brown fox said "hello Mr lazy dog."',
    'One lazy dog is too few, 12 is too many.',
    'Are there 11, 12, or 13 lazy dogs?',
    'There is no punctuation in this sentence']


# pytest unit_tests_data_provider.py --alluredir=./allure/my_allure_results to run
# allure serve ./allure/my_allure_results to generate a report

@allure.title("Ensure Invalid Sentences Fail")
@pytest.mark.parametrize('invalid_sentences_array', invalid_sentences)
def test_ensure_invalid_sentences_fail(invalid_sentences_array):
    """This ensures that invalid sentences fail"""

    for invalid_sentence in invalid_sentences_array:
        assert is_sentence_valid(invalid_sentence) == False


valid_sentences = [
    'The quick brown fox said "hello Mr lazy dog".',
    'The quick brown fox said hello Mr lazy dog.',
    'One lazy dog is too few, 13 is too many.',
    'One lazy dog is too few, thirteen is too many.',
    'How many "lazy dogs" are there?']


@allure.title("Ensure Valid Sentences Fail")
@pytest.mark.parametrize('valid_sentences_array', valid_sentences)
def test_ensure_valid_sentences_pass(valid_sentences_array):
    """This ensures that invalid sentences fail"""

    for valid_sentence in valid_sentences_array:
        assert is_sentence_valid(valid_sentence) == False
