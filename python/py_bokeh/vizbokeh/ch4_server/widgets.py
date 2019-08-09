#from bokeh.io import output_file, show
from bokeh.io import curdoc

from bokeh.models.widgets import TextInput, Button, DatePicker, Select, Paragraph
from bokeh.layouts import layout, column, row



#prep bokeh output file
#output_file=("../nb/ch4/simple_bokeh.html")  ##do not need for bokeh server

def update(attrname, old, new):
    output.text="hello, " + text_input.value + " at " \
                + dt_picker.value.strftime('%Y-%m-%d') \
                + " with option " +  dummy_select.value

def updateBtn():
    update(attrname=None,old=None,new=None)

text_input=TextInput(value="Ivana")
button=Button(label="Generate Text")


dt_picker_ = DatePicker(min_date='2010-01-01',
                       max_date='2018-03-28',
                       value='2018-03-27')


dummy_select = Select(
                      value='select an option',
                      options=['a','b'])



output=Paragraph()

button.on_click(updateBtn)
dummy_select.on_change('value',update)
dt_picker.on_change('value',update)

lay_out=layout([[text_input,button,dt_picker],[output]])



#show(lay_out)
#curdoc().add_root(lay_out)

# curdoc().add_root(
#     column(
#         row(text_input),
#         row(dummy_select),
#         row(dt_picker),
#         row(button),
#         row(output)
#     )
#)

curdoc().add_root(
    column(
        row(dummy_select,dt_picker),
        row(text_input,button),
        row(output)
    ),
)


curdoc().title = "Widgets Demo"

