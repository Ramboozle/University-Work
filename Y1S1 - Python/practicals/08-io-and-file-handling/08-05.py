 # The Unix spell command is a simple spell-checker.It prints out all the words in a
 # text file that are not found in a dictionary. Write and test an implementation of this,
 # that takes a file name as a command-line argument.
 # Note: You may want to simplify the program at first by testing with a text file that
 # does not contain any punctuation. A complete version should obviously be able to
 # handle normal files, with punctuation.
 # Another Note: You will need a list of valid words. Linux users will already have one
 # (probably in /usr/share/dict/words). It is more complicated,as usual, for
 # Windows users. Happily, there are several available on GitHub.

import sys
dictionary_file = 'words.txt'
file_to_check = sys.argv[1]

def load_words(file_path):
    with open(file_path) as f:
        return set(word.strip().lower() for word in f)

def check_spelling(file_path, dictionary):
    with open(file_path) as f:
        for line in f:
            for word in line.split():
                cleaned_word = ''.join(filter(str.isalpha, word)).lower()
                if cleaned_word and cleaned_word not in dictionary:
                    print(cleaned_word)

dictionary = load_words(dictionary_file)
check_spelling(file_to_check, dictionary)