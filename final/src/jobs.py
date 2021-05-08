#jobs.py
import uuid
import json
import hotqueue
import redis
import os
import sys

redis_ip = os.environ.get('REDIS_IP')
if not redis_ip:
    raise Exception()
#redis_ip = '10.101.199.157'

rd = redis.StrictRedis(host = redis_ip, port=6379, db = 0)
rd_jobs = redis.StrictRedis(host=redis_ip, port=6379, db=2)
rd_imgs = redis.StrictRedis(host=redis_ip, port=6379, db=3)
q = hotqueue.HotQueue('queue', host = redis_ip, port=6379, db=1)

def _generate_jid():
    return str(uuid.uuid4())

def _generate_job_key(jid):
    return 'job.{}'.format(jid)

def _instantiate_job(jid, status, start, end):
    if type(jid) == str:
        return {'id': jid,
                'status': status
        }
    return {'id': jid.decode('utf-8'),
            'status': status.decode('utf-8')
    }

def _save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd_jobs.hmset(job_key, job_dict)

def _queue_job(jid):
    """Add a job to the redis queue."""
    q.put(jid)

def add_job(animal_type, start, end, status="submitted"):
    """Add a job to the redis queue."""
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, status)
    _save_job(_generate_job_key(jid), job_dict)
    _queue_job(jid)
    return job_dict

def update_job_status(jid, new_status):
    """Update the status of job with job id `jid` to status `status`."""
    jid, status, datetime = rd.hmget(_generate_job_key(jid), 'id', 'status')
    job = _instantiate_job(jid, status)

    if job:
        job['status'] = new_status
        _save_job(_generate_job_key(job['id']), job)
    else:
        raise Exception()
