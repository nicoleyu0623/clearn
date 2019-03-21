
##prep data


fn = "la_weather.csv"
with open(fn, mode="rt",encoding='utf-8') as f:
    weather_data = [ line.split('\n')[0].split(',') for line in f.readlines() ]

del weather_data[0]
weather = [el[1] for el in weather_data]


first_element = weather[0]
print(first_element)
last_element = weather[-1]
print(last_element)

superhero_ranks = {}
superhero_ranks['Aquaman'] = 1
superhero_ranks['Superman'] = 2

president_ranks = {}
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3

fdr_rank = president_ranks['FDR']
lincoln_rank = president_ranks['Lincoln']
aquaman_rank = president_ranks['Aquaman']


animals = { 7: 'raven', 8:'goose', 9:'duck'}

times = {'morning':9, 'afternoon':14, 'evening':19, 'night':23}

students = {
    "Tom": 60,
    "Jim": 70
}
students['Ann'] = 85
students['Tom'] = 80
students['Jim'] += 5

planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}

jupiter_found = "jupiter" in planet_numbers
earth_found = "earth" in planet_numbers

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]

short_names = [ x for x in planet_names if len(x) <=5 ]
long_names = [ x for x in planet_names if len(x) > 5 ]

pantry = ["apple", "orange", "grape", "apple", "orange", "apple",
          "tomato", "potato", "grape"]

pantry_counts= {}

for el in pantry:
    if el not in pantry_counts:
        pantry_counts[el] = 1
    else:
        pantry_counts[el] += 1

weather_counts = {}
for day in weather:
    if day not in weather_counts:
        weather_counts[day] = 1
    else:
        weather_counts[day] += 1




