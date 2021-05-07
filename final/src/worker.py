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
    jobid, status, start, end = rd.hmget(generate_job_key(jid), 'id', 'status', 'start', 'end', 'outcome_type')
    data = json.loads(rd.get('data'))
    x_values_to_plot = []
    y_values_to_plot = []

    # Fill X and Y coordinates
    
    Euthanized = 0
    Returned = 0
    Adoption = 0
    Transfer = 0

    x_values_to_plot.append(1)
    x_values_to_plot.append(2)
    x_values_to_plot.append(3)
    x_values_to_plot.append(4)

    for key in rd.keys():
        outcome_type_key = str(rd.get(key, 'outcome_type'))
        if (outcome_type_key == 'Euthanasia'):
            Euthanized = Euthanized + 1
        if (outcome_type_key == 'Return to Owner'):
            Returned = Returned + 1
        if (outcome_type_key == 'Adoption'):
            Adoption = Adoption + 1
        if (outcome_type_key == 'Transfer'):
            Transfer = Transfer + 1
    
    y_values_to_plot.append(Euthanized)
    y_values_to_plot.append(Returned)
    y_values_to_plot.append(Adoption)
    y_values_to_plot.append(Transfer)

    plt.scatter(x_values_to_plot, y_values_to_plot)
    plt.xlabel('Outcome Type')
    plt.ylabel('Number of Animals')
    plt.savefig('/output_image.png')


    with open('/output_image.png', 'rb') as f:
        img = f.read()

    rd.hset(jobid, 'image', img)
    rd.hset(jobid, 'status', 'finished')

if __name__ == '__main__':
    execute_job()
