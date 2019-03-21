from pprint import pprint as pp
from bokeh.plotting import figure
from bokeh.io import output_notebook, output_file, show,save
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool,WheelZoomTool

### just execute this python file

output_file("nb/ch2/iris.html")
#Create the figure object
f = figure()

#style the tools   dir(bokeh.models.tools)

f.tools = [PanTool(),ResetTool(),WheelZoomTool()]  #just allow  Pan and Reset tool
f.toolbar_location = 'above' #below, right, left
f.toolbar.logo= None

#customized hoover ojbect
hover = HoverTool(tooltips=[("Species","@species"),
                            ("Sepal Width","@sepal_width")])
f.add_tools(hover)  #hover tool move cursor on data point to see number behind

#stylize the plot area (chart size!)
f.plot_width=900
f.plot_height=500

##colors
#f.background_fill_color="olive"
f.background_fill_color="#BFEBBB"
f.background_fill_alpha=0.25
#f.border_fill_color="orange"  #color the border area

#style the title
f.title.text="Iris Morphology"
f.title.text_color="blue"
f.title.text_font="Arial"
f.title.text_font_size="28px"
f.title.align="center"


#Style the axes
# ticks, majors, minors
f.yaxis.minor_tick_line_color="green"  #y_axis
f.xaxis.minor_tick_line_color="blue" #x_axis

#f.axis.minor_tick_line_color="yellow" #on both axis
f.yaxis.major_label_orientation="vertical"  # major ticks numbers rotated 90 degrees
f.xaxis.visible=True # do not show axis
f.xaxis.minor_tick_in= -6  #negative values allowed, shows inside ticks outside the axis
#f.xaxis.minor_tick_out=8
#labels
f.xaxis.axis_label="Petal Lenght"
f.yaxis.axis_label="Petal Width"
f.xaxis.axis_label_text_font_size="18px" #size of axis label text
f.axis.axis_label_text_color="blue"
f.axis.major_label_text_color="orange"


#axis geomegry
#specify explicitly limits of plot range !

##range can be dynamic, see ch2_iris_styling_Ex3Sol.py

f.x_range=Range1d(start=0,end=10, bounds=(-3,9)) #bounds() limits where you pan chart
f.y_range=Range1d(start=0,end=5)
f.xaxis.bounds=(1,6)  #put axis on a specified region only
f.xaxis[0].ticker.desired_num_ticks=3 #how many major ticks you one on xaxis
f.yaxis[0].ticker.desired_num_ticks=2  #on y axis

f.yaxis[0].ticker.num_minor_ticks=5 #number of minor ticks

#Style the grid
#f.xgrid.grid_line_color = None
f.xgrid.grid_line_color = "grey"
f.ygrid.grid_line_color = 'brown'
f.ygrid.grid_line_alpha = 0.9
f.grid.grid_line_dash = [5,3]
f.grid.minor_grid_line_color = (128, 128, 0, 0.1)
f.grid.minor_grid_line_dash = [3, 3]


### color codes for distinct species
colormap={'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
## add new column to flowers df
flowers['color']=[colormap[x] for x in flowers['species']]


#adding glyphs
specie="setosa"
for specie in list(flowers.species.unique()):
    f.circle(x=flowers.loc[flowers["species"]==specie,"petal_length"],
         y=flowers.loc[flowers["species"]==specie,"petal_width"],
         size=flowers.loc[flowers["species"]==specie,'sepal_width']*4,
         fill_alpha=0.2,
         color=flowers.loc[flowers["species"]==specie,'color'],  #color param is set for every data set
         line_dash=[5,3],legend=specie
    )


#style the legend
f.legend.location = 'top_left'
#f.legend.location = (100,250) #explicit location in x,y pixesl from bottom left corner
f.legend.background_fill_alpha = 0.9  #no white backgournd on legend
f.legend.border_line_color = None
f.legend.margin = 10
f.legend.padding = 18 # does not seem to work
f.legend.label_text_color = 'olive'
f.legend.label_text_font = 'times'
f.legend.label_text_font_size='12px'


show(f)

##debug
pp(flowers.species.unique() )
