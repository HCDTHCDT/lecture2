from flask import Flask , render_template


app = Flask(__name__)

@app.route("/")
def index():
    headline="Hello ,world!"
    return render_template("index.html" , headline=headline)


#flsak debug mode to run automatically.... (export-Git bash...)/(set-CMD) FLASK_DEBUG=1

@app.route("/bye")
def bye():
    headline="Good bye!"
    return render_template("index.html" , headline=headline)