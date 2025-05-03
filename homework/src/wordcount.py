# obtain a list of files in the input directory
import os

from homework.src._internals.count_words import count_words
from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.split_into_words import split_into_words
from homework.src._internals.write_word_counts import write_word_counts


def main():

    # mover a la función read_all_lines
    all_lines = read_all_lines()

    # mover a "preprocess_lines"
    all_lines = preprocess_lines(all_lines)

    # mover a "split_in_words"
    words = split_into_words(all_lines)

    # mover a "count_words"
    counter = count_words(words)

    ##
    write_word_counts(counter)


if __name__ == "__main__":
    main()
