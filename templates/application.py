from flask import Flask , render_template


app = Flask(__name__)

#function names in routes are mandatory

@app.route("/")
def index():
    return render_template("index.html")
