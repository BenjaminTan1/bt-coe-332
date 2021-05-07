#worker.py
from jobs import q, update_job_status, add_worker_ip
import matplotlib.pyplot as plt
import time
import datetime
import redis

#worker_ip = os.environ.get('WORKER_IP')
#if not worker_ip:
#    raise Exception()

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
#redis_ip = '10.101.199.157'

rd = redis.StrictRedis(host=redis_ip, port=6379, db=0)

# Analysis Job goes here:
# Create a graph of the Animal Type by date

@q.worker
def execute_job(jid):
    jobid, status, start, end = rd.hmget(generate_job_key(jid), 'id', 'status', 'start', 'end', 'animal_type')
    data = json.loads(rd.get('data'))
    x_values_to_plot = []
    y_values_to_plot = []

    # Fill values to plot...
    # Want x values to be Time, and y values to be the number of intakes on the date
    start = job['start']
    end = job['end']
    
    # Use datetime to pull the request startdate and enddate
    startdate = datetime.datetime.strptime(start,'%m-$d-%Y')

    enddate = datetime.datetime.strptime(end, '%m-%d-$Y')
    
    # initialize the base animal count per day at 0
    animalcount = 0
    for key in rd.keys():
        datetimekey = str(rd.get(key, 'DateTime'))
        if (start <= datetimekey
            x_values_to_plot.append(key)
            y_values_to_plot.append(key)

    plt.scatter(x_values_to_plot, y_values_to_plot)
    plt.xlabel('Time')
    plt.ylabel('Number of Intakes')
    plt.savefig('/output_image.png')


    with open('/output_image.png', 'rb') as f:
        img = f.read()

    rd.hset(jobid, 'image', img)
    rd.hset(jobid, 'status', 'finished')

if __name__ == '__main__':
    execute_job()
