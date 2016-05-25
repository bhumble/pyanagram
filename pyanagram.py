#!/usr/bin/python

import argparse
from collections import defaultdict

def is_anagram(s1, s2, threshold = 0):
    c1 = [0] * 95 # 95 covers ' ' through '~' (including all alphanumerics) on the ASCII table
    c2 = [0] * 95

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord(' ')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord(' ')
        c2[pos] = c2[pos] + 1

    diff = 0
    for i in range(len(c1)):
        if c1[i] != c2[i]:
            diff += abs(c2[i] - c1[i])

    return diff <= threshold


def get_dictionary(filename='/usr/share/dict/words'):
    with open(filename) as f:
        for word in f:
            yield word.rstrip()
            
# Parse command-line:
parser = argparse.ArgumentParser(description='Print all anagrams of provided string.')
parser.add_argument('str', help='string to find anagrams of')
i_parser = parser.add_mutually_exclusive_group(required=False)
i_parser.add_argument('-i', '--ignore-case', dest='i', action='store_true', help="ignore case when finding anagrams")
i_parser.add_argument('-n', '--no-ignore-case', dest='i', action='store_false', help="don't ignore case when finding anagrams")
parser.set_defaults(i=True)
parser.add_argument('-t', '--threshold', dest='t', default=0, type=int, help='allow up to <T> fewer/additional characters when finding anagrams')
args = parser.parse_args()

words = get_dictionary()
for word in words:
    if is_anagram(args.str.lower() if args.i else args.str, word.lower() if args.i else word, args.t):
        print(word)
