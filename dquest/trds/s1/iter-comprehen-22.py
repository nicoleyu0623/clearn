from banners import *

from pprint import pprint as pp

import csv
fn="top100.csv"
f = open(fn, mode="rt")
data = csv.reader(f)
music = list(data)



pp(music[:2])

artists = [ r[1] for r in music[1:] ] # skip header

pp(artists[:3])


def counter(artists_list):
    freqs = {}
    for a in artists:
        if a not in freqs:
            freqs[a] = 1
        else:
            freqs[a] += 1
    return freqs

#pp(counter(artists))

from collections import Counter

tallies = Counter(artists)
counts = dict(tallies.items())

artist_counts = [[key,value] for key,value in counts.items()]

pp(artist_counts[:3])

sample = [
            [1,2,3,4,5],
            [4,4,5],
            [3,2]
         ]

sample.sort(key=len)
pp(sample)

def by_count(x):
    return x[1]

artist_counts.sort(key=by_count,reverse=True)
pp(artist_counts[:4])


f = lambda x: x + 1

artist_counts = [[key,value] for key,value in counts.items()]
artist_counts.sort(key=lambda x:x[1],reverse=True)
pp(artist_counts[:4])


def extract_artist(data):
    artists = [r[1] for r in data[1:]]  # skip header
    return artists

def get_count(list_artists):
    tallies = Counter(artists)
    counts = dict(tallies.items())
    artist_counts = [[key, value] for key, value in counts.items()]
    return artist_counts

def sort_by_streams(artist_cnt):
    artist_cnt.sort(key=lambda x: x[1], reverse=True)
    return artist_cnt

artists = extract_artist(music)

artist_counts = get_count(artists)

top = sort_by_streams(artist_counts)

banner("last test")
pp(top[:10])

