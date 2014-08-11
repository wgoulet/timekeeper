from flask import Flask
from flask import request
from flask import render_template
from flask import json
from flask_cors import cross_origin
from flask import jsonify
import pickle


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
        data = request.json
        savedata(data)
        print data    
        #return make_response(data)
        return "Saved"

    else:
        print "Unable to parse"
    return "Error"    

@app.route("/timesheet/getdata.json")
def fetchdata():
    data = loaddata()
    return jsonify(data=data)
     

def loaddata():
    f = open('datfile','r')
    return pickle.load(f)


def savedata(data):
    f = open('datfile','w')
    pickle.dump(data,f)
    

if __name__ == "__main__":
    app.run("0.0.0.0",5000)
