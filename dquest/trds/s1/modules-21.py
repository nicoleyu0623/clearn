
def average(list_data):
    return sum(list_data)/len(list_data)





#### testing
from pprint import pprint as pp

top5_streams = [2993988783, 1829621841, 1460802540, 1386258295, 1311243745]

total_average=average(top5_streams)

pp(total_average)

import statistics as st

average = st.mean(top5_streams)

pp(average)



import csv
fn="top100.csv"
f = open(fn, mode="rt")
data = csv.reader(f)
music = list(data)

pp(music[:3])

import statistics as st
dir(st)


del music[0] # remove header

track_names = [r[0] for r in music]
stream_numbers =[ int(r[3]) for r in music ]

pp(stream_numbers[:2])


import csv
def read_data(filename):
    f = open(filename,"r")
    music = list(csv.reader(f))
    return music

def get_data(list_data):
    stream_numbers = []
    track_names = []

    for song in list_data[1:]:
        stream_numbers.append(int(song[3]))
        track_names.append(song[0])
    return track_names,stream_numbers

##prints in root module our defined  functions
print(dir())


## pipline

def read_data(filename):
    f = open(filename)
    return list(csv.reader(f))


def get_data(data):
    list1 = []
    list2 = []
    for x in data[1:]:
        list1.append(int(x[3]))
        list2.append(x[0])
    return list1, list2

def ceil(data):
    ceiling = 0
    for x in data:
        if x > ceiling:
            ceiling = x
        else:
            ceiling
    return ceiling

def average(data):
    total = 0
    for x in data:
        total += x
    return total/len(data)

fn="top100.csv"
music=read_data(fn)
stream_numbers,track_names=get_data(music)
average=average(stream_numbers)

pp(average)

import statistics as s
variation=s.stdev(stream_numbers)

print(variation)

from statistics import mean, stdev, median

average=mean(stream_numbers)
variation=stdev(stream_numbers)
med=median(stream_numbers)
