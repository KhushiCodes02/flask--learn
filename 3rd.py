from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("1.html")

@app.route("/about")
def prince():
    name = "Harsh_Sahu"
    return render_template("2.html" , name2 = name)

@app.route("/boot")
def boot():
    return render_template("index.html")

@app.route("/bootstrap")
def bootstrap():
    return render_template("boot.html")
app.run(debug=True)