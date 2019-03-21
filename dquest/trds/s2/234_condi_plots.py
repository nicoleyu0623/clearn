import pandas as  pd

from pprint import pprint as pp

import seaborn as sns
import matplotlib.pyplot as plt


"""
titatnic data dictionary  train.csv
PassengerId -- A numerical id assigned to each passenger.
Survived -- Whether the passenger survived (1), or didn't (0).
Pclass -- The class the passenger was in.
Name -- the name of the passenger.
Sex -- The gender of the passenger -- male or female.
Age -- The age of the passenger. Fractional.
SibSp -- The number of siblings and spouses the passenger had on board.
Parch -- The number of parents and children the passenger had on board.
Ticket -- The ticket number of the passenger.
Fare -- How much the passenger paid for the ticket.
Cabin -- Which cabin the passenger was in.
Embarked -- Where the passenger boarded the Titanic.

"""

fn='titanic/train.csv'
tfolks = pd.read_csv(fn)


pp(tfolks.isnull().sum() )

num_cols = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]

titanic = tfolks[num_cols]

titanic.dropna(inplace=True) #drop rows with NaS  ?

sns.distplot(titanic["Fare"])   #by default frequncy distrib + pdf
plt.show()

sns.distplot(titanic["Age"])  #plot 1
plt.show()

#4
sns.kdeplot(titanic["Age"],shade=True) #jsut a p density func
plt.xlabel("Age")
plt.show()

#5
sns.set_style("white")
sns.kdeplot(titanic["Age"],shade=True)
sns.despine(top=True, right=True, left=True,bottom=True)  #no axe frame
plt.xlabel("Age")
plt.show()


#6
# Condition on unique values of the "Survived" column.
g = sns.FacetGrid(titanic, col="Pclass", size=6)
sns.despine(top=True, right=True, left=True,bottom=True)
# For each subset of values, generate a kernel density plot of the "Age" columns.
g.map(sns.kdeplot, "Age", shade=True)
#g.map(plt.hist, "Age")  #for histograms
plt.show()


#7  2 params makes a 2 x 3 grid
g = sns.FacetGrid(titanic, row="Pclass", col="Survived", size=6)
g.map(sns.kdeplot, "Age", shade=True)
plt.show()

#8
sns.despine(top=True, right=True, left=True,bottom=True)
g = sns.FacetGrid(titanic, row="Pclass", col="Survived", hue="Sex", size=3)
g.map(sns.kdeplot, "Age", shade=True)
plt.show()

#9
g = sns.FacetGrid(titanic, row="Pclass", col="Survived", hue="Sex", size=3)
g.map(sns.kdeplot, "Age", shade=True)
g.add_legend()
sns.despine(left=True,bottom=True)
plt.show()
