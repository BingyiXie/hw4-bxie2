import flask 

app = flask.Flask(__name__)

Shows =["Prison Break", "Gossip Girl", "Walking Dead", "Loki", "Dark"]

@app.route("/")
def index():
    # return "hello, world!"
    return flask.render_template("index.html", len = 1, Shows = Shows)
    

app.run()


