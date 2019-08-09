## based on course by ardit Sulce.   
Data Visualization on the Browser with Python and Bokeh


bokeh version used incourse = 0.13.0  (current version is 1.0.4)

pip3 install bokeh==0.13.0

in pycharm createed new project with VirtualEnv    ~/venv/bokeh   with pythong 3.6

installation: 

cd  ~/venv/bokeh
bin/pip3 install bokeh==0.13.0

this installs also dependencies, including Jinja2, numpy(1.16.1), PyYAML, tornado(5.1.1)

also, lets install a version of pandas 0.23.4
bin/pip3 install pandas==0.23.4


install also jupyter
bin/pip3 install jupyter 

source ~/venv/bokeh/bin/activate

start jupyter in the env
cd ~
venv/bokeh/bin/jupyter notebook   # jupyter notebook starts with correct venv's python kernel and local packages


==================== contents ===============================
ch1 Getting Started
ch2 Customizing Bokeh Graphs
ch3 Advanced Plotting
ch4 Boker Server: Interactive Plotting with HTML Widgets
ch5 Boker Server: Streaming Real Time Data
ch6 Embedding Bokeh Plots in WebSites
ch7 Deploying Bokeh Data Visualization Apps in Live Servers
=============================================================

-------------------
ch1 getting started
--------------------
    bokeh in  Interactive jupyter session bug

    1. instead of show(f) use save(f) to overwrite your plot, not to append it
    2. using bokeh non-interactively as python  bokeh_code.py

    official doc   bokeh.pydata.org
    complete API: Refererence Guide !

----------------------------
ch2 Customizing Bokeh Graphs
----------------------------

    nb/ch2/iris_styling.ipynb
    f.background_fill_color="#BFEBBB"  #can use rgb picker

    some font names that could be used in bokeh:
    Antiqua, Arial, Calibri, Courier, Fraktur,Helvetica, Modern,Monospace,Open Sans, Palatino, roman, Sans-serif,Serif,Swiss,Times, Times New Roman, Verdana


   ch2_iris.styling.py    styles, axes, ticks, colors,  color of data, alpha, legend

--------------------
ch3 Advanced Plotting
--------------------
    columnDataSource (needed for hoover and used to draw glyphs)
    hovertools customized with data  (iris)
    layout multiple plots
    span annotation (lines)
    box_annotations (rectangles)
    labels for specific glyphs  ch3_categorical_labels.py

----------------------------------------------------------
ch4 Boker Server: Interactive Plotting with HTML Widgets
----------------------------------------------------------

    bokeh server
    >python -m bokeh serve widgets.py  #basic example
    >bokeh serve widgets.py
    >bokeh serve --port 5007 dyn_chart_labels_select.py

    >server zimine$ bokeh serve --disable-index-redirect  --port 5006 \
       --allow-websocket-origin=127.0.0.1:5006  dyn_slyder_labels.py
           filters dta on slider vales, chnages labels
    selecgt_span_ex8Sol how to dynamically compute values of Select UI

-------------------------------------------
ch5 Boker Server: Streaming Real Time Data
-------------------------------------------

    streaming in bokeh server
    random_generator_chart.py
    bitcoin_stream-webscrap.py
    bitcoint_stream_widgets.py

-------------------------------------
ch6 Embedding Bokeh Plots in WebSites
-------------------------------------

    venv/bokeh/bin/pip3 install Flask
    ch6_inflask    flaskapp0    python flaskapp0/app.py how to embed a basic line chart (this starts the flask web server)

    embedding dynamic bokeh charts  (2 separate processes) 
    ## bokeh tornado runs on 5006
    #  flask runs on 5000
    bokeh serve  --allow-websocket-origin=localhost:5000   random_generator.py  
    python app.py  # runs on port 5000 
    (flask must also be running, user access  localhost:500)


    
    djangoapp0   (better for big apps), flask more flexible
    django-admin startproject mysite
    cd djangoapp0/mysite
    python manage.py startapp bokehapp
    #to run the server
    python manage.py runserver 

-----------------------------------------------------------
ch7 Deploying Bokeh Data Visualization Apps in Live Servers
-----------------------------------------------------------

 copied flaskapp0  from ch6
 made account of on digitalocean.com 
 droplet 5/mo   1gb/1cpu 25 gb ssd  1000 gb network
 name: do-lon1-01  credentials are sent to email

tar cvf - ch7_deploy | compress >  ch7_deploy.tar.Z
created ch7_deploy.tar.Z  and transfered to do-lon1-01
sftp tar.Z to root@do-lon1-01_ip
ssh root@do-lon1-1_ip

################################
## instaling packaging, virtual environment
################################
untar 
cd ch7-deploy/pkg
./install_debian_packages.sh
./mk_venv.sh
. /opt/envs/virtual/bin/activate  (deactivate)
./install_pip_packages.sh

################################
## copy webapp and config code 
################################
cd ch7-deploy
cp -r flaskapp0/* /opt/webapps/bokehflask/

## config
################################
cd webapp_config
#overwrite
cp default  /etc/nginx/sites-available/default
cp bokeh_serve.conf  etc/supervisor/conf.d/ 
cp flask_conf  etc/supervisor/conf.d/

##modify config files 
/opt/webapps/bokehflask/app.py

- Add "from werkzeug.contrib.fixers import ProxyFix" to the remote app.py file.
- Modify the index function as follows: 
def index():
    url="http://104.236.40.212:5006"
    session=pull_session(url=url,app_path="/random_generator")
    bokeh_script=autoload_server(None,app_path="/random_generator",session_id=session.id, url=url)
    return render_template("index.html", bokeh_script=bokeh_script)
- Add "app.wsgi_app = ProxyFix(app.wsgi_app)" to the remote app.py file after the index function.

make sure this file changes sits in  /opt/webapps/bokehflask/app.py

- Open the bokeh_serve.conf file with "nano /etc/supervisor/conf.d/bokeh_serve.conf" and put your IP (from digital ocean) for --allow-websocket-origin and your IP and port 5006 for --host 

##starting services
service nginx restart  #nginx is a high perf webserver
service supervisor restart # a process conrol system 


erros with bokeh v 1.0.4
the index()  func in app.py has an error  as seen  in 
/var/log/supervisor/flask-stdout---supervisor-WQlNpO.log

so accessing the public http://104.236.40.212:5006
is accessing th bokeh directly without flask

Failed to install bokeh 0.13.0  in the droplet 

