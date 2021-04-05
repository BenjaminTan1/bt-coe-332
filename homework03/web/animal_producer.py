import random, uuid, datetime, json

userdata = [];
def add_data(animal):
	userdata.append(animal)

print (type(userdata))

heads = ['snake', 'raven', 'lion', 'bull', 'eagle', 'bunny']

for i in range(0,100):
	uid = str(uuid.uuid4())
	head = random.choice(heads)
	arms = random.randint(2,10)
	legs = random.randint(3,12)
	tails = random.randint(0,2)
	cdate = str(datetime.datetime.now())
	
	animal={}
	animal['uid'] = uid
	animal['head'] = head
	animal['arms'] = arms
	animal['legs'] = legs
	animal['tails'] = tails
	animal['created_on'] = cdate

	print(json.dumps(animal))
	
	add_data(animal)

with open('data_file.json', 'w') as write_file:
	json.dump(userdata, write_file)
