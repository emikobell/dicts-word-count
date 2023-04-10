
import sys

def parse_words_in_file(input_file):
    """Parse the words in file and create a list."""
    words_file = open(input_file)
    
    words_list = []

    for line in words_file:
        words_list.extend(line.rstrip().split(" "))
        
    return words_list

# print(parse_words_in_file(sys.argv[1]))

def count_words_in_list(words_list):
    words_in_file = {}

    for word in words_list:
        words_in_file[word] = words_in_file.get(word, 0) + 1

    return words_in_file

def print_word_report(word_dictionary):
    for word, count in word_dictionary.items():
        print(word, count)


# word_dictionary = count_words_in_file(sys.argv[1])
# word_dictionary = count_words_in_file('twain.txt')
# word_dictionary = count_words_in_file('test.txt')

words_list = parse_words_in_file(sys.argv[1])
word_dictionary = count_words_in_list(words_list)
print_word_report(word_dictionary)