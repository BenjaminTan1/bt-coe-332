Step 1:
	[btan9967@isp02 homework06]$ kubectl apply -f btan9967-test-pvc.yml
	persistentvolumeclaim/btan9967-test-data unchanged
Step 2: 
	[btan9967@isp02 homework06]$ kubectl apply -f btan9967-test-service.yml
	service/btan9967-test-service unchanged
Step 3:
	[btan9967@isp02 homework06]$ kubectl apply -f btan9967-test-deployment.yml
	deployment.apps/btan9967-test-redis configured
Step 1-3 Check:
	[btan9967@isp02 homework06]$ kubectl exec -it py-debug-deployment-5cc8cdd65f-ttl84 -- /bin/bash
	root@py-debug-deployment-5cc8cdd65f-ttl84:/# python3
	Python 3.9.2 (default, Mar 31 2021, 12:13:11)
	[GCC 8.3.0] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import redis
	>>> rd = redis.StrictRedis(host='10.99.25.180', port=6379, db=0)
	>>> rd.set('m','1')
	True
	>>> quit()
	root@py-debug-deployment-5cc8cdd65f-ttl84:/# exit
	exit
	
	[btan9967@isp02 homework06]$ kubectl exec -it py-debug-deployment-5cc8cdd65f-ttl84 -- /bin/bash
	root@py-debug-deployment-5cc8cdd65f-ttl84:/# python3
	Python 3.9.2 (default, Mar 31 2021, 12:13:11)
	[GCC 8.3.0] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import redis
	>>> rd = redis.StrictRedis(host='10.99.25.180', port=6379, db=0)
	>>> rd.get('m')
	b'1'
Step 4:
	[btan9967@isp02 web]$ docker push benjamintan1/animals:latest
	The push refers to repository [docker.io/benjamintan1/animals]
	[btan9967@isp02 homework06]$ kubectl apply -f btan9967-test-deployment-flask.yml
	deployment.apps/btan9967-test-flask configured
Step 5:
	[btan9967@isp02 homework06]$ kubectl apply -f btan9967-test-service-flask.yml
	service/btan9967-test-flask created