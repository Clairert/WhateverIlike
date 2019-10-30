from flask import Flask, request, render_template
from mongoengine import *
import os
import csv

app = Flask(__name__)
connect('web3DB')

app.config.from_object('config')




class country(Document):
	name = StringField()



@app.route('/')
@app.route('/index')
@app.route('/home')
def hello_world():
    pageName = "Web 3"
    for file in os.listdir(app.config['FILES_FOLDER']):
        filename = os.fsdecode(file)
        path = os.path.join(app.config['FILES_FOLDER'],filename)
        f=open(path)
        r=csv.reader(f)
        d=list(r)
        for data in d:
            print(data)
    return render_template("index.html", title=pageName), 200



@app.route('/inspiration')
def inspiration():
    pageName = "Inspiration"
    newcountry = country(name="motivationLand")
    newcountry.save()
    return render_template("inspiration.html", title=pageName)


@app.route('/loadData')
def loadData():
    return "Success"


@app.route('/countries', methods=['GET'])
@app.route('/countries/<country_id>', methods=['GET'])
def getCountries(country_id=None):
    #Code goes here
    return "Success"



@app.route('/delete/<country_id>', methods=['DELETE'])
def deleteCountry(country_id):
    #codeGOESHERE
    return "Success"


@app.route('/newCountry', methods=['PUT'])
def addCountry():
    #CODECODEY
    return "Success"


if __name__=="__main__":
    app.run(debug=True, port=8080)

