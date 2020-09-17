#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line utility that accepts a word file and prints a dictionary of
anagrams for that file.

Module provides a function, find_anagrams(), which can be used to do the same
for an arbitrary list of strings.
"""

# Your name here, and any other people/sources who helped.
# Give credit where credit is due.
__author__ = "marcornett"

import sys
# import timeit
# import cProfile


# def alphabetize(string):
#     """Returns alphabetized version of the string."""
#     return "".join(sorted(string.lower()))


def find_anagrams(words):
    """
    Returns a dictionary with keys that are alphabetized words and values
    that are all words that, when alphabetized, match the key.
    Example:
    {'dgo': ['dog'], 'act': ['cat', 'act']}
    """
    anagrams = {}
    for word in words:
        alphabetized = "".join(sorted(word.lower()))
        if alphabetized not in anagrams:
            anagrams[alphabetized] = [word]
        else:
            anagrams[alphabetized].append(word)
    # anagrams = {alphabetize(word): [w for w in words if alphabetize(
    #     w) == alphabetize(word)] for word in words}
    return anagrams


def main(args):
    # run find_anagrams() on first argument filename
    if len(args) < 1:
        print("Please specify a word file!")
        sys.exit(1)

    with open(args[0]) as f:
        words = f.read().split()
    anagram_dict = find_anagrams(words)
    for k, v in anagram_dict.items():
        print(f"{k} : {v}")


if __name__ == "__main__":
    main(sys.argv[1:])

#     print(timeit.timeit("find_anagrams", setup="""def find_anagrams(words):
#         anagrams = {alphabetize(word): [w for w in words if alphabetize(
#             w) == alphabetize(word)] for word in words}
#         return anagrams;

#         with open(''.join(sys.argv[1:])) as f:
#             words = f.read().split()""", number=10_000))

# print(timeit.timeit('main(["words/short.txt"])',
#                     setup='from __main__ import main', number=20))

# cProfile.run('main(["words/short.txt"])')

# 3.439347607 w/ alphabetize
# 1.905289119 without
