#api.py
import json
from flask import Flask, request
import jobs
import requests
import redis
import os
import uuid
import datetime

# Sets the redis IP_ADDRESS from the service.

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
#redis_ip = '10.101.199.157'

app = Flask(__name__)
rd = redis.StrictRedis(host = redis_ip, port=6379, db = 0)
q = HotQueue('queue', host = redis_ip, port=6379, db=1)

# Returns the data under the given key.
def get_data():
    return json.loads(rd.get('intakes_key').decode('utf-8'))

@app.route('/', methods=['GET'])
def instructions():
    return """
    Try these routes:
    /                            # General info.
    /load                        # Adds data.json info to the database.
    /getAll                      # Returns the database.
    /getAnimal/?Animal_ID=...    # Query an animal ID.
    /animalType/<Animal_Type>           # Sort by animal type. 
    /updateAnimal/?Animal_ID=... # Updates an animal with an animal ID specified
    /addAnimal                   # Adds an animal.
    /delete/?Animal_ID=...       # Deletes an animal with an animal ID specified
    /jobs                        # Lists jobs.
    /download/<jobuuid>
    
"""
# Loads data into the redis database.
@app.route('/load', methods=['GET'])
def loaddata():
    with open("data.json","r") as f:
        dict = json.load(f)
    
    rd.set('intakes_key', json.dumps(dict, indent=2))
        
    return 'The file data.json was imported into database.\n'

@app.route('/getAll', methods=['GET'])
def GetAll():
    return json.dumps(get_data(), indent=2)

# Route to add an animal
@app.route('/addAnimal', methods = ['GET','POST'])
def Add():
    try:
        add = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    
    test = get_data()
    test['intakes'].append(add)
    rd.set('intakes_key', json.dumps(test))

    return json.dumps(get_data, indent=2)

# Route to fulfill the R of CRUD
@app.route('/getAnimal/', methods=['GET'])
def Get_Animal():
    test = get_data()
    output= {}
    animal_id = request.args.get('Animal_ID')
    for x in test['intakes']:
        if x['Animal ID'] == animal_id:
            output = x

    return json.dumps(output, indent = 2)

# Route to fulfill the U of CRUD
@app.route('/updateAnimal/', methods=['GET'])
def Update():
    test = get_data()

    animal_id = request.args.get('Animal_ID')
    name = request.args.get('name')
    intaketype = request.args.get('intaketype')
    intakecondition = request.args.get('intakecondition')
    animaltype = request.args.get('Animal_Type')
    breed = request.args.get('breed')
    color = request.args.get('color')

    intake = {}
    for x in test['intakes']:
        if x['Animal ID'] == animal_id:
            x['Name'] = name
            x['Intake Type'] = intaketype
            x['Intake Condition'] = intakecondition
            x['Animal_Type'] = animaltype
            x['Breed'] = breed
            x['Color'] = color
        
    rd.set('intakes_key', json.dumps(test))
    return json.dumps(intake, indent=2)

# Route to fulfill the D of CRUD
@app.route('/delete/', methods=['GET'])
def delete():
    test = get_data()
    animal_id = request.args.get('Animal_ID')
    for x in test['intakes']:
        if x['Animal ID'] == animal_id:
            test['intakes'].remove(x)
    
    rd.set('intakes_key', json.dumps(test))

    return 'Animal with ID {} deleted.'.format(animal_id)

# Filter by animal type/ extra route (Dog, Cat, Bird, Other)
@app.route('/animalType/<Animal_Type>', methods=['GET'])
def SortByType(Animal_Type):
    test = get_data()
    jsonList = test['intakes']

    output = [x for x in jsonList if x['Animal Type'] == Animal_Type]

    return json.dumps(output, indent=2)

# Allows the user to submit a Job request for the worker that uses the DateTime to graph the number of animals during that time
@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    
    return json.dumps(jobs.add_job(job['start'], job['end']))

# Download image based on ID
@app.route('/download/<jobuuid>', methods=['GET'])
def download(jobuuid):
    path = f'/app/{jobuuid}.png'
    with open(path, 'wb') as f:
        f.write(rd.hget(jobuuid, 'image'))
    return send_file(path, mimetype='image/png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
