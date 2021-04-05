import json
from flask import Flask, request

app = Flask(__name__)

def get_data():
	with open('data_file.json', 'r') as json_file:
		userdata = json.load(json_file)
	return userdata

@app.route('/', methods=['GET'])
def hello_world():
	return 'Hello World!\n'

@app.route('/<name>', methods = ['GET'])
def hello_name(name):
	return 'Hello, {}!\n'.format(name)

# Returns all animals.
@app.route('/animals', methods = ['GET'])
def get_animals():
	return json.dumps(get_data())

# Returns all animals with a specified head in the URL. Default type is snake.
@app.route('/animals/heads', methods = ['GET'])
def get_animal_heads():
	head_type = request.args.get('head_type', 'snake')
	animals = []
	for x in get_data():
		if x['head'] == head_type:
			animals.append(x)
	return json.dumps(animals)

@app.route('/animals/legs', methods = ['GET'])
def get_animal_legs():
	leg_type = request.args.get('leg_type', '6')
	animals = []
	for x in get_data():
		if x['legs'] == int(leg_type):
			animals.append(x)
	return json.dumps(animals)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
	




