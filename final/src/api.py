#api.py
import json
from flask import Flask, request
import jobs
import requests
import redis
import os
import uuid
import datetime
import hotqueue

# Sets the redis IP_ADDRESS from the service.

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
#redis_ip = '10.101.199.157'

app = Flask(__name__)
rd = redis.StrictRedis(host = redis_ip, port=6379, db = 0)
rd_jobs = redis.StrictRedis(host=redis_ip, port=6379, db=2)
rd_imgs = redis.StrictRedis(host=redis_ip, port=6379, db=3)
q = hotqueue.HotQueue('queue', host = redis_ip, port=6379, db=1)

# Returns the data under the given key.
def get_data():
    with open("data.json","r") as json_file:
        userdata = json.load(json_file)
    return userdata

@app.route('/', methods=['GET'])
def instructions():
    return """
    The route are as follows:
    curl <host>:<flask_port>/                            								# General info.
    curl <host>:<flask_port>/load                        								# Adds data.json info to the database.
    curl <host>:<flask_port>/getAll                      								# Returns the database.
    curl <host>:<flask_port>/getAnimal/?animal_id=...    								# Query an animal ID.
    curl <host>:<flask_port>/outcomeType/<outcome_type>  								# Sort by outcome type. 
    curl <host>:<flask_port>/updateAnimal/?animal_id=... 								# Updates an animal with an animal ID specified.
    curl -X POST -H "content-type: application/json" -d '{<Animal>} <host>:<flask_port>/addAnimal 			# Add an animal.
    curl <host>:<flask_port>/delete/?animal_id=...       								# Deletes an animal with an animal ID specified.
    curl -X POST -d <host>:<flask_port>/jobs                        							# Lists jobs.
    curl <host>:<flask_port>/download/<jobuuid>          								# Obtains image from a job.
    
"""
# Loads data into the redis database.
@app.route('/load', methods=['GET'])
def loaddata():
    with open("data.json","r") as f:
        dict = json.load(f)
    
    rd.set('key', json.dumps(dict, indent=2))
        
    return 'The file data.json was imported into database.\n'

@app.route('/getAll', methods=['GET'])
def GetAll():
    return json.dumps(get_data(), indent=2)

# Create Route
@app.route('/addAnimal', methods = ['GET','POST'])
def Add():
    add = request.json
    
    test = get_data()
    test.append(add)
    rd.set('key', json.dumps(test))

    return json.dumps(get_data(), indent=2)

# Read Route
@app.route('/getAnimal/', methods=['GET'])
def Get_Animal():
    test = get_data()
    output= {}
    animal_id = request.args.get('animal_id')
    for x in test:
        if x['animal_id'] == animal_id:
            output = x

    return json.dumps(output, indent = 2)

# Update Route
@app.route('/updateAnimal/', methods=['GET'])
def Update():
    test = get_data()

    animal_id = request.args.get('animal_id')
    name = request.args.get('name')
    datetime = request.args.get('datetime')
    monthyear = request.args.get('monthyear')
    date_of_birth = request.args.get('date_of_birth')
    outcome_type = request.args.get('outcome_type')
    outcome_subtype = request.args.get('outcome_subtype')
    animal_type = request.args.get('animal_type')
    sex_upon_outcome = request.args.get('sex_upon_outcome')
    age_upon_outcome = request.args.get('age_upon_outcome')
    breed = request.args.get('breed')
    color = request.args.get('color')

    # Creates a variable for outputting the updated animal.
    output = {}

    for x in test:
        if x['animal_id'] == animal_id:
            x['name'] = name
            x['datetime'] = datetime
            x['monthyear'] = monthyear
            x['date_of_birth'] = date_of_birth
            x['outcome_type'] = outcome_type
            x['animal_type'] = animal_type
            x['sex_upon_outcome'] = sex_upon_outcome
            x['age_upon_outcome'] = age_upon_outcome
            x['breed'] = breed
            x['color'] = color
            output = x
         
    rd.set('key', json.dumps(test))
    return json.dumps(output, indent=2)

# Delete Route
@app.route('/delete/', methods=['GET'])
def delete():
    test = get_data()
    animal_id = request.args.get('animal_id')
    for x in test:
        if x['animal_id'] == animal_id:
            test.remove(x)
    
    rd.set('key', json.dumps(test))

    return 'Animal deleted.'

# Job for making matlab plots
@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    
    return json.dumps(jobs.add_job(job['start'], job['end']))

# Image download
@app.route('/download/<jobuuid>', methods=['GET'])
def download(jobuuid):
    path = f'/app/{jobuuid}.png'
    with open(path, 'wb') as f:
        f.write(rd_imgs.hget(jobuuid, 'image'))
    return send_file(path, mimetype='image/png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
