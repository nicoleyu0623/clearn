import os
import sys
from pprint import pprint as pp

pd=os.path.dirname(os.getcwd())
ppd=os.path.dirname(pd)
sys.path.extend([pd,ppd])
## added parent 2 folders to import util
from util import *

from functools import reduce



def count_words(doc):
    normalised_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalised_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies



def combine_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count # d.get() gets an item for key word with 0 as default value
        #if word key not in d it gets created and assigned 0 + count
        #if word key is in d it gets updated and assigned d.get(word) + count
    return d


def demo_combine_word_counts_via_map_reduce():

    documents = [
        'It was the best of times, it was the worst of times.',
        'I went to the woods because I wished to live deliberately, to front only the essential facts of life...',
        'Friends, Romans, countrymen, lend me your ears; I come to bury Caesar, not to praise him.',
        'I do not like green eggs and ham. I do not like them, Sam-I-Am.'
    ]

    pp('total number of documents to process: {}'.format(len(documents)))
    counts = map(count_words, documents)


    total_count = reduce(combine_counts, counts)

    starprint('total documents word counts')
    pp(total_count)


if __name__ == '__main__':
    demo_combine_word_counts_via_map_reduce()
