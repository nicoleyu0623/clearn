#Categorical axes

#importing libraries
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models.annotations import Label, LabelSet
from bokeh.models import ColumnDataSource

#prepare the output
output_file("nb/ch3/students.html")

#crate columndatasource
source=ColumnDataSource(dict(average_grades=["B+","A","D-"],
                             exam_grades=["A+","C","D"],
                             student_names=["Stephan","Helder","Riazudidn"]))

#create the figure
f = figure(x_range=["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"],
           y_range=["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"])


#add description label  (x=7 element position in x_range)
description=Label(x=7,y=1,
                  text="This graph shows average grades and exam grades for 3rd grade students",
                  render_mode="css")
f.add_layout(description)

#add labels for glyphs  (student_names will be corresponding to glyphs)
labels=LabelSet(x="average_grades",
                y="exam_grades",
                text="student_names",
                x_offset=5, y_offset=5, source=source)
f.add_layout(labels)

#create glyphs
f.circle(x="average_grades",
         y="exam_grades",
         source=source, size=11,alpha=0.5)

show(f)
