
import pandas as pd
import matplotlib.pyplot as plt

#%matplotlib inline

for ix in range(1,19):
    if ix % 3 ==1:
        print("1st col", ix)
    elif ix %3 ==2:
        print("2nd col", ix)
        if ix ==17:
            print(" #making empty plot here")
    elif ix %3 == 0:
        print("3rd col", ix)


women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)

stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

def rm_spines(x, rmaxes=False):
    x.spines["right"].set_visible(False)
    x.spines["left"].set_visible(False)
    x.spines["top"].set_visible(False)
    x.spines["bottom"].set_visible(False)
    if rmaxes:
        x.axis('off')



## with visuals enhacements
fig = plt.figure(figsize=(18,18))
major_ix = 0
for sp in range(1,19):
    ax = fig.add_subplot(6,3,sp)
    if sp % 3 ==1:
        cu_cat = stem_cats
    elif sp %3 ==2:
        cu_cat = lib_arts_cats
    elif sp %3 == 0:
        cu_cat = other_cats
    if sp == 17:
        rm_spines(ax,rmaxes=True)
        continue
    ax.plot(women_degrees['Year'],women_degrees[cu_cat[major_ix]],
            c=cb_dark_blue, label='Women', linewidth=2)
    ax.plot(women_degrees['Year'], 100 - women_degrees[cu_cat[major_ix]],
            c=cb_orange, label='Men', linewidth=3)

    ax.set_title(cu_cat[major_ix])
    ##chart aestetics
    rm_spines(ax)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0, 100)
    ax.set_yticks([0,100])
    ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)  ###!!! new change
    ax.tick_params(bottom="off", top="off", left="off", right="off", labelbottom='off')
    if major_ix == len(stem_cats) -1 :
        ax.tick_params(labelbottom='on')
    #inline legend
    if sp == 1:
        ax.text(2005, 87, 'Women')
        ax.text(2002, 8, 'Men')
    elif sp == 18:
        ax.text(2005, 60, 'Men')
        ax.text(2005, 35, 'Women')

    if  sp % 3 == 0:
        major_ix += 1
plt.show()