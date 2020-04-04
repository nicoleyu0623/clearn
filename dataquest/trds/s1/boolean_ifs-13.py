

cat =True
dog = False
print(type(cat))

##prepare cities
with open("crime_rates.csv", mode="rt",encoding='utf-8') as f:
    cities = [ line.split('\n')[0].split(',')[0] for line in f.readlines() ]

with open("crime_rates.csv", mode="rt", encoding='utf-8') as f:
    crime_rates = [ int(line.split('\n')[0].split(",")[1]) for line in f.readlines() ]

print(cities[:5])
print(crime_rates[:5])

first_alb = cities[0] == "Albuquerque"
second_alb = cities[1] == "Albuquerque"
first_last = cities[0] == cities[-1]


first_500 = crime_rates[0] > 500
first_749 = crime_rates[0] >= 749
first_last = crime_rates[0] >= crime_rates[-1]

second_500 = crime_rates[1] < 500
second_371  = crime_rates[1] <= 371
second_last = crime_rates[1] <= crime_rates[-1]


result = 0
if cities[2] == "Anchorage":
    result = 1

if crime_rates[0] > 500:
    if crime_rates[1] > 300:
        both_conditions = True

five_hundred_list = [x for x in crime_rates if x > 500]

highest = 0
for  el in five_hundred_list:
    if el > highest:
        highest = el
print("highest: {}".format(highest))
