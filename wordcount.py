
import sys

def parse_words_in_file(input_file):
    """Parse the words in file and create a list."""

    words_file = open(input_file)
    
    words_list = []

    for line in words_file:
        words_list.extend(line.rstrip().split(" "))
        
    return words_list

def normalize_words_list(words_list):
    """Normalize the words in a list.
    Strips non-alphanumeric characters and
    converts alphanumeric strings to lowercase."""

    normalized_list = []

    for word in words_list:
        word = word.lower()
        # strip punctuation
        for ch in word:
            if not ch.isalpha():
                word = word.replace(ch, "")
        normalized_list.append(word)
    
    return normalized_list
        


def count_words_in_list(words_list):
    """Create a dictionary of words with
    the number of times they occur in a list."""

    words_in_file = {}

    for word in words_list:
        words_in_file[word] = words_in_file.get(word, 0) + 1

    return words_in_file

def print_word_report(word_dictionary):
    """Print a dictionary of word counts on each line."""

    for word, count in word_dictionary.items():
        print(word, count)


words_list = parse_words_in_file(sys.argv[1])
normalized_list = normalize_words_list(words_list)
word_dictionary = count_words_in_list(normalized_list)
print_word_report(word_dictionary)