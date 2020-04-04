
def read_csv(filename):
    with open(filename, mode="rt",encoding='utf-8') as f:
        fields = [ line.split('\n')[0].split(',') for line in f.readlines() ]
    del fields[0] #header
    final_list = [ [int(i) for i in x] for x in fields ]
    return final_list


cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")

from pprint import pprint as pp
pp(cdc_list[:10])

def month_births(list_data):
    births_per_month = {}
    for  row in list_data:
        if row[1] not in births_per_month:
            births_per_month[row[1]] = row[4]
        else:
            births_per_month[row[1]] += row[4]
    return births_per_month

cdc_month_births = month_births(cdc_list)

pp(cdc_month_births)


def dow_births(list_data):
    day_counts = {}
    for  row in list_data:
        if row[3] not in day_counts:
            day_counts[row[3]] = row[4]
        else:
            day_counts[row[3]] += row[4]
    return day_counts

cdc_day_births = dow_births(cdc_list)

pp(cdc_day_births)


def calc_counts(list_data, column_index):
    counts = {}
    for row in list_data:
        if row[column_index] not in counts:
            counts[row[column_index]] = row[4]
        else:
            counts[row[column_index]] += row[4]
    return counts

#cdc_year_births
pp( calc_counts(cdc_list, column_index=0 ))
#cdc_month_births
pp( calc_counts(cdc_list, column_index=1 ))
#cdc_dom_births
pp( calc_counts(cdc_list, column_index=2 ))
#cdc_dow_birhs
pp( calc_counts(cdc_list, column_index=3 ))

def dict_min_max(dict):
    mx = max([v for v in dict.values()])
    mn = min([v for v in dict.values()])
    return mn,mx

z={'a':1, 'b':-8, 'c':5}

print(dict_min_max(z))


cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
ssa_list = read_csv("US_births_2000-2014_SSA.csv")

pp(cdc_list[-1])
pp(ssa_list[0])

