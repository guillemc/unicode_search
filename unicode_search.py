#!/usr/bin/env python3

import unicodedata
from collections import namedtuple

MAX_UNICODE = 1114111

UInfo = namedtuple('UInfo', 'ord chr name category hex utf8 xml')

def search_names(*s):
    return [i for i in range(0, MAX_UNICODE) if matches(i, s)]


def matches(i, search):
    name = unicodedata.name(chr(i), '')
    if not name:
        return False
    for s in search:
        if not s.upper() in name:
           return False
    return True


def info(i):
    if type(i) == int:
        char = chr(i)  # returns the string representing a character whose Unicode code point is i
    else:
        char = i
        i = ord(char)  # ord is the inverse of chr: returns the integer representing the Unicode code point of char
    return UInfo(
        i,
        char,
        unicodedata.name(char),
        unicodedata.category(char),
        hex(i),
        char.encode('utf8'),
        char.encode('ascii', 'xmlcharrefreplace')
    )



if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('term', nargs='+', help='search terms')
    args = parser.parse_args()

    terms = args.term

    result = []

    for term in terms:
        if len(term) == 1:
            result.append(term)

    result.extend(search_names(*terms))

    if not result:
        print('No results for %s' % terms)
    else:
        s = "{ord!s:>7} {chr} {name} ({hex}, {utf8}, {xml})"
        for i in result:
            print(s.format(**info(i)._asdict()))




