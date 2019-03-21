#from bokeh.io import output_file, show
from bokeh.io import curdoc

from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout


#prep bokeh output file
#output_file=("../nb/ch4/simple_bokeh.html")  ##do not need for bokeh server

text_input=TextInput(value="Ivana")
button=Button(label="Generate Text")

output=Paragraph()

def update():
    output.text="hello, " + text_input.value


button.on_click(update)

lay_out=layout([[button,text_input],[output]])



#show(lay_out)

curdoc().add_root(lay_out)