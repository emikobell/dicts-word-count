"""Count words in file."""


def count_words_in_file(input_file):
    words_file = open(input_file)
    words_in_file = {}

    for line in words_file:
        words = line.rstrip().split(" ")
        for word in words:
            words_in_file[word] = words_in_file.get(word, 0) + 1

    return words_in_file

def print_word_report(word_dictionary):
    for word, count in word_dictionary.items():
        print(word, count)


word_dictionary = count_words_in_file('twain.txt')
# word_dictionary = count_words_in_file('test.txt')
print_word_report(word_dictionary)