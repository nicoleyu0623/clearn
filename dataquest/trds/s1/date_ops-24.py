from banners import *
from pprint import pprint as pp
import csv


fn="global_rankings.csv"
f = open(fn, mode="rt")
data = csv.reader(f)
music = list(data)

starprint("contents of music list of list")
pp(music[:2])

from datetime import datetime

jan_27_1965 = datetime(1965, 1, 27, 12, 43)
aug_3_1972 = datetime(1972, 8, 3, 1, 43)
oct_31_2000 = datetime(2000, 10, 31, 15, 12)
mar_2_2017 = datetime(2017, 3, 2, 7, 30)



Jun_2_08 = datetime.strptime("6-02-2008", '%m-%d-%Y')
Jul_15_01 = datetime.strptime("7?15?2001", '%m?%d?%Y')
dec_20_08 =  datetime.strptime("12--30--2010", '%m--%d--%Y')


def string_to_date(listoflist):
    modlist = [ x[:-2]
                + [ datetime.strptime(x[-2], '%Y-%m-%d') ]
                + [x[-1]]  for x in music[1:] ]
    return modlist

def string_to_date_c(music):
    add_date = []
    for track in music[1:]:
        track[-2] = datetime.strptime(track[-2], '%Y-%m-%d')
        add_date.append(track)
    return add_date

## Run ->  profile
cleaned_music= string_to_date(music)
#cleaned_music=string_to_date_c(music)


def get_month(cmusic):
     data = [  x + [x[-2].month] for x in cmusic]
     return data


add_month= get_month(cleaned_music)

starprint("added month")
print(add_month[:2])


def get_day(cmusic):
    data = [x + [x[-3].day] for x in cmusic]
    return data

add_day = get_day(add_month)


def organize_by_month(cleaned_music):
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    organized = dict()
    for month in months:
        tracks_in_month = []
        for track in cleaned_music:
            if track[-2] == month:
                tracks_in_month.append(track)
        organized[month] = tracks_in_month
    return organized

def aggregate(organized):
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    monthly_sum = dict()

    for month in months:
        tracks = organized[month]
        # Need the track name, artist and number of streams
        groups = dict()
        for t in tracks:
            track_name = t[2]
            if track_name not in groups.keys():
                groups[track_name] = int(t[3])
            else:
                groups[track_name] += int(t[3])
        monthly_sum[month] = groups
    return monthly_sum

organized = organize_by_month(add_day)
aggregated = aggregate(organized)

#pp(aggregated[1])

months = [1,2,3,4,5,6,7,8,9,10,11,12]

top_songs_by_month=[]


sorted_dict = {}
for m in months:
    sorted_dict[m] = sorted( aggregated[m].items(), key=lambda x:x[1],reverse=True)

top_songs_by_month = []
for k in sorted_dict.keys():
    top_songs_by_month.append(sorted_dict[k][0])

pp(top_songs_by_month)






