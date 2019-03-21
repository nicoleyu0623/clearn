#Categorical axes

#importing libraries
from bokeh.io import curdoc

from bokeh.plotting import figure
from bokeh.models.annotations import LabelSet
from bokeh.models import ColumnDataSource

from bokeh.models.widgets import Select
from bokeh.layouts import layout

#crate columndatasource
source=ColumnDataSource(dict(average_grades=["B+","A","D-"],
                             exam_grades=["A+","C","D"],
                             student_names=["Stephan","Helder","Riazudidn"]))

#create the figure
f = figure(x_range=["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"],
           y_range=["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"])

#add labels for glyphs
#"student_names" initial value for lavels
labels=LabelSet(x="average_grades",
                y="exam_grades",
                text="student_names",
                x_offset=5, y_offset=5, source=source)
f.add_layout(labels)

#create glyphs
f.circle(x="average_grades", y="exam_grades", source=source, size=8)

#call back for select
def update_labels(attr,old,new):   #callback signagure: attr,old,new
    labels.text=select.value

#create select widget   #tuple[0] element correspnends to dict key in source
options=[("average_grades","Average Grades"),
         ("exam_grades","Exam Grades"),
         ("student_names","Student Names")]
select=Select(title="Info to show",options=options)

select.on_change("value",update_labels)  #on_change  calls a call_back  update_labels

#create layout and add to curdoc
lay_out=layout([[select]])   #layout have  1 Select UI widget
curdoc().add_root(f)           #curdoc has a figure and a a layout
curdoc().add_root(lay_out)
