from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return ("Hello, World!")

@app.route("/new")
def new():
    return ("This is new page")
app.run(debug=True)