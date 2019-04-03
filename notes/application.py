from flask import Flask , render_template , request , session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#notes=[]#is global for everyone...one change will effect all others ... check with two browsers #cookies with browser for identification

@app.route("/",methods=["GET","POST"])
def index():
    if session.get("notes") == None:
        session["notes"]=[]
    #to avoid overrriding for every note add op
    if request.method == "POST":
        note=request.form.get("note")
        # notes.append(note)
        session["notes"].append(note)

    return render_template("index.html",notes=session["notes"])#notes=notes"]
#data lost when server shut down! in the global mode but not in the session note list mode...so DATA BASE is the key!    