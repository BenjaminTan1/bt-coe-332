<h1>HOMEWORK 07 README</h1>
<p> I am very bad at making README.md files. Sorry </p>

<h2>PA</h2>
<h3>1.</h3>
<p>docker build -f Dockerfile -t benjamintan1/hw7:latest .</p>
<p>docker push benjamintan1/hw7:latest</p>
<h3>2.</h3>
<p>[btan9967@isp02 api]$ kubectl apply -f btan9967-hw7-flask-deployment.yml</p>
<p>[btan9967@isp02 api]$ kubectl apply -f btan9967-hw7-flask-service.yml</p>
<p>[btan9967@isp02 db]$ kubectl apply -f btan9967-hw7-redis-deployment.yml</p>
<p>[btan9967@isp02 db]$ kubectl apply -f btan9967-hw7-redis-pvc.yml</p>
<p>[btan9967@isp02 db]$ kubectl apply -f btan9967-hw7-redis-service.yml</p>
<p>[btan9967@isp02 worker]$ kubectl apply -f btan9967-hw7-worker-deployment.yml</p>
---
<p>Ouput Sample: deployment.apps/btan9967-hw7-worker-deployment created </p>
---
<p>This output is then repeated for all the kubectl apply commands.</p>
<h3>3.</h3>
<p> Then, we want to determine the IP address of our flask and redis and put it into our deployment files using: </p>
<p>[btan9967@isp02 homework07]$ kubectl get service </p>
<p>NAME                    TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE  </p>
<p>btan9967-hw07-flask     ClusterIP   10.96.24.170   <none>        5000/TCP   165m </p>
<p>btan9967-test-service   ClusterIP   10.102.161.2   <none>        6379/TCP   129m </p>
---
<p>We exec into a debug pod created previously with redis installed</p>
<p>kubectl exec -it py-debug-deployment-5cc8cdd65f-ttl84 -- /bin/bash</p>
<p>Then:</p>
<p>curl -X POST -H "content-type: application/json" -d '{"start": "go!", "end": "stop!"}' IP_ADDRESS_FLASK:5000/jobs</p>
<p>Output Sample: {"status": "submitted", "start": "go!", "end": "stop!", "id" ""23sf822-39b3-404c-9ba2-6e3df87b33b4"}
<p>Where IP_ADDRESS_FLASK is the address found upon kubectl get service.</p>
---
<p>Then, while this is running, we open up another terminal then, in an interactive python shell, execute commands:</p>
<p>In [1]: import redis</p>
<p>In [2]: rd = redis.StrictRedis(host="IP_ADDRESS_REDIS", port=6379, db=3)</p>
<p>Out [3]: rd.keys()</p>
<p>Out[3]:[b'23sf822-39b3-404c-9ba2-6e3df87b33b4']</p>
<p>In[4]: rd.hgetall('job.23sf822-39b3-404c-9ba2-6e3df87b33b4')</p>
<p>Out[4]:</p>
{b'status': b'complete',
 b'start': b'go!',
 b'end': b'stop!',
 b'id': b'23sf822-39b3-404c-9ba2-6e3df87b33b4',
 b'worker': b'WORKER_IP_ADDRESS'}</p>
 ---
<h2>PB</h2>
<p>Functionality added to worker.py and jobs.py. See above output for example of where the <WORKER_IP_ADDRESS> is printed.</p>
<h2>PC</h2>
<p>Using the debug pod, we do:</p>
<p>for i in range(1,10)</p>
<p>do</p>
<p>curl -X POST -H "content-type: application/json" -d '{"start": "go!", "end": "stop!"}'  IP_ADDRESS_FLASK:5000/jobs</p>
---
<p>{"status": "submitted", "start": "go!", "end": "stop!", "id": "93845f36-1522-4221-2da0-8963f6740e33"}</p>
<p>{"status": "submitted", "start": "go!", "end": "stop!", "id": "e8323442-8e38-4990-a712-8398822bf8a4"}</p>
<p>{"status": "submitted", "start": "go!", "end": "stop!", "id": "72c22e2d-3ec9-48cc-9c7e-24a01b638ff2"}</p>
<p>{"status": "submitted", "start": "go!", "end": "stop!", "id": "735247c5-1537-480b-a82a-da43891bda84"}</p>
<p>...</p>
<p>Same output wiht different UUID</p>
---
<p>Then when we run the same commands as before with print(rd.hgetall(key)) in the python interactive shell, we get that each worker did 5 tasks each</p>
<p>In [1]: import redis</p>
<p>In [2]: rd = redis.StrictRedis(host="IP_ADDRESS_REDIS", port=6379, db=3)</p>
<p>In [3]: for key in rd.keys():</p>
<p>   ...:     print(rd.hgetall(key))</p>
---
<p>Sample Output</p>
<p>{b'status': b'complete',
 b'start': b'go!',
 b'end': b'stop!',
 b'id': b'93845f36-1522-4221-2da0-8963f6740e33',
 b'worker': b'WORKER_IP_ADDRESS1'}</p>
 <p>{b'status': b'complete',
 b'start': b'go!',
 b'end': b'stop!',
 b'id': b'e8323442-8e38-4990-a712-8398822bf8a4',
 b'worker': b'WORKER_IP_ADDRESS2'}</p>
 ...
 ---
