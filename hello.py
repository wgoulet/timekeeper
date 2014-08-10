from flask import Flask
from flask import request
from flask import render_template
from flask import json
from flask_cors import cross_origin


app = Flask(__name__)

@app.route("/timesheet/main")
def index():
    return render_template('index.htm')

@app.route("/timesheet/")
def hello():
    return "hello world I'm back dude"


@app.route("/timesheet/savedata",methods=['POST','OPTIONS'])
@cross_origin()
def submit():
    error = None
    print request.method
    if request.method == 'POST':
        print "In method"    
        #import pdb; pdb.set_trace()
        data = request.form
        for i in data.iteritems(multi=True):
            print i
        
            
        #return make_response(data)
        return "testing"

    else:
        print "Unable to parse"
    return "Error"    


if __name__ == "__main__":
    app.run("0.0.0.0",5000)
