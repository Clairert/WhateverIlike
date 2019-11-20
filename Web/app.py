from flask import Flask, request, render_template
from mongoengine import *
import os
import csv

app = Flask(__name__)
connect('web3DB')

app.config.from_object('config')




class Country(Document):
	name = StringField()
	data = DictField()


@app.route('/')
@app.route('/index')
@app.route('/home')
def hello_world():
    pageName = "Web 3"
    for file in os.listdir(app.config['FILES_FOLDER']):
        filename = os.fsdecode(file)
        path = os.path.join(app.config['FILES_FOLDER'],filename)
        f = open(path)
        r = csv.DictReader(f) 
        d = list(r)
        for data in d:
            county = Country()
            dict = {}
            for key in data: # iterate through the header keys
                if key == "country":
                    # check if this country already exists in the db
                    if Country.objects(name=data[key]).count() > 0:
                        
                        county = Country.objects(name=data[key])[0]
                        dict = county.data
                        #found country
                        # if the country already exists, replace the blank country with the existing country from the db, and replace the blank dict with the current country's 
                        # data
                    else:
                        county.name = data[key]

                        #create country
                        # if the country does not exist, we can use the new blank country we created above, and set the name
                else:
                    f = filename.replace(".csv","") # we want to trim off the ".csv" as we can't save anything with a "." as a mongodb field name
                    if f in dict: # check if this filename is already a field in the dict
                        dict[f][key] = data[key] # if it is, just add a new subfield which is key : data[key] (value)
                    else:
                        dict[f] = {key:data[key]} # if it is not, create a new object and assign it to the dict
            county["data"] = dict
            Country.save(county)
                # add the data dict to the country

            # save the country
    
    return render_template("index.html", title=pageName), 200



@app.route('/inspiration')
def inspiration():
    pageName = "Inspiration"
    newcountry = Country(name="motivationLand")
    newcountry.save()
    return render_template("inspiration.html", title=pageName)


@app.route('/loadData')
def loadData():
    return "Success"

@app.route('/imga')
def imga():
    filename = "chris"
    return os.path.join(app.config['static_FOLDER'],filename)


@app.route('/countries', methods=['GET'])
@app.route('/countries/<country_id>', methods=['GET'])
def getCountries(country_id=None):
    Countries = Country.objects
    return Countries.to_json(), 200



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

