# --- Each Part of the Midterm is Labeled Next to the Function that Satisfies the Requirement ---

import json, redis, random, uuid, datetime
from flask import Flask, request

#rd = redis.StrictRedis(host = '127.0.0.1', port = 6411, db = 0)
rd = redis.StrictRedis(host = 'benjamin-redis', port = 6379, db = 0)

app = Flask(__name__)

def write_to_redis():
	with open("/data_file.json", "r") as json_file:
		userdata = json.load(json_file)
		for x in userdata:
			rd.hmset(str(x), x)
	return userdata

data = write_to_redis()

@app.route('/', methods = ['GET'])
def hello_world():
	return 'Hello World\n'

# --- 5. Returns the Average Number of Legs Per Animal ---
# Route that returns the average number of legs of all the animals. Iterates throughout the animals arraya, adds the legs, then divides by the length of the animal library.
@app.route('/animals/avg_legs', methods = ['GET'])
def get_avg_legs():
	leg_count = 0
	for x in data:
		leg_count += x['legs']
	leg_count = int(leg_count / len(data))
	return json.dumps(leg_count)

#print(get_avg_legs())

# --- 1. Query a Range of Dates ---
# Returns animals created between two dates. Default dates are arbitrarily chosen for ease of debugging.
@app.route('/animals/dates', methods = ['GET'])
def get_dates():
	start = request.args.get('start', "'2021-03-30_01:36:58.553084'")
	startdate = datetime.datetime.strptime(start, "'%Y-%m-%d_%H:%M:%S.%f'")
	end = request.args.get('end', "'2021-03-31_01:36:58.553084'")
	enddate = datetime.datetime.strptime(end, "'%Y-%m-%d_%H:%M:%S.%f'")
	
	animals = []

	for x in data:
		if (datetime.datetime.strptime( x['created_on'], '%Y-%m-%d %H:%M:%S.%f') >= startdate and datetime.datetime.strptime( x['created_on'], '%Y-%m-%d %H:%M:%S.%f') <= enddate ):
			animals.append(x)

	return json.dumps(animals)

# --- 4. Deletes a Selection of Animals by a Date Range ---
# Deletes animals created between two dates. Returns the deleted slots just for ease of debugging.
@app.route('/animals/dates/purge', methods = ['GET'])
def purge_dates():
	start = request.args.get('start', "'2021-03-30_01:36:58.553084'")
	startdate = datetime.datetime.strptime(start, "'%Y-%m-%d_%H:%M:%S.%f'")
	end = request.args.get('end', "'2021-03-31_01:36:58.553084'")
	enddate = datetime.datetime.strptime(end, "'%Y-%m-%d_%H:%M:%S.%f'")

	animals = []
	for x in data:
		if (datetime.datetime.strptime( x['created_on'], '%Y-%m-%d %H:%M:%S.%f') >= startdate and datetime.datetime.strptime( x['created_on'], '%Y-%m-%d %H:%M:%S.%f') <= enddate ):
			rd.delete(str(x))
			animals.append(rd.hgetall(str(x)))

	return json.dumps(animals)

# --- 6. Returns a Total Count of Animals ---
# Route that returns the total number of animals. Uses the fact that each animal is saved under a different key.
@app.route('/animals/total', methods = ['GET'])
def get_tot_animals():
	return json.dumps(len(rd.keys()))

#print(get_tot_animals())

# --- 2. Selects a Particular Creature by its Unique Identifier ---
# --- 3. Edits a Particular Creature by its Unique Identifier ---
# Selects a particular creature by its unique identifier. Also edits that create with updated 'stats' if a part or value are inserted into the URL. The uid is defaulted to a URL already known to be inside data_file.json for easy debugging.
@app.route('/animals/UID', methods = ['GET'])
def select_uid():
	uid = request.args.get('uid', '5baaf418-75fa-4621-be31-09aa31756e79')
	part = request.args.get('part')
	value = request.args.get('value')	

	for x in data:
		if(x['uid'] == uid):
			if(part != None):
				rd.hmset(str(x), {str(part): str(value)})
			return json.dumps(rd.hgetall(str(x)))
	return json.dumps(uid)

if __name__ == '__main__':
	app.run(debug=True, host='benjamin-web', port = '5000')
