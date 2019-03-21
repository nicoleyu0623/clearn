#!/usr/bin/env python3
"""Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>

"""

import sys
from urllib.request import urlopen

## exmaples of functions


def fetch_words(url):
    """ Fetch a list fo words from a URl.
    Args:
     url:  the Url of a UTF-8 text document

    Returns:
        A list of string containing the words
        from the document
    """

    """the above is from google python stile"""

    story_words = []
    with urlopen(url) as story:
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """ Print items per line.
    Args:
     items: An iterable series of printable items
    """
    for item in items:
            print(item)


def main(url):
    """Print a list of words from a text document from a URL
    Args:
        url: the URL of an UTF-8 text document
    """

    """'http://sixty-north.com/c/t.txt'"""
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])# the oth argument is the module filename

