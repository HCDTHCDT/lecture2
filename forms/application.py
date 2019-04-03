from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/hello",methods=["POST","GET"]) #comment the "GET" and else in function and see the dif #also try without any methods arg.
def hello():
    if request.method=="GET":
        return "<h2>Please submit the form instead</h2>"
    else:    
        name=request.form.get("name")
        return render_template("hello.html",name=name)  
