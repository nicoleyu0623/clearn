
fn = "movie_metadata.csv"
with open(fn, mode="rt",encoding='utf-8') as f:
    movie_data = [ line.split('\n')[0].split(',') for line in f.readlines() ]

del movie_data[0]
print(movie_data[:2])

def first_elts(data):
    movies = [ x[0] for x in data ]
    return movies

movie_names =first_elts(movie_data)
print(movie_names[:5])


def is_usa(movie, data):
    movies = [x[0] for x in data]
    try:
        idx = movies.index(movie)

        if data[idx][6] == "USA":
            return True
        else:
            return False
    except (ValueError, TypeError):
        print("movie title failed")
        return False

print(is_usa("Avatar", movie_data))
print(is_usa("Spectre", movie_data))


wonder_woman = [['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]]

wonder_woman_usa = is_usa('Wonder Woman', wonder_woman)
print(wonder_woman_usa)

def index_equals_str(list_data, list_index, str_value):
    try:
        if list_data[int(list_index)] == str_value:
            return True
        else:
            return False
    except (ValueError, TypeError):
        print("list_index of wrong type")
        return False

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

wonder_woman_in_color = index_equals_str(wonder_woman, list_index=2, str_value="Color")

print(wonder_woman_in_color)



def feature_counter(list_data, list_index, str_value):
    feature = [x[list_index] for x in list_data]
    cnt = sum(1 for x in feature if x == str_value)
    return cnt


cnt_title = feature_counter(movie_data, 0, "Avatar")
print(cnt_title)

num_of_us_movies = feature_counter(movie_data, 6, "USA")
print(num_of_us_movies)

cnt_uk = feature_counter(movie_data, 6, "UK")
print(cnt_uk)

def summary_statistics(data):
    num_japan_films = feature_counter(data, 6, "Japan")
    num_color_films = feature_counter(data, 2, "Color")
    num_films_english = feature_counter(data, 5, "English")

    summ_stats = {}
    summ_stats["japan_films"] = num_japan_films
    summ_stats["color_films"] = num_color_films
    summ_stats["films_in_english"] = num_films_english
    return summ_stats

summary = summary_statistics(movie_data)
print(summary)
