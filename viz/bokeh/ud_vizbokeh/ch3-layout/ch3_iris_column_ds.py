#Plotting flower species

#Importing libraries
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, ColumnDataSource, LabelSet

#additional columns to df defined before  CoumnDataSource attachment


colormap={'setosa':'red','versicolor':'green','virginica':'blue'}
flowers['color'] = [colormap[x] for x in flowers['species']]
flowers['size'] = flowers['sepal_width'] * 4

urlmap = {'setosa':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/800px-Kosaciec_szczecinkowaty_Iris_setosa.jpg',
        'versicolor':'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/800px-Blue_Flag%2C_Ottawa.jpg',
        'virginica':'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/800px-Iris_virginica.jpg'}
flowers['imgs'] = [urlmap[x] for x in flowers['species']]

setosa = ColumnDataSource(flowers.loc[flowers["species"]=="setosa",:])
versicolor = ColumnDataSource(flowers.loc[flowers["species"]=="versicolor",:])
virginica = ColumnDataSource(flowers.loc[flowers["species"]=="virginica",:])

ds={}
ds['setosa'] = {'dsrc':setosa, 'label':"Setosa"}
ds['versicolor'] = {'dsrc':versicolor, 'label':"Versicolor"}
ds['virginica'] = {'dsrc':virginica, 'label':"Virginica"}



#Define the output file path
output_file("nb/ch3/iris.html")

#Create the figure object
f = figure()

#adding glyphs

for k in ds.keys():
    f.circle(x="petal_length", y="petal_width", size='size', fill_alpha=0.2,
    color="color", line_dash=[5,3], legend=ds[k]['label'], source=ds[k]['dsrc']) #calls columnDataSource



#style the tools
f.tools = [PanTool(),ResetTool()]

#hover = HoverTool(tooltips=[("Species","@species"),("Sepal Width","@sepal_width")])

#tooltips param has a html code iside triple quotes
hover=HoverTool(tooltips="""
    <div>
            <div>
                <img
                    src="@imgs" height="42" alt="@imgs" width="42"
                    style="float: left; margin: 0px 15px 15px 0px;"
                    border="2"
                ></img>
            </div>
            <div>
                <span style="font-size: 15px; font-weight: bold;">@species</span>
            </div>
            <div>
                <span style="font-size: 10px; color: #696;">Petal length: @petal_length</span><br>
                <span style="font-size: 10px; color: #696;">Petal width: @petal_width</span>
            </div>
        </div>
""")

f.add_tools(hover)
f.toolbar_location="above"
f.toolbar.logo=None

#Style the legend
f.legend.location = (575,555)
f.legend.location = 'top_left'
f.legend.background_fill_alpha = 0
f.legend.border_line_color = None
f.legend.margin = 10
f.legend.padding = 18
f.legend.label_text_color = 'olive'
f.legend.label_text_font = 'times'

#Save and show the figure
show(f)
