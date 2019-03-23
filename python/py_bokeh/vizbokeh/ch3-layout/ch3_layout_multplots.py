
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.plotting import figure
from bokeh.models.annotations import Span, BoxAnnotation

output_file("nb/ch3/layout.html")


#dummy data
x1,y1=list(range(0,10)),list(range(10,20))
x2,y2=list(range(20,30)),list(range(30,40))
x3,y3=list(range(40,50)),list(range(50,60))

#creat new plot

f1 = figure(width=250,plot_height=250,title="Circles")
f1.circle(x1,y1,size=10, color="navy",alpha=0.5)

f2 = figure(width=250,plot_height=250,title="Triangles")
f2.triangle(x2,y2,size=10, color="firebrick",alpha=0.5)


f3 = figure(width=250,plot_height=250,title="Squares")
f3.square(x3,y3,size=10, color="olive",alpha=0.5)


#create a span annotation
span_4 = Span(location=4,dimension='height',line_color='green',line_width=2) #vertical line
#span_4 = Span(location=14,dimension='width',line_color='green',line_width=2) #horizontal line
f1.add_layout(span_4)

#create a box annotation
box_2_6 = BoxAnnotation(left=2, right=6, fill_color="firebrick", fill_alpha=0.2)
f1.add_layout(box_2_6)


#put all plots in a grid
f = gridplot( [[f1,f2],[None,f3]])
#f = gridplot( [[f1,f2,f3]])

show(f)
