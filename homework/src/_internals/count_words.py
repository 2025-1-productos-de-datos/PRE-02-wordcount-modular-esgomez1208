import os


def count_words(words):

    counter = {}
    for word in words:
        if word in counter:
            counter[word] = counter.get(word, 0) + 1
        else:
            counter[word] = 1
    return counter
