#
# Method to filter through valid and invalid sentences
#
# Criteria that has to be met:
# String starts with a capital letter.
# String has an even number of quotation marks.
# String ends with one of the following sentence termination characters: ".", "?", "!"
# String has no period characters other than the last character.
# Numbers below 13 are spelled out (”one”, “two”, "three”, etc…).
#
def is_sentence_valid(sentence: str):
    # Using guard clauses filter the sentence

    # Check if the sentence has a full stop other than the last character
    if "." in sentence[:-1]:
        return False

    # Check if the number in the sentence is numeric or text
    if not (is_numeric(sentence)):
        return False

    # Check if the first letter is uppercase
    if not (sentence[0].isupper()):
        return False

    # Check if the last character is a symbol
    if not (sentence.endswith((".", "!", "?"))):
        return False

    # Check if the " count is even
    if (sentence.count('"') % 2) != 0:
        return False

    # If nothing has returned false the sentence is valid.

    return True


# Method that check if a string contains a number then ensure it is less than 13
def is_numeric(txt):
    txt = txt.replace(',', '')
    # Check to see if the string contains any digits
    if any(i.isdigit() for i in txt):
        # Loop through the text and add to list if there is a digit
        my_list = [int(s) for s in txt.split() if s.isdigit()]
        # Check all digits and ensure none are less than 13
        for i in my_list:
            if i < 13:
                return False
            else:
                return True
    else:
        return True


valid_sentences = [
    'The quick brown fox said "hello Mr lazy dog".',
    'The quick brown fox said hello Mr lazy dog.',
    'One lazy dog is too few, 13 is too many.',
    'One lazy dog is too few, thirteen is too many.',
    'How many "lazy dogs" are there?']

invalid_sentences = [
    'The quick brown fox said "hello Mr. lazy dog".',
    'the quick brown fox said "hello Mr lazy dog".',
    '"The quick brown fox said "hello Mr lazy dog."',
    'One lazy dog is too few, 12 is too many.',
    'Are there 11, 12, or 13 lazy dogs?',
    'There is no punctuation in this sentence']

# Loop through test sentences
for i in valid_sentences:
    print(i + " is " + str(is_sentence_valid(i)))

print("\n")

for i in invalid_sentences:
    print(i + " is " + str(is_sentence_valid(i)))
