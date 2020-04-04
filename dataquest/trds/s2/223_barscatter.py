import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint as pp
import numpy as np

"""
data dictionary:

FILM - film name
RT_user_norm - average user rating from Rotten Tomatoes, normalized to a 1 to 5 point scale
Metacritic_user_nom - average user rating from Metacritc, normalized to a 1 to 5 point scale
IMDB_norm - average user rating from IMDB, normalized to a 1 to 5 point scale
Fandango_Ratingvalue - average user rating from Fandango, normalized to a 1 to 5 point scale
Fandango_Stars - the rating displayed on the Fandango website (rounded to nearest star, 1 to 5 point scale)
"""



fn='fandango_scores.csv'
dat=pd.read_csv(fn)
pp(dat.info())
pp(dat.head(3))
cols = [
'FILM',
'RT_user_norm',
'Metacritic_user_nom',
'IMDB_norm',
'Fandango_Ratingvalue',
'Fandango_Stars']

norm_reviews = dat[cols]

pp(norm_reviews.head(3))

pp(norm_reviews.describe())

#4
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = np.arange(5) + 0.75

fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.5)
plt.show()


#5
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = np.arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()

ax.bar(bar_positions, bar_heights, 0.5)
#settinng x-ticks
ax.set_xticks(tick_positions)
ax.set_xticklabels(num_cols, rotation=90)

#setting labels
ax.set_xlabel('Rating Source')
ax.set_ylabel('Average Rating')
ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')
plt.show()

#6 vertial bar

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_widths = norm_reviews[num_cols].iloc[0].values
bar_positions = np.arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()
ax.barh(bar_positions, bar_widths, 0.5) #horizontal bar

#now setting y-ticks
ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols)

ax.set_ylabel('Rating Source')
ax.set_xlabel('Average Rating')
ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')
plt.show()

#7 scatter plots
fig, ax = plt.subplots()
ax.scatter( norm_reviews.Fandango_Ratingvalue.values,
            norm_reviews.RT_user_norm.values )
ax.set_xlabel('Fandango')
ax.set_ylabel('Rotten Tomatoes')
plt.show()

#8
fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.scatter( norm_reviews.Fandango_Ratingvalue.values,
            norm_reviews.RT_user_norm.values )

ax2.scatter(norm_reviews.RT_user_norm.values,
            norm_reviews.Fandango_Ratingvalue.values)

ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')

ax2.set_xlabel('Rotten Tomatoes')
ax2.set_ylabel('Fandango')
plt.show()

##9
fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')
ax1.set_xlim(2.5, 5) #hard setting limits
ax1.set_ylim(0, 5)

ax2.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['Metacritic_user_nom'])
ax2.set_xlabel('Fandango')
ax2.set_ylabel('Metacritic')
ax2.set_xlim(2.5, 5)
ax2.set_ylim(0, 5)

ax3.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['IMDB_norm'])
ax3.set_xlabel('Fandango')
ax3.set_ylabel('IMDB')
ax3.set_xlim(2.5, 5)
ax3.set_ylim(0, 5)

plt.show()
