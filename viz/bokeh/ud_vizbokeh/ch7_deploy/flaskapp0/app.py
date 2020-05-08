#flask app

from flask import Flask, render_template

from BasicLine import js,div,cdn_js, cdn_css

from bokeh.embed import server_document

#instantiate the flask app
app = Flask(__name__)


bokeh_script=server_document("http://localhost:5006/random_generator")

#create index page function
@app.route("/")
def index():
    #session=pull_session(app_path="/random_generator")
    #bokeh_script=autoload_server(None,app_path="/random_generator",session_id=session.id)
    return render_template("index.html",js=js,div=div,cdn_js=cdn_js,cdn_css=cdn_css,
                           bokeh_script=bokeh_script)

#run the app
if __name__ == "__main__":
    app.run(debug=True)  #set this to False in Prod
