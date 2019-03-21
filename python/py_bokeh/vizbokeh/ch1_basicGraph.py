from bokeh.plotting import figure
from bokeh.io import output_file,show,save
import pandas as pd

df=pd.read_csv("http://pythonhow.com/data/bachelors.csv")
x=df['Year']
y=df['Engineering']

output_file("nb/ch1/data_csv_womens.html")
f1=figure()
f1.line(x,y)
show(f1)