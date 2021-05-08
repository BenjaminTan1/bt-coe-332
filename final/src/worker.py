#worker.py
from jobs import q, update_job_status
import matplotlib.pyplot as plt
import time
import datetime
import os
import redis

#worker_ip = os.environ.get('WORKER_IP')
#if not worker_ip:
#    raise Exception()

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
#redis_ip = '10.101.199.157'

rd = redis.StrictRedis(host = redis_ip, port=6379, db = 0)
rd_jobs = redis.StrictRedis(host=redis_ip, port=6379, db=2)
rd_imgs = redis.StrictRedis(host=redis_ip, port=6379, db=3)

# Create a graph of the Animal Type by date

@q.worker
def execute_job(jid):
    
    update_job_status(jid, 'in progress')
    
    animals = json.loads(rd.get('key'))
    outputType = animals['output_type']

    job_id = 'job.{}'.format(jid)
    
    euthanasia = 0
    returnedToOwner = 0
    adoption = 0
    transfer = 0

    for x in outputType:
        if x == 'Euthanasia':
            euthanasia = euthanasia + 1
        if x == 'Return to Owner':
            returnedToOwner = returnedToOwner + 1
        if x == 'Adoption':
            adoption = adoption + 1
        if x == 'Transfer':
            transfer = transfer + 1

    x = ['Euthanasia','Return to Owner', 'Adoption','Transfer']
    y = [euthanasia, returnedToOwner, adoption, transfer]

    plt.figure()

    plt.bar(y)
    plt.set(gca, 'XTickLabel',{'EU','RTO','ADP','TR'})

    plt.savefig('/outputtype.png')
    with open('/outputtype.png','rb') as f:
        img = f.read()

    rd_imgs.hset(jid,'image',img)
    update_job_status(jid, 'complete')

if __name__ == '__main__':
    execute_job()
