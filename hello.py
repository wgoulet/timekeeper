from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/timesheet/main")
def index():
    return render_template('index.htm')

@app.route("/timesheet/")
def hello():
    return "hello world I'm back dude"

if __name__ == "__main__":
    app.run("0.0.0.0",5000)

@app.route("/timesheet/submit")
def submit():
    error = None
    if request.method == 'POST':
        return "Saved Data"
    return "Error"    


