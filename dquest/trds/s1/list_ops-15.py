
fn = "la_weather.csv"
with open(fn, mode="rt",encoding='utf-8') as f:
    weather_data = [ line.split('\n')[0].split(',') for line in f.readlines() ]

#del weather_data[0]
print(weather_data[:3])

weather = [el[1] for el in weather_data]

print(weather[:3])

count=len(weather)

new_weather = weather[1:]

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]

weather_type_found = [ x in new_weather for x in weather_types]
