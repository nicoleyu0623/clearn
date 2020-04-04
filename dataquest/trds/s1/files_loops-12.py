from banners import *

f = open("crime_rates.csv", "rt")
data = f.read() #all file contents in 1 string
print(data)
f.close()

rows = data.split('\n')  # creates a list of lines
print(rows[:5])

ten_rows = rows[0:10]

starprint("printint 10 elements")
for row in ten_rows:
    print(row)

final_data=[]
for row in rows:
        elems = row.split(',')
        final_data.append(elems)

print(final_data[:5])

starprint("extracting subelemtns from list of list")

five_elements = final_data[:5]

cities_list=[]
for el in five_elements:
    cities_list.append(el[0])

print(cities_list)

cities_list = [] #reempty again
for row in final_data:  # all 73 cities from ds
    cities_list.append(row[0])

starprint("printing all cities")
print(cities_list)

### types

rows = data.split('\n')
int_crime_rates = []
for row in rows:
    els = row.split(",")
    int_crime_rates.append(int(els[1]))

print(int_crime_rates[:5])