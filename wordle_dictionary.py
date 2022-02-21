
DEFAULT_WORD_LENGTH = 5
SOURCE_FILE = "Collins Scrabble Words (2019).txt"

def build_dictionary(word_length=DEFAULT_WORD_LENGTH, source_file=SOURCE_FILE):

    word_dictionary = []

    with open(source_file, 'r') as f:
        for word in f:
            word = word.strip()
            if len(word) == word_length:
                word_dictionary += [word]

    return word_dictionary

